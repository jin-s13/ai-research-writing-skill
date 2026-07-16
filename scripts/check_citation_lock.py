#!/usr/bin/env python3
"""Validate citation requests and an existing citation lock without network access."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from citation_lock import validate_lock
from paper_contract import ContractError, load_json_object


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--main")
    parser.add_argument("--max-age-days", type=int, default=180)
    args = parser.parse_args()
    root = args.project_path.resolve()
    try:
        if args.main:
            tex = root / args.main
        else:
            state = load_json_object(root / "paper_state.json")
            main_tex = state.get("main_tex")
            if not isinstance(main_tex, str) or not main_tex:
                raise ContractError("paper_state.json main_tex must be a non-empty path")
            tex = root / main_tex
        failures = validate_lock(
            root, tex, root / "citation_requests.json", root / "citation_lock.json",
            max_age_days=args.max_age_days,
        )
    except ContractError as exc:
        print(f"Citation lock check failed: {exc}", file=sys.stderr)
        return 2
    if failures:
        print("Citation lock failures:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("Citation lock check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
