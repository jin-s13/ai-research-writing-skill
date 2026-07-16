#!/usr/bin/env python3
"""Exercise the real auto-research exporter against this skill's validator."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL = Path(__file__).resolve().parents[3]


def write_stage(root: Path, number: int, name: str, content: str) -> None:
    path = root / f"stage-{number:02d}" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--auto-research", type=Path, required=True)
    args = parser.parse_args()
    auto = args.auto_research.resolve()
    if not (auto / "researchclaw/writing_handoff.py").is_file():
        print(f"auto-research writing exporter not found: {auto}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as directory:
        run_dir = Path(directory) / "run"
        run_dir.mkdir()
        write_stage(run_dir, 1, "goal.md", "# Goal\nDoes method A improve accuracy over baseline B?")
        write_stage(run_dir, 9, "exp_plan.yaml", "metric: accuracy\nseeds: [1, 2]\n")
        write_stage(run_dir, 14, "analysis.md", "# Analysis\nThe result is positive but narrowly scoped.")
        write_stage(run_dir, 15, "decision.md", "# Decision\nPROCEED with bounded claims.")
        (run_dir / "experiment_summary_best.json").write_text(
            json.dumps({"conditions": {"method_a": {"accuracy": 0.91, "seeds": [0.90, 0.92]}}}),
            encoding="utf-8",
        )
        interpreter = auto / ".venv/bin/python"
        if not interpreter.is_file():
            interpreter = Path(sys.executable)
        command = [
            str(interpreter), "-m", "researchclaw", "writing-handoff",
            "--run-dir", str(run_dir), "--target-venue", "ICML",
            "--paper-type", "empirical ML paper", "--require-unblocked",
            "--writing-skill-path", str(SKILL),
        ]
        completed = subprocess.run(command, cwd=auto, text=True, capture_output=True, check=False)
        handoff = json.loads((run_dir / "research_handoff.json").read_text(encoding="utf-8")) \
            if (run_dir / "research_handoff.json").is_file() else None
        numeric = json.loads((run_dir / "writing-handoff/numeric_evidence.json").read_text(encoding="utf-8")) \
            if (run_dir / "writing-handoff/numeric_evidence.json").is_file() else None
        stdout_lines = [
            line for line in completed.stdout.strip().splitlines()
            if not line.startswith("Writing handoff:")
        ]
        result = {
            "schema_version": "ai-research-writing/cross-project-eval-v1",
            "auto_research_exporter": "researchclaw writing-handoff",
            "skill_validator": "scripts/check_research_handoff.py --require-unblocked",
            "status": "pass" if completed.returncode == 0 else "fail",
            "exit_code": completed.returncode,
            "handoff_schema": handoff.get("schema_version") if handoff else None,
            "numeric_schema": numeric.get("schema_version") if numeric else None,
            "numeric_entries": len(numeric.get("entries", [])) if numeric else 0,
            "stdout_tail": stdout_lines[-8:],
            "stderr_tail": completed.stderr.strip().splitlines()[-8:],
        }
        output = Path(__file__).with_name("auto_research_handoff_results.json")
        output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
