#!/usr/bin/env python3
"""Verify evidence-sensitive manuscript numbers against a provenance registry."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from paper_contract import ContractError, collect_tex_text, load_json_object


SCHEMA_VERSION = "ai-research-writing/numeric-evidence-v1"
ROOT_FIELDS = {"schema_version", "entries"}
ENTRY_FIELDS = {"value", "source", "locator", "representations", "tolerance", "note"}
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
    path_part = raw.split("#", 1)[0]
    if not path_part:
        raise ContractError(f"Numeric evidence source has no file path: {raw}")
    path = (root / path_part).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ContractError(f"Numeric evidence source escapes project root: {raw}") from exc
    if not path.is_file():
        raise ContractError(f"Numeric evidence source does not exist: {raw}")
    return path


def _verify_json_pointer(path: Path, raw_source: str, expected: float, tolerance: float) -> None:
    if "#" not in raw_source:
        return
    fragment = raw_source.split("#", 1)[1]
    if path.suffix.lower() != ".json":
        raise ContractError(f"Numeric evidence fragments require a JSON source: {raw_source}")
    if not fragment.startswith("/"):
        raise ContractError(f"Numeric evidence JSON fragment must be a JSON Pointer beginning with '/': {raw_source}")
    try:
        value: object = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"Cannot read numeric evidence JSON source: {raw_source}: {exc}") from exc
    for raw_token in fragment[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict) and token in value:
            value = value[token]
        elif isinstance(value, list) and token.isdigit() and int(token) < len(value):
            value = value[int(token)]
        else:
            raise ContractError(f"Numeric evidence JSON Pointer does not resolve: {raw_source}")
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)):
        raise ContractError(f"Numeric evidence JSON Pointer is not a finite number: {raw_source}")
    if not math.isclose(float(value), expected, rel_tol=tolerance, abs_tol=tolerance):
        raise ContractError(
            f"Numeric evidence value {expected:g} does not match source value {float(value):g}: {raw_source}"
        )


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
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)):
            raise ContractError(f"numeric_evidence.json entries[{index}].value must be a finite number")
        if not isinstance(source, str) or not source:
            raise ContractError(f"numeric_evidence.json entries[{index}].source must be a non-empty path")
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
        _verify_json_pointer(source_path, source, numeric, float(tolerance))
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
