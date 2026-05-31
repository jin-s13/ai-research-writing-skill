# Repository Inventory

Inventory generated for the example paper about `ai-research-writing-skill`.

## Core Skill Files

- `SKILL.md`: root skill contract, operating modes, gates, evidence policy, task-state audit.
- `references/README.md`: reference loading map.
- `references/workflow.md`: full-paper workflow.
- `references/artifacts.md`: durable artifact contract.
- `references/task-management.md`: task packet and completion audit workflow.

## Example Paper Template

This example paper uses the repository's bundled ICML 2026 template files copied into `paper/`:

- `icml2026.sty`
- `icml2026.bst`
- `fancyhdr.sty`

The example includes two image-generated figures used in the paper:

- `paper/figures/teaser_imagegen.png`
- `paper/figures/overview_imagegen.png`

It also keeps a deterministic TikZ fallback:

- `paper/figures/method_overview.tex`

## Deterministic Helper Scripts

The repository includes 8 top-level helper script/reference files under `scripts/`:

- `camera_ready_check.py`
- `check_citations.py`
- `check_todos.py`
- `extract_claims.py`
- `make_latex_table.py`
- `parse_build_log.py`
- `research_quality_gate.py`
- `README.md`

## Venue Templates

The repository includes bundled LaTeX template directories for 9 venue families:

- AAAI 2026
- ACL
- COLM 2025
- CVPR 2026
- ECCV 2026
- ICCV 2025
- ICLR 2026
- ICML 2026
- NeurIPS 2025

## Portable Skill Entrypoint

- `SKILL.md`: the canonical agent entrypoint.
- `README.md`: installation guidance that asks agents to install or load the repository using the root `SKILL.md`.

## Reference Library

The repository includes 21 top-level reference files under `references/`, covering story design, citations, figures, reviewer checks, venues, submission packaging, and task management.
