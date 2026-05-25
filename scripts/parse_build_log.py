#!/usr/bin/env python3
"""Summarize important LaTeX build log issues."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = {
    "errors": re.compile(r"^! .+", re.MULTILINE),
    "emergency": re.compile(r"Emergency stop|Fatal error occurred", re.IGNORECASE),
    "undefined_citations": re.compile(r"(?:Citation|Package natbib Warning: Citation) [`']?([^'`]+)[`']?.*undefined", re.IGNORECASE),
    "undefined_references": re.compile(r"Reference [`']?([^'`]+)[`']?.*undefined", re.IGNORECASE),
    "overfull": re.compile(r"Overfull \\hbox .*", re.MULTILINE),
    "underfull": re.compile(r"Underfull \\hbox .*", re.MULTILINE),
    "missing_files": re.compile(r"LaTeX Error: File `([^']+)' not found", re.IGNORECASE),
}


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        item = item.strip()
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", type=Path)
    parser.add_argument("--max-lines", type=int, default=20)
    args = parser.parse_args()

    text = args.log_file.read_text(encoding="utf-8", errors="replace")
    findings = {name: unique(pattern.findall(text)) for name, pattern in PATTERNS.items()}

    print(f"# Build Log Summary: {args.log_file}")
    print()
    exit_code = 0
    for name, items in findings.items():
        count = len(items)
        print(f"## {name.replace('_', ' ').title()} ({count})")
        if items:
            for item in items[: args.max_lines]:
                print(f"- {item}")
            if count > args.max_lines:
                print(f"- ... {count - args.max_lines} more")
        else:
            print("- None")
        print()
        if name in {"errors", "emergency", "undefined_citations", "undefined_references", "missing_files"} and items:
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
