# Repository Inventory

Inventory generated for the example paper about `ai-research-writing-skill`.

## Core Skill Files

- `SKILL.md`: root skill contract, operating modes, gates, evidence policy, task-state audit.
- `references/README.md`: reference loading map.
- `references/workflow.md`: full-paper workflow.
- `references/artifacts.md`: durable artifact contract.
- `references/task-management.md`: task packet and completion audit workflow.

## Example Paper Template

This example paper was built with the official ICML 2026 archive recorded in `paper_state.json`. The archive URL and SHA-256 are part of the build contract; template files are fetched when rebuilding rather than redistributed by this repository.

The example includes two image-generated figures used in the paper:

- `paper/figures/teaser_imagegen.png`
- `paper/figures/overview_imagegen.png`

It also keeps a deterministic TikZ fallback:

- `paper/figures/method_overview.tex`

## Deterministic Helper Scripts

The repository includes 10 Python helper scripts under `scripts/`, including:

- `camera_ready_check.py`
- `check_citations.py`
- `check_todos.py`
- `extract_claims.py`
- `make_latex_table.py`
- `parse_build_log.py`
- `research_quality_gate.py`
- `record_build.py`
- `fetch_template.py`
- `paper_contract.py`

## Venue Templates

The audited manifest records official source and license status for 9 venue families:

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

The repository includes 21 top-level reference and schema files under `references/`, covering story design, citations, figures, reviewer checks, venues, submission packaging, task management, and the machine state contract.
