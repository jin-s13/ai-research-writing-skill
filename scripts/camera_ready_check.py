#!/usr/bin/env python3
"""Run a static camera-ready readiness audit for a LaTeX paper."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TODO_RE = re.compile(r"\b(TODO|FIXME|TBD|PLACEHOLDER|CITATION\s+NEEDED|answerTODO|justificationTODO)\b", re.I)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]*)\}")
GRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")


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
    path = parent / value
    return path if path.suffix else path.with_suffix(".tex")


def collect_tex(path: Path, seen: set[Path] | None = None) -> str:
    if seen is None:
        seen = set()
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    text = strip_comments(path.read_text(encoding="utf-8"))
    chunks = [text]
    for match in INPUT_RE.finditer(text):
        child = resolve_tex(path.parent, match.group(1))
        if child.exists():
            chunks.append(collect_tex(child, seen))
    return "\n".join(chunks)


def has_section(text: str, name: str) -> bool:
    return re.search(rf"\\section\*?\{{[^}}]*{re.escape(name)}[^}}]*\}}", text, re.I) is not None


def graphics_missing(main_path: Path, text: str) -> list[str]:
    missing: list[str] = []
    suffixes = ["", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg"]
    for match in GRAPHICS_RE.finditer(text):
        raw = match.group(1)
        candidates = [(main_path.parent / (raw + suffix)).resolve() for suffix in suffixes]
        if not any(candidate.exists() for candidate in candidates):
            missing.append(raw)
    return sorted(set(missing))


def status(ok: bool) -> str:
    return "pass" if ok else "check"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("main_tex", type=Path)
    args = parser.parse_args()

    text = collect_tex(args.main_tex)
    root = args.main_tex.parent
    checks: list[tuple[str, bool, str]] = []

    checks.append(("No unresolved TODO markers", TODO_RE.search(text) is None, "Remove TODO/FIXME/PLACEHOLDER markers."))
    checks.append(("Limitations section present", has_section(text, "Limitations"), "Add or verify a limitations section."))
    checks.append(("Bibliography present", bool(re.search(r"\\bibliography\{|\\printbibliography", text)) or any(root.glob("*.bib")), "Check bibliography setup."))
    checks.append(("Checklist file or section present", (root / "checklist.tex").exists() or "checklist" in text.lower(), "Add/verify venue checklist."))
    checks.append(("Likely non-anonymous author block", "Anonymous" not in text and "\\author{" in text, "Camera-ready usually needs final authors."))
    checks.append(("Acknowledgment considered", "acknowledg" in text.lower(), "Add acknowledgments/funding if allowed and needed."))
    checks.append(("Reproducibility mentioned", re.search(r"reproducib|code|data|release", text, re.I) is not None, "Add code/data/reproducibility details."))
    checks.append(("LLM usage considered", re.search(r"large language model|\\bLLM\\b|language models", text, re.I) is not None, "Add LLM disclosure if applicable."))

    missing_graphics = graphics_missing(args.main_tex, text)
    checks.append(("All includegraphics paths resolve", not missing_graphics, "Missing: " + ", ".join(missing_graphics[:10])))

    print(f"# Camera-Ready Static Check: {args.main_tex}")
    print()
    print("| Check | Status | Note |")
    print("|---|---|---|")
    for name, ok, note in checks:
        print(f"| {name} | {status(ok)} | {note if not ok else ''} |")

    return 1 if any(not ok for _, ok, _ in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
