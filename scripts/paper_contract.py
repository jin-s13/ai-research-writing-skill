#!/usr/bin/env python3
"""Shared strict parsing helpers for paper quality checks."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]*)\}")
GRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")
CITE_RE = re.compile(
    r"\\(?:cite|citep|citet|citealp|citealt|citeauthor|citeyear|"
    r"parencite|textcite|autocite|footcite|supercite|nocite)"
    r"\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}"
)
BIB_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")
GRAPHIC_SUFFIXES = ("", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")


class ContractError(RuntimeError):
    """Raised when a declared paper input cannot be read or resolved."""


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ContractError(f"Required file does not exist: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ContractError(f"Required text file is not valid UTF-8: {path}") from exc
    except OSError as exc:
        raise ContractError(f"Required file cannot be read: {path}: {exc}") from exc


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        escaped = False
        out: list[str] = []
        for char in line:
            if char == "%" and not escaped:
                break
            out.append(char)
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def resolve_tex(parent: Path, value: str) -> Path:
    path = (parent / value).resolve()
    return path if path.suffix else path.with_suffix(".tex")


def collect_tex_files(main_tex: Path) -> list[Path]:
    ordered: list[Path] = []
    seen: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen:
            return
        seen.add(path)
        text = strip_comments(read_utf8(path))
        ordered.append(path)
        for match in INPUT_RE.finditer(text):
            child = resolve_tex(path.parent, match.group(1).strip())
            if not child.is_file():
                raise ContractError(f"Missing LaTeX input declared by {path}: {child}")
            visit(child)

    visit(main_tex)
    return ordered


def collect_tex_text(main_tex: Path) -> str:
    return "\n".join(strip_comments(read_utf8(path)) for path in collect_tex_files(main_tex))


def resolve_graphics(main_tex: Path) -> list[Path]:
    resolved: list[Path] = []
    for tex_path in collect_tex_files(main_tex):
        text = strip_comments(read_utf8(tex_path))
        for match in GRAPHICS_RE.finditer(text):
            raw = match.group(1).strip()
            candidates = [(tex_path.parent / f"{raw}{suffix}").resolve() for suffix in GRAPHIC_SUFFIXES]
            found = next((candidate for candidate in candidates if candidate.is_file()), None)
            if found is None:
                raise ContractError(f"Missing graphic declared by {tex_path}: {raw}")
            resolved.append(found)
    return sorted(set(resolved))


def collect_citation_keys(main_tex: Path) -> set[str]:
    keys: set[str] = set()
    for match in CITE_RE.finditer(collect_tex_text(main_tex)):
        for raw_key in match.group(1).split(","):
            key = raw_key.strip()
            if key and key != "*":
                keys.add(key)
    return keys


def collect_bib_keys(bib_path: Path) -> list[str]:
    return [match.group(1).strip() for match in BIB_RE.finditer(read_utf8(bib_path))]


def load_json_object(path: Path) -> dict[str, object]:
    try:
        value = json.loads(read_utf8(path))
    except json.JSONDecodeError as exc:
        raise ContractError(f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"Expected a JSON object in {path}")
    return value


def paper_input_files(root: Path, main_tex: Path, bibliography: Path) -> list[Path]:
    files = collect_tex_files(main_tex)
    files.extend(resolve_graphics(main_tex))
    if not bibliography.is_file():
        raise ContractError(f"Required bibliography does not exist: {bibliography}")
    files.append(bibliography.resolve())
    return sorted(set(path.resolve() for path in files), key=lambda path: str(path.relative_to(root.resolve())))


def digest_files(root: Path, paths: list[Path], external_records: list[str] | None = None) -> str:
    root = root.resolve()
    digest = hashlib.sha256()
    for path in paths:
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root)
        except ValueError as exc:
            raise ContractError(f"Build input escapes project root: {resolved}") from exc
        digest.update(relative.as_posix().encode("utf-8"))
        digest.update(b"\0")
        try:
            digest.update(resolved.read_bytes())
        except OSError as exc:
            raise ContractError(f"Build input cannot be read: {resolved}: {exc}") from exc
        digest.update(b"\0")
    for record in sorted(external_records or []):
        digest.update(b"external\0")
        digest.update(record.encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def digest_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except FileNotFoundError as exc:
        raise ContractError(f"Required file does not exist: {path}") from exc
    except OSError as exc:
        raise ContractError(f"Required file cannot be read: {path}: {exc}") from exc
