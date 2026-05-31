# Task Packet: Paper About AI Research Writing Skill

- Scope: write a complete example paper package about this repository itself.
- Target venue/template: generic article demo.
- Files to read: root `SKILL.md`, `README.md`, `references/`, `scripts/`, `templates/`, plugin metadata, examples.
- Files allowed to edit: `examples/paper-about-ai-research-writing-skill/`.
- Evidence/data inputs: local repository inventory and public related-project URLs.
- Required artifacts: `paper_story.md`, `claim_evidence_map.md`, `citation_verification.md`, `literature/positioning.md`, `paper/main.tex`, paper figures/tables, `paper/references.bib`, `build_check.md`.
- Rejection checks: no acceptance guarantee, no benchmark claim, no unsupported comparison claim.
- Validation commands: `python3 ../../scripts/research_quality_gate.py .`; `python3 ../../scripts/check_citations.py paper/main.tex paper/references.bib`; compile `paper/main.tex`.
- Acceptance criteria: paper compiles and every major claim is supported or caveated.
