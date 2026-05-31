# Artifact Contract

Use this reference for full-paper tasks or whenever the agent needs to decide which durable files to create. Artifacts should be created in the target paper project, not in the skill library.

For smaller requests, produce only the relevant subset, but still preserve claim-evidence discipline.

## Project and Evidence Artifacts

- `project_inventory.md`: repository structure, notes, results, templates, existing citations, unresolved missing inputs.
- `experiment_inventory.md`: datasets, baselines, metrics, numbers, caveats, reproducibility gaps.
- `claim_evidence_map.md`: major claims mapped to evidence and status.
- `plan/project-overview.md` when a paper repo already uses a `plan/` workspace: target, constraints, language, venue, deadlines, source files, and current stage.
- `plan/progress.md`: current task, artifacts changed, checks run, remaining risks, and capability-use audit.
- `plan/task-packets/<task>.md`: scope, files to read, files allowed to edit, required evidence, required artifacts, rejection checks, and validation commands for medium or full-paper work.

## Story Artifacts

- `paper_story.md`: thesis, gap, method insight, contributions, claims to make, and claims to avoid.
- Task boundary notes when the task is new, niche, or easy to confuse with nearby settings.

## Literature Artifacts

- `literature/paper_inventory.md`: important related papers, metadata, local file path or URL, status, and relevance.
- `literature/related_work_matrix.md`: lines of work, representative papers, gaps, and how the paper relates.
- `literature/positioning.md`: closest works, task differences, contribution boundary, and claims to make or avoid.
- `literature/notes/`: compact notes for close papers and baselines.
- `literature/papers/`: local copies of important papers only when access and licensing permit.

Do not commit copyrighted PDFs or private downloads unless redistribution is allowed and the user explicitly wants them included.
If a paper cannot be downloaded, the inventory must record the official URL and status (`metadata-only` or `needs-access`) instead of silently omitting the missing local copy.

## Draft and Citation Artifacts

- Main LaTeX draft: preserve the venue template; keep anonymous unless final/camera-ready is requested.
- `references.bib`: verified references only, fetched from authoritative BibTeX/metadata sources rather than written from memory.
- `citation_verification.md`: source used to verify each citation and the sentence-level claim it supports.

## Figure and Table Artifacts

- `figures/figure_plan.md`: role, message, entities, relationships, layout, backend, source, and fallback for each figure.
- `figures/figure_specs.yaml` or `figures/figure_specs.md`: machine-checkable role/message/entities/layout/backend specs.
- Generated figure/table assets: image-generated diagrams, deterministic plot PDFs/PNGs, and LaTeX tables that the draft can include directly.
- Figure/table source files: prompts/specs for generated diagrams, deterministic scripts for numerical plots, and editable fallback/overlay files when needed.

## Submission and Review Artifacts

- Checklist, reproducibility, limitations, compute/data/code, and LLM usage notes for the target venue.
- `build_check.md`: compilation attempt, tool availability, and unresolved build blockers.
- `submission_readiness.md`: reviewer-risk status before final submission when the paper is close to complete.
- `reviewer_analysis.md`: author-facing reviewer-style diagnosis with strengths, risks, evidence gaps, and recommended decisions.
- `plan/review/<task>_spec.md`: whether the output matched the requested scope, files, and required artifacts.
- `plan/review/<task>_quality.md`: claim support, logic, citation fit, prose quality, and unresolved weaknesses.

## Minimal Subsets

| Request type | Minimal durable artifacts |
|---|---|
| Story only | `paper_story.md` |
| Abstract/Introduction revision | `claim_evidence_map.md`, revised `.tex` section |
| Related Work | `literature/paper_inventory.md`, `literature/related_work_matrix.md`, `literature/positioning.md`, citation updates |
| Figures | `figures/figure_plan.md`, figure specs, generated assets, source or fallback files |
| Citation repair | `references.bib`, `citation_verification.md` |
| Submission audit | `build_check.md`, `submission_readiness.md`, checklist notes |
| Medium or multi-file task | `plan/task-packets/<task>.md`, `plan/progress.md`, relevant output artifacts |
