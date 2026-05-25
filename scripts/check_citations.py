#!/usr/bin/env python3
"""Check that LaTeX citation keys exist in a BibTeX file.

The checker follows simple ``\\input`` and ``\\include`` links from the main
TeX file so citations in section files are included in the audit.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CITE_RE = re.compile(
    r"\\(?:"
    r"cite|citep|citet|citealp|citealt|citeauthor|citeyear|"
    r"parencite|textcite|autocite|footcite|supercite|nocite"
    r")\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}"
)
BIB_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]*)\}")


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


def resolve_tex_path(parent: Path, value: str) -> Path:
    path = (parent / value).expanduser()
    if path.suffix:
        return path
    return path.with_suffix(".tex")


def collect_tex_text(tex_path: Path, seen: set[Path] | None = None) -> str:
    if seen is None:
        seen = set()
    tex_path = tex_path.resolve()
    if tex_path in seen:
        return ""
    seen.add(tex_path)
    text = tex_path.read_text(encoding="utf-8")
    text = strip_comments(text)
    chunks = [text]
    for match in INPUT_RE.finditer(text):
        child = resolve_tex_path(tex_path.parent, match.group(1))
        if child.exists():
            chunks.append(collect_tex_text(child, seen))
    return "\n".join(chunks)


def collect_cites(tex_path: Path) -> set[str]:
    text = collect_tex_text(tex_path)
    keys: set[str] = set()
    for match in CITE_RE.finditer(text):
        for key in match.group(1).split(","):
            key = key.strip()
            if key and key != "*":
                keys.add(key)
    return keys


def collect_bib_keys(bib_path: Path) -> set[str]:
    text = bib_path.read_text(encoding="utf-8")
    return {m.group(1).strip() for m in BIB_RE.finditer(text)}


def collect_duplicate_bib_keys(bib_path: Path) -> list[str]:
    text = bib_path.read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    for match in BIB_RE.finditer(text):
        key = match.group(1).strip()
        counts[key] = counts.get(key, 0) + 1
    return sorted(key for key, count in counts.items() if count > 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path, help="Main LaTeX file")
    parser.add_argument("bib", type=Path, help="BibTeX file")
    args = parser.parse_args()

    cites = collect_cites(args.tex)
    bib_keys = collect_bib_keys(args.bib)
    duplicates = collect_duplicate_bib_keys(args.bib)
    missing = sorted(cites - bib_keys)
    unused = sorted(bib_keys - cites)

    if duplicates:
        print("Duplicate bib entries:")
        for key in duplicates:
            print(f"  {key}")

    if missing:
        print("Missing citation keys:")
        for key in missing:
            print(f"  {key}")
    else:
        print("No missing citation keys.")

    if unused:
        print(f"Unused bib entries: {len(unused)}")

    return 1 if missing or duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
