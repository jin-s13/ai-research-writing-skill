#!/usr/bin/env python3
"""Run the reproducible contract evaluation used by the example paper."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


EXAMPLE = Path(__file__).resolve().parents[1]
REPO = EXAMPLE.parents[1]


CASES = [
    (
        "Failure-path regression suite",
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
    ),
    (
        "Skill package contract",
        [sys.executable, "scripts/research_quality_gate.py", ".", "--mode", "skill"],
    ),
    (
        "Citation-key integrity",
        [
            sys.executable,
            "scripts/check_citations.py",
            "examples/paper-about-ai-research-writing-skill/paper/main.tex",
            "examples/paper-about-ai-research-writing-skill/paper/references.bib",
        ],
    ),
    (
        "Unresolved-marker scan",
        [
            sys.executable,
            "scripts/check_todos.py",
            "examples/paper-about-ai-research-writing-skill/paper/main.tex",
            "examples/paper-about-ai-research-writing-skill/paper/references.bib",
            "examples/paper-about-ai-research-writing-skill/paper/tables",
            "examples/paper-about-ai-research-writing-skill/paper/figures",
        ],
    ),
]


def write_if_changed(path: Path, content: str) -> None:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def latex_escape(value: str) -> str:
    replacements = {"&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#"}
    return "".join(replacements.get(char, char) for char in value)


def main() -> int:
    table_path = EXAMPLE / "paper/tables/contract_evaluation.tex"
    results: list[dict[str, object]] = []
    for name, command in CASES:
        completed = subprocess.run(command, cwd=REPO, text=True, capture_output=True, check=False)
        results.append(
            {
                "name": name,
                "status": "pass" if completed.returncode == 0 else "fail",
                "exit_code": completed.returncode,
                "command": command,
                "stdout_tail": completed.stdout.strip().splitlines()[-5:],
                "stderr_tail": completed.stderr.strip().splitlines()[-5:],
            }
        )

    output = {
        "schema_version": "ai-research-writing/contract-eval-v1",
        "scope": "mechanical reliability; not paper-quality or acceptance evaluation",
        "cases": results,
        "passed": sum(result["status"] == "pass" for result in results),
        "total": len(results),
    }
    (EXAMPLE / "evaluation/results.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Reproducible contract evaluation. These checks measure mechanical reliability, not scientific writing quality or acceptance probability.}",
        r"\label{tab:contract-evaluation}",
        r"\begin{tabular}{lc}",
        r"\toprule",
        r"Check & Result \\",
        r"\midrule",
    ]
    for result in results:
        lines.append(f"{latex_escape(str(result['name']))} & {str(result['status']).upper()} " + r"\\")
    lines.extend([r"\midrule", f"Total & {output['passed']}/{output['total']} " + r"\\", r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    write_if_changed(table_path, "\n".join(lines) + "\n")

    for result in results:
        print(f"{result['status'].upper()}: {result['name']} (exit {result['exit_code']})")
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
