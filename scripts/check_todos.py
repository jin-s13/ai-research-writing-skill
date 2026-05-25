#!/usr/bin/env python3
"""Detect unresolved TODO-like markers before paper submission."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "venv",
    ".venv",
    "build",
    "dist",
}

TEXT_SUFFIXES = {
    ".tex",
    ".bib",
    ".md",
    ".txt",
    ".sty",
    ".cls",
    ".py",
    ".sh",
    ".yaml",
    ".yml",
    ".json",
    ".csv",
    ".tsv",
    ".svg",
}

MARKER_RE = re.compile(
    r"\b(TODO|FIXME|TBD|XXX|PLACEHOLDER|CITATION\s+NEEDED|answerTODO|justificationTODO)\b",
    re.IGNORECASE,
)


def iter_files(paths: list[Path]):
    for path in paths:
        if path.is_dir():
            for child in path.rglob("*"):
                if any(part in SKIP_DIRS for part in child.parts):
                    continue
                if child.is_file() and child.suffix.lower() in TEXT_SUFFIXES:
                    yield child
        elif path.is_file():
            yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="latin-1")
        except UnicodeDecodeError:
            return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument(
        "--allow",
        action="append",
        default=[],
        help="Regex pattern for lines that should not be reported",
    )
    args = parser.parse_args()

    allow_res = [re.compile(pattern) for pattern in args.allow]
    findings: list[tuple[Path, int, str]] = []

    for path in iter_files(args.paths):
        text = read_text(path)
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if not MARKER_RE.search(line):
                continue
            if any(pattern.search(line) for pattern in allow_res):
                continue
            findings.append((path, lineno, line.strip()))

    if findings:
        print("Unresolved TODO-like markers:")
        for path, lineno, line in findings:
            print(f"  {path}:{lineno}: {line}")
        return 1

    print("No unresolved TODO-like markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
