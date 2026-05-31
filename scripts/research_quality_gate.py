#!/usr/bin/env python3
"""Run lightweight project-level quality checks for research paper drafts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {".md", ".tex", ".bib", ".txt", ".yaml", ".yml", ".json", ".csv", ".tsv"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "venv", ".venv", "build", "dist"}

PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|FIXME|XXX|PLACEHOLDER|CITATION\s+NEEDED|FILL\s+LATER)\b|"
    r"待回填|待替换|待补充|公式占位|算法占位",
    re.IGNORECASE,
)
PROCESS_RE = re.compile(
    r"write naturally|avoid ai|replace later|user should|this section is a template|"
    r"discussion prompt|figure position|table position|"
    r"写作要求|修改要求|请用户|用户替换|回填模板|讨论提示|图位|表位|实验目的",
    re.IGNORECASE,
)
CITATION_RE = re.compile(
    r"\\cite[tpa]?\{[^}]+\}|\[[A-Za-z0-9_-]+(?:,\s*[A-Za-z0-9_-]+)*\]|"
    r"\([A-Z][^)]*(?:19|20)\d{2}[^)]*\)|（[^）]*(?:19|20)\d{2}[^）]*）"
)
LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)", re.MULTILINE)


def iter_text_files(root: Path):
    root_is_skill_library = (root / "SKILL.md").exists() and (root / "references").exists() and (root / "templates").exists()
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if root_is_skill_library:
            relative_parts = path.relative_to(root).parts
            if relative_parts[:1] in {("templates",), ("references",), ("scripts",)}:
                continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return ""


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def has_any(root: Path, candidates: list[str]) -> bool:
    return any((root / candidate).exists() for candidate in candidates)


def check_required_artifacts(root: Path, submission: bool) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    root_is_skill_library = (root / "SKILL.md").exists() and (root / "references").exists() and (root / "templates").exists()

    if root_is_skill_library and not submission:
        return failures, warnings

    if not has_any(root, ["claim_evidence_map.md", "plan/evidence-map.md", "refs/evidence-map.md"]):
        warnings.append("Missing claim/evidence map: claim_evidence_map.md, plan/evidence-map.md, or refs/evidence-map.md")

    if not has_any(root, ["paper_story.md", "plan/project-overview.md"]):
        warnings.append("Missing story or project overview artifact: paper_story.md or plan/project-overview.md")

    if (root / "plan").exists():
        if not (root / "plan/progress.md").exists():
            failures.append("plan/ exists but plan/progress.md is missing.")
        packet_dir = root / "plan/task-packets"
        if packet_dir.exists() and not any(packet_dir.glob("*.md")):
            warnings.append("plan/task-packets/ exists but contains no task packet markdown files.")

    if submission:
        required = [
            "build_check.md",
            "submission_readiness.md",
            "citation_verification.md",
        ]
        for candidate in required:
            if not (root / candidate).exists():
                failures.append(f"Submission mode requires {candidate}.")

    return failures, warnings


def check_text_files(root: Path, strict: bool) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []

    for path in iter_text_files(root):
        text = read_text(path)
        if not text:
            continue
        name = rel(path, root)
        is_manuscript = path.suffix.lower() in {".tex", ".md"} and (
            "chapter" in path.parts
            or path.name.lower().startswith(("main", "paper", "draft"))
            or path.parent.name in {"sections", "sec", "chapters"}
        )

        for lineno, line in enumerate(text.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                target = failures if strict or is_manuscript else warnings
                target.append(f"{name}:{lineno}: unresolved placeholder-like text: {line.strip()[:140]}")
            if is_manuscript and PROCESS_RE.search(line):
                failures.append(f"{name}:{lineno}: process/user-instruction text appears in manuscript: {line.strip()[:140]}")

        if is_manuscript:
            list_lines = len(LIST_RE.findall(text))
            if list_lines > 12:
                warnings.append(f"{name}: {list_lines} list-like lines; verify the section is prose-led.")

            if path.name.lower().startswith(("intro", "01_intro", "1_intro")):
                citations = len(CITATION_RE.findall(text))
                if citations < 3:
                    warnings.append(f"{name}: Introduction-like file has only {citations} citation marker(s).")

    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path, help="Paper project directory to check")
    parser.add_argument("--submission", action="store_true", help="Require final submission artifacts")
    parser.add_argument("--strict", action="store_true", help="Treat placeholders outside manuscript files as failures")
    args = parser.parse_args()

    root = args.project_path.resolve()
    if not root.exists():
        print(f"Project path does not exist: {root}", file=sys.stderr)
        return 2

    failures, warnings = check_required_artifacts(root, args.submission)
    text_failures, text_warnings = check_text_files(root, args.strict)
    failures.extend(text_failures)
    warnings.extend(text_warnings)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if failures:
        print("Failures:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("Research quality gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
