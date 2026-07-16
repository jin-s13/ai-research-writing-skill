#!/usr/bin/env python3
"""Verify evidence-sensitive manuscript numbers against a provenance registry."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path

from paper_contract import ContractError, collect_tex_text, load_json_object


SCHEMA_VERSION = "ai-research-writing/numeric-evidence-v2"
ROOT_FIELDS = {"schema_version", "entries"}
ENTRY_FIELDS = {"value", "source", "selector", "aggregate", "representations", "tolerance", "note"}
SELECTOR_FIELDS = {"kind", "pointer", "column", "where"}
SELECTOR_KINDS = {"json-pointer", "jsonl", "csv", "tsv"}
AGGREGATES = {"identity", "mean", "sample-std", "population-std", "sum", "min", "max", "count"}
REPRESENTATIONS = {"raw", "percent"}
STRICT_SECTION_TERMS = {
    "result",
    "experiment",
    "evaluation",
    "ablation",
    "analysis",
    "finding",
    "benchmark",
}
SECTION_RE = re.compile(r"\\(?:section|subsection|subsubsection)\*?\{([^}]*)\}", re.IGNORECASE)
TABLE_RE = re.compile(
    r"\\begin\{(table\*?|tabular\*?|tabularx|longtable)\}.*?\\end\{\1\}",
    re.DOTALL,
)
NUMBER_RE = re.compile(r"(?<![A-Za-z_\\])([+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?)(?![A-Za-z_])")
SKIP_RE = re.compile(
    r"\\(?:cite|citep|citet|citealp|citealt|citeauthor|citeyear|ref|eqref|pageref|label)"
    r"\*?(?:\[[^\]]*\]){0,2}\{[^}]*\}|"
    r"\\(?:url|path|input|include|includegraphics)(?:\[[^\]]*\])?\{[^}]*\}|"
    r"\\href\{[^}]*\}\{[^}]*\}|"
    r"\\(?:begin|end)\{[^}]*\}",
    re.DOTALL,
)


@dataclass(frozen=True)
class EvidenceValue:
    value: float
    source: str
    tolerance: float

    def matches(self, candidate: float) -> bool:
        return math.isclose(candidate, self.value, rel_tol=self.tolerance, abs_tol=self.tolerance)


@dataclass(frozen=True)
class NumericFinding:
    value: float
    line: int
    section: str
    context: str


def _source_path(root: Path, raw: str) -> Path:
    if not raw:
        raise ContractError(f"Numeric evidence source has no file path: {raw}")
    if "#" in raw:
        raise ContractError("Numeric evidence v2 keeps JSON pointers in selector.pointer, not source fragments")
    path = (root / raw).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ContractError(f"Numeric evidence source escapes project root: {raw}") from exc
    if not path.is_file():
        raise ContractError(f"Numeric evidence source does not exist: {raw}")
    return path


def _json_pointer(value: object, pointer: str, source: str) -> object:
    if pointer == "":
        return value
    if not pointer.startswith("/"):
        raise ContractError(f"Numeric evidence JSON Pointer must begin with '/': {source}#{pointer}")
    for raw_token in pointer[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict) and token in value:
            value = value[token]
        elif isinstance(value, list) and token.isdigit() and int(token) < len(value):
            value = value[int(token)]
        else:
            raise ContractError(f"Numeric evidence JSON Pointer does not resolve: {source}#{pointer}")
    return value


def _matches_where(row: dict[str, object], where: dict[str, object]) -> bool:
    return all(str(row.get(key)) == str(expected) for key, expected in where.items())


def _selected_values(path: Path, source: str, selector: dict[str, object]) -> list[float]:
    unknown = sorted(set(selector) - SELECTOR_FIELDS)
    if unknown:
        raise ContractError("Numeric evidence selector contains unknown fields: " + ", ".join(unknown))
    kind = selector.get("kind")
    if kind not in SELECTOR_KINDS:
        raise ContractError(f"Numeric evidence selector.kind must be one of: {', '.join(sorted(SELECTOR_KINDS))}")
    where = selector.get("where", {})
    if not isinstance(where, dict) or any(not isinstance(key, str) or not key for key in where):
        raise ContractError("Numeric evidence selector.where must be an object with non-empty string keys")

    selected: list[object]
    if kind == "json-pointer":
        pointer = selector.get("pointer")
        if not isinstance(pointer, str):
            raise ContractError("json-pointer selector requires a string pointer")
        if path.suffix.lower() != ".json":
            raise ContractError(f"json-pointer selector requires a .json source: {source}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ContractError(f"Cannot read numeric evidence JSON source: {source}: {exc}") from exc
        value = _json_pointer(payload, pointer, source)
        selected = value if isinstance(value, list) else [value]
    elif kind in {"csv", "tsv"}:
        column = selector.get("column")
        if not isinstance(column, str) or not column:
            raise ContractError(f"{kind} selector requires a non-empty column")
        delimiter = "," if kind == "csv" else "\t"
        try:
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle, delimiter=delimiter)
                if reader.fieldnames is None or column not in reader.fieldnames:
                    raise ContractError(f"Numeric evidence column {column!r} is missing from {source}")
                selected = [row[column] for row in reader if _matches_where(row, where)]
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            raise ContractError(f"Cannot read numeric evidence {kind.upper()} source: {source}: {exc}") from exc
    else:
        column = selector.get("column")
        if not isinstance(column, str) or not column:
            raise ContractError("jsonl selector requires a non-empty column")
        selected = []
        try:
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ContractError(f"Invalid JSONL at {source}:{line_number}: {exc}") from exc
                if not isinstance(row, dict):
                    raise ContractError(f"JSONL record at {source}:{line_number} must be an object")
                if _matches_where(row, where):
                    if column not in row:
                        raise ContractError(f"JSONL column {column!r} is missing at {source}:{line_number}")
                    selected.append(row[column])
        except (OSError, UnicodeDecodeError) as exc:
            raise ContractError(f"Cannot read numeric evidence JSONL source: {source}: {exc}") from exc

    if not selected:
        raise ContractError(f"Numeric evidence selector matched no values in {source}")
    values: list[float] = []
    for item in selected:
        if isinstance(item, bool):
            raise ContractError(f"Numeric evidence selector produced a boolean in {source}")
        try:
            number = float(item)
        except (TypeError, ValueError) as exc:
            raise ContractError(f"Numeric evidence selector produced a non-number in {source}: {item!r}") from exc
        if not math.isfinite(number):
            raise ContractError(f"Numeric evidence selector produced a non-finite value in {source}")
        values.append(number)
    return values


def _aggregate(values: list[float], operation: str, source: str) -> float:
    if operation not in AGGREGATES:
        raise ContractError(f"Numeric evidence aggregate must be one of: {', '.join(sorted(AGGREGATES))}")
    if operation == "identity":
        if len(values) != 1:
            raise ContractError(f"identity aggregate requires exactly one selected value in {source}")
        return values[0]
    if operation == "mean":
        return statistics.fmean(values)
    if operation == "sample-std":
        if len(values) < 2:
            raise ContractError(f"sample-std requires at least two values in {source}")
        return statistics.stdev(values)
    if operation == "population-std":
        return statistics.pstdev(values)
    if operation == "sum":
        return math.fsum(values)
    if operation == "min":
        return min(values)
    if operation == "max":
        return max(values)
    if operation == "count":
        return float(len(values))
    raise AssertionError(operation)


def load_registry(root: Path, registry_path: Path) -> list[EvidenceValue]:
    registry = load_json_object(registry_path)
    unknown_root = sorted(set(registry) - ROOT_FIELDS)
    if unknown_root:
        raise ContractError("numeric_evidence.json contains unknown fields: " + ", ".join(unknown_root))
    if registry.get("schema_version") != SCHEMA_VERSION:
        raise ContractError(f"numeric_evidence.json schema_version must be {SCHEMA_VERSION}")
    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ContractError("numeric_evidence.json requires a non-empty entries list")

    values: list[EvidenceValue] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ContractError(f"numeric_evidence.json entries[{index}] must be an object")
        unknown = sorted(set(entry) - ENTRY_FIELDS)
        if unknown:
            raise ContractError(
                f"numeric_evidence.json entries[{index}] contains unknown fields: " + ", ".join(unknown)
            )
        value = entry.get("value")
        source = entry.get("source")
        selector = entry.get("selector")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)):
            raise ContractError(f"numeric_evidence.json entries[{index}].value must be a finite number")
        if not isinstance(source, str) or not source:
            raise ContractError(f"numeric_evidence.json entries[{index}].source must be a non-empty path")
        if not isinstance(selector, dict):
            raise ContractError(f"numeric_evidence.json entries[{index}].selector must be an object")
        operation = entry.get("aggregate", "identity")
        if not isinstance(operation, str):
            raise ContractError(f"numeric_evidence.json entries[{index}].aggregate must be a string")
        tolerance = entry.get("tolerance", 1e-6)
        if not isinstance(tolerance, (int, float)) or isinstance(tolerance, bool) or tolerance < 0:
            raise ContractError(f"numeric_evidence.json entries[{index}].tolerance must be non-negative")
        representations = entry.get("representations", ["raw"])
        if (
            not isinstance(representations, list)
            or not representations
            or any(item not in REPRESENTATIONS for item in representations)
        ):
            raise ContractError(
                f"numeric_evidence.json entries[{index}].representations must contain raw and/or percent"
            )
        numeric = float(value)
        source_path = _source_path(root, source)
        computed = _aggregate(_selected_values(source_path, source, selector), operation, source)
        if not math.isclose(computed, numeric, rel_tol=float(tolerance), abs_tol=float(tolerance)):
            raise ContractError(
                f"Numeric evidence value {numeric:g} does not match computed source value {computed:g}: {source}"
            )
        if "raw" in representations:
            values.append(EvidenceValue(numeric, source, float(tolerance)))
        if "percent" in representations:
            values.append(EvidenceValue(numeric * 100.0, source, float(tolerance)))
    return values


def _mask_ranges(text: str, pattern: re.Pattern[str]) -> str:
    chars = list(text)
    for match in pattern.finditer(text):
        for index in range(match.start(), match.end()):
            if chars[index] != "\n":
                chars[index] = " "
    return "".join(chars)


def find_unverified_numbers(text: str, evidence: list[EvidenceValue]) -> list[NumericFinding]:
    cleaned = _mask_ranges(text, SKIP_RE)
    table_ranges = [(match.start(), match.end()) for match in TABLE_RE.finditer(cleaned)]
    sections = [(match.start(), match.group(1).strip()) for match in SECTION_RE.finditer(cleaned)]
    cleaned = _mask_ranges(cleaned, SECTION_RE)
    findings: list[NumericFinding] = []
    current_section = ""
    section_index = 0

    for match in NUMBER_RE.finditer(cleaned):
        while section_index < len(sections) and sections[section_index][0] <= match.start():
            current_section = sections[section_index][1]
            section_index += 1
        in_table = any(start <= match.start() < end for start, end in table_ranges)
        strict_section = any(term in current_section.lower() for term in STRICT_SECTION_TERMS)
        if not in_table and not strict_section:
            continue
        candidate = float(match.group(1).replace(",", ""))
        if any(item.matches(candidate) for item in evidence):
            continue
        line_start = cleaned.rfind("\n", 0, match.start()) + 1
        line_end = cleaned.find("\n", match.end())
        if line_end == -1:
            line_end = len(cleaned)
        findings.append(
            NumericFinding(
                value=candidate,
                line=cleaned.count("\n", 0, match.start()) + 1,
                section=current_section or "table/outside named section",
                context=" ".join(cleaned[line_start:line_end].split())[:180],
            )
        )
    return findings


def verify_project(root: Path, main_tex: Path, registry_path: Path) -> list[NumericFinding]:
    evidence = load_registry(root, registry_path)
    return find_unverified_numbers(collect_tex_text(main_tex), evidence)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--main", help="Main TeX path relative to the project")
    parser.add_argument("--registry", default="numeric_evidence.json", help="Registry path relative to the project")
    args = parser.parse_args()

    root = args.project_path.resolve()
    if not root.is_dir():
        print(f"Project directory does not exist: {root}", file=sys.stderr)
        return 2
    try:
        if args.main:
            main_tex = root / args.main
        else:
            state = load_json_object(root / "paper_state.json")
            main_value = state.get("main_tex")
            if not isinstance(main_value, str) or not main_value:
                raise ContractError("paper_state.json main_tex must be a non-empty path")
            main_tex = root / main_value
        findings = verify_project(root, main_tex, root / args.registry)
    except ContractError as exc:
        print(f"Numeric evidence check failed: {exc}", file=sys.stderr)
        return 2

    if findings:
        print("Unverified numbers in evidence-sensitive manuscript regions:")
        for finding in findings:
            print(f"  collected line {finding.line} [{finding.section}]: {finding.value:g} | {finding.context}")
        return 1
    print("Numeric evidence check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
