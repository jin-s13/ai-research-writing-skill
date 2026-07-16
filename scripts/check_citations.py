#!/usr/bin/env python3
"""Check LaTeX citation keys and fail on incomplete input graphs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from paper_contract import ContractError, collect_bib_keys, collect_citation_keys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path, help="Main LaTeX file")
    parser.add_argument("bib", type=Path, help="BibTeX file")
    args = parser.parse_args()

    try:
        cites = collect_citation_keys(args.tex)
        bib_key_list = collect_bib_keys(args.bib)
    except ContractError as exc:
        print(f"Citation check failed: {exc}", file=sys.stderr)
        return 2

    bib_keys = set(bib_key_list)
    duplicates = sorted({key for key in bib_key_list if bib_key_list.count(key) > 1})
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
    if not missing and not duplicates:
        print("Citation key check passed.")
    if unused:
        print(f"Unused bib entries: {len(unused)}")
    return 1 if missing or duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
