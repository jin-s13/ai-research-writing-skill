# Full Paper Workflow

Use this reference for full-paper generation, major revisions, or submission preparation. Move through the states below; do not silently skip a gate. If evidence is unavailable, record the limitation and continue with a weaker claim.

For the expected artifacts, load `references/artifacts.md` alongside this workflow.

## State Machine

### 1. Venue and Template Detection

- Identify target venue, anonymity mode, page limit, checklist, camera-ready constraints, and main `.tex` file.
- If target venue and template conflict, state the conflict and follow the user's stated target unless they override it.
- Load `references/venue-profiles.md`.
- Use `templates/README.md` when choosing or explaining a bundled LaTeX template.

### 2. Repo and Artifact Inventory

- Inspect repo structure, README/docs, notes, results, templates, existing `.bib`, and prior drafts.
- Create `project_inventory.md` and `experiment_inventory.md` for full-paper tasks.
- Prefer repository evidence over memory.
- Note missing artifacts instead of guessing.

### 3. Paper Story

- Load `references/paper-story.md`.
- Load `references/literature-review.md` when the literature gap or related work positioning is uncertain.
- Write the one-sentence thesis.
- Identify the exact literature gap and the technical reason it exists.
- Separate strong claims, careful claims, and claims to avoid.
- Produce `paper_story.md` before drafting long prose.
- For new or niche tasks, explicitly define the task boundary and input/output.

### 4. Claim-Evidence Map

- Map each Abstract/Introduction claim to repo evidence, experiment numbers, or verified citations.
- For existing drafts, use `scripts/extract_claims.py` to bootstrap the map, then manually refine evidence status.
- Remove or weaken unsupported claims.
- Load `references/abstract-introduction.md` for Abstract/Introduction work.
- Load `references/section-writing.md` when writing or revising other sections.
- Treat negative or mixed results as scope control, not as material to hide.

### 5. Draft Sections

- Draft in this order: Abstract, Introduction, Related Work, Method, Experiments, Limitations, Conclusion.
- For Abstract/Introduction, include paragraph roles and a reverse outline.
- For Related Work, first create or update the literature corpus, related work matrix, and positioning analysis in `literature/`.
- Keep terminology stable across all sections.
- Do not write the paper as "naive baseline + patch" unless the paper is explicitly an ablation note. Build curiosity around a real technical challenge.
- Use `references/reviewer-self-review.md` for major revisions and before submission.

### 6. Figures and Tables

- Load `references/figure-workflow.md`.
- Load `references/figure-spec.md` when creating or reviewing a figure plan.
- For every figure, first classify it as `evidence-result` or `concept-method`, then write its role, message, entities, relationships, layout, backend, source, and backup/fallback.
- For `evidence-result` figures, use deterministic plotting or LaTeX tables; never use image generation for exact numbers, axes, metric values, tables, or benchmark claims.
- After the plan is written, generate the actual figure files. Do not stop with `figures/figure_plan.md` unless the needed tool, data, or access is unavailable and recorded as a blocker.
- For `concept-method` figures, use built-in image generation as the visual/inspiration version, and keep TikZ/SVG as the exact-text version: editable backup, simplified schematic, or exact-label overlay whenever feasible.
- Do not bind generated figures to a specific external image API or model unless the user explicitly requests it.
- Use `scripts/make_latex_table.py` for CSV-to-LaTeX tables when exact table formatting is needed.
- Inspect generated diagrams. If text is distorted or labels are wrong, regenerate with shorter text or add deterministic labels through the fallback/overlay.
- Update the LaTeX draft to reference generated figure/table assets when the paper section depends on them.
- Captions must state the takeaway, not merely describe the visual elements.

### 7. Citation Verification

- Load `references/citation-workflow.md` for finding and adding citations.
- Load `references/citation-checklist.md` for final citation/checklist audit.
- Fetch citation metadata programmatically; do not write BibTeX from memory.
- Create or update `references.bib` with retrieved BibTeX entries. Do not stop at candidate URLs or a citation plan when an authoritative BibTeX source is available.
- Download or save official accessible copies of important related papers in `literature/papers/` when access and licensing permit; otherwise record `metadata-only` or `needs-access` in `literature/paper_inventory.md`.
- Record verification sources in `citation_verification.md`.
- Verify that the cited paper supports the sentence-level claim, not merely the broad topic.

### 8. Reviewer Self-Review

- Load `references/reviewer-self-review.md`.
- Review the paper as a skeptical reviewer across contribution, clarity, experiments, evaluation completeness, and method soundness.
- Produce an author-facing reviewer analysis, not only automatic edits; explain strengths, weaknesses, rejection risks, and trade-offs.
- Convert high-risk issues into concrete edits, experiments, or explicit limitations.

### 9. Venue Checklist and Build

- Use the checklist that matches the actual target/template. If user request and template conflict, state the conflict and choose the target venue unless the user overrides.
- Load `references/venue-templates.md` when drafting venue-specific sections or checklist text.
- Fill checklist answers honestly; `No` is better than pretending missing reproducibility details exist.
- Run LaTeX build if tools are available; otherwise record missing tools in `build_check.md`.
- Use `scripts/parse_build_log.py` when a LaTeX log exists.
- Use `scripts/check_citations.py` when a `.tex`/`.bib` pair exists.
- Use `scripts/check_todos.py` before submission packaging.

### 10. Submission Packaging

- Load `references/submission-packaging.md`.
- Use `scripts/camera_ready_check.py` for final/camera-ready audits.
- Before commit/push, check `git status`, staged files, generated binary sizes, and whether the worktree is clean after commit.
- For Overleaf-linked repos, push only after the user asks or clearly authorizes it.
