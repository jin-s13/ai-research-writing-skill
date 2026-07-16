#!/usr/bin/env python3
"""Run a strict static camera-ready readiness audit for a LaTeX paper."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from paper_contract import ContractError, collect_tex_text, resolve_graphics


TODO_RE = re.compile(r"\b(TODO|FIXME|TBD|PLACEHOLDER|CITATION\s+NEEDED|answerTODO|justificationTODO)\b", re.I)


def has_section(text: str, name: str) -> bool:
    return re.search(rf"\\section\*?\{{[^}}]*{re.escape(name)}[^}}]*\}}", text, re.I) is not None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("main_tex", type=Path)
    parser.add_argument("--checklist", type=Path, help="Explicit venue checklist file")
    parser.add_argument("--llm-disclosure", type=Path, help="Explicit LLM disclosure file when required")
    args = parser.parse_args()

    try:
        text = collect_tex_text(args.main_tex)
        resolve_graphics(args.main_tex)
    except ContractError as exc:
        print(f"Camera-ready check failed: {exc}", file=sys.stderr)
        return 2

    root = args.main_tex.parent
    checklist_ok = has_section(text, "Checklist") or (args.checklist is not None and args.checklist.is_file())
    disclosure_ok = args.llm_disclosure is None or args.llm_disclosure.is_file()
    checks = [
        ("No unresolved markers", TODO_RE.search(text) is None, "Remove unresolved markers."),
        ("Limitations section present", has_section(text, "Limitations"), "Add a limitations section."),
        ("Bibliography command present", bool(re.search(r"\\bibliography\{|\\printbibliography", text)), "Add an explicit bibliography command."),
        ("Venue checklist artifact present", checklist_ok, "Provide --checklist or an actual Checklist section."),
        ("Non-anonymous author metadata present", bool(re.search(r"\\(?:author|icmlauthor)\{(?!\s*Anonymous)", text, re.I)), "Camera-ready requires final author metadata."),
        ("Acknowledgments section present", has_section(text, "Acknowledg"), "Add acknowledgments or document a venue-specific exception."),
        ("Declared LLM disclosure file resolves", disclosure_ok, "The --llm-disclosure path does not exist."),
    ]

    print(f"# Camera-Ready Static Check: {args.main_tex}")
    print("\n| Check | Status | Note |\n|---|---|---|")
    for name, ok, note in checks:
        print(f"| {name} | {'pass' if ok else 'fail'} | {'' if ok else note} |")
    return 1 if any(not ok for _, ok, _ in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
