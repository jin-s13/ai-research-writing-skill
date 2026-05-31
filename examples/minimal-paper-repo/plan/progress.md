# Progress

## Current Task

- Stage: demo fixture.
- Task: provide a minimal repository that shows expected AI Research Writing Skill outputs.
- Input files: `notes.md`, `results/main_results.csv`, `main.tex`.
- Output files: `paper_story.md`, `claim_evidence_map.md`, `figures/figure_plan.md`, `build_check.md`.
- Verification planned: `python3 ../../scripts/research_quality_gate.py .`

### Capability-use audit

- Required references/scripts: root `SKILL.md`, `references/task-management.md`, `scripts/research_quality_gate.py`.
- Inputs consumed: notes, result CSV, draft LaTeX.
- Inputs not used and why: no external citations; demo intentionally avoids literature claims.
- Artifacts produced: story, claim map, positioning note, figure plan, build note.
- Verification run: not recorded in fixture.
- Remaining risk: demo values are illustrative and not scientific evidence.
