---
name: paper-writing-suite
description: End-to-end research paper generation and revision for ML/AI/systems papers from repositories, notes, experiments, and conference templates. Use when Codex needs to turn a research project into a publication-ready LaTeX draft, build a paper story, write or revise Abstract/Introduction/Related Work/Method/Experiments, design figures and tables, verify citations, complete NeurIPS/ICML/ICLR-style checklists, run build checks, or prepare an Overleaf/Git submission.
---

# Paper Writing Suite

## Core Mandate

Treat paper writing as a **claim-evidence-engineering workflow**, not prose generation. Every major claim must be backed by code, results, notes, or verified citations. If evidence is missing, weaken the claim or mark the gap explicitly.

Never invent citations. Fetch BibTeX programmatically from arXiv, DOI/Crossref, Semantic Scholar, publisher pages, or official software/documentation sources. If a citation cannot be verified, use an explicit placeholder and tell the user.

When the user asks for a full paper, do not stop at an outline. Produce concrete paper artifacts, then iterate.

## Operating Modes

Choose the smallest mode that satisfies the user request.

- **Full-paper mode**: repo/notes/results/template -> story -> draft -> figures -> citations -> checklist -> build/package.
- **Story mode**: clarify thesis, gap, contributions, claims-to-make, and claims-to-avoid before drafting.
- **Section mode**: revise Abstract/Introduction/Related Work/Method/Experiments with paragraph roles and claim-evidence checks.
- **Figure mode**: design publication figures, choose deterministic or generated backends, and create regeneration sources.
- **Citation mode**: find, verify, and add references without hallucinating BibTeX.
- **Submission mode**: run checklist, build checks, TODO/citation checks, and Git/Overleaf packaging.
- **Automation mode**: extract claims, generate LaTeX tables, parse build logs, or run camera-ready checks with bundled scripts.

If the user asks for multiple named skills that this suite subsumes, apply this suite as the coordinator and load the relevant reference files below.

## Output Contract

For a full paper-writing request, create or update these artifacts when applicable:

- `project_inventory.md`: repo, notes, results, templates, existing citations, unresolved missing inputs.
- `paper_story.md`: thesis, gap, method insight, contributions, claims to make/avoid.
- `claim_evidence_map.md`: major claims mapped to evidence and status.
- `experiment_inventory.md`: datasets, baselines, metrics, numbers, caveats, reproducibility gaps.
- Main LaTeX draft: venue template preserved, anonymous unless final/camera-ready is requested.
- `references.bib`: verified references only.
- `citation_verification.md`: source used to verify each citation.
- `figures/figure_plan.md`: role, message, entities, relationships, layout, backend for each figure.
- `figures/figure_specs.yaml` or `figures/figure_specs.md`: machine-checkable role/message/entities/layout/backend specs.
- Figure/table source files: deterministic scripts for numerical plots; editable fallback for diagrams.
- Checklist/reproducibility/limitations notes for the target venue.
- `build_check.md`: compilation attempt and unresolved build blockers.
- `submission_readiness.md`: reviewer-risk status before final submission when the paper is close to complete.

For smaller requests, produce the relevant subset, but still maintain claim-evidence discipline.

## State Machine

Move through these states. Do not silently skip a gate; if evidence is unavailable, record the limitation and continue with a weaker claim.

1. **Venue and Template Detection**
   - Identify target venue, anonymity mode, page limit, checklist, camera-ready constraints, and main `.tex` file.
   - If target venue and template conflict, state the conflict and follow the user's stated target unless they override it.
   - Load `references/venue-profiles.md`.

2. **Repo and Artifact Inventory**
   - Inspect repo structure, README/docs, notes, results, templates, existing `.bib`, and prior drafts.
   - Create `project_inventory.md` and `experiment_inventory.md` for full-paper tasks.
   - Prefer repository evidence over memory. Note missing artifacts instead of guessing.

3. **Paper Story**
   - Load `references/paper-story.md`.
   - Prefer repository evidence over memory. Note missing artifacts instead of guessing.
   - Write the one-sentence thesis.
   - Identify the exact literature gap and the technical reason it exists.
   - Separate strong claims, careful claims, and claims to avoid.
   - Produce `paper_story.md` before drafting long prose.
   - For new or niche tasks, explicitly define the task boundary and input/output.

4. **Claim-Evidence Map**
   - Map each Abstract/Introduction claim to repo evidence, experiment numbers, or verified citations.
   - For existing drafts, use `scripts/extract_claims.py` to bootstrap the map, then manually refine evidence status.
   - Remove or weaken unsupported claims.
   - Load `references/abstract-introduction.md` for Abstract/Introduction work.
   - Load `references/section-writing.md` when writing or revising other sections.
   - Treat negative or mixed results as scope control, not as material to hide.

5. **Draft Sections**
   - Draft in this order: Abstract, Introduction, Related Work, Method, Experiments, Limitations, Conclusion.
   - For Abstract/Introduction, include paragraph roles and a reverse outline.
   - Keep terminology stable across all sections.
   - Do not write the paper as "naive baseline + patch" unless the paper is explicitly an ablation note. Build curiosity around a real technical challenge.
   - Use `references/reviewer-self-review.md` for major revisions and before submission.

6. **Figures and Tables**
   - Load `references/figure-workflow.md`.
   - Load `references/figure-spec.md` when creating or reviewing a figure plan.
   - For every figure, first write its role, message, entities, relationships, layout, backend, source, and fallback.
   - Use deterministic plotting for numbers. Use image generation only for non-numeric polished diagrams, and keep an editable fallback such as TikZ/SVG.
   - Use `scripts/make_latex_table.py` for CSV-to-LaTeX tables when exact table formatting is needed.
   - Inspect generated diagrams. If text is distorted or labels are wrong, use the editable fallback.
   - Captions must state the takeaway, not merely describe the visual elements.

7. **Citation Verification**
   - Load `references/citation-workflow.md` for finding and adding citations.
   - Load `references/citation-checklist.md` for final citation/checklist audit.
   - Fetch citation metadata programmatically; do not write BibTeX from memory.
   - Record verification sources in `citation_verification.md`.
   - Verify that the cited paper supports the sentence-level claim, not merely the broad topic.

8. **Reviewer Self-Review**
   - Load `references/reviewer-self-review.md`.
   - Review the paper as a skeptical reviewer across contribution, clarity, experiments, evaluation completeness, and method soundness.
   - Convert high-risk issues into concrete edits, experiments, or explicit limitations.

9. **Venue Checklist and Build**
   - Use the checklist that matches the actual target/template. If user request and template conflict, state the conflict and choose the target venue unless the user overrides.
   - Load `references/venue-templates.md` when drafting venue-specific sections or checklist text.
   - Fill checklist answers honestly; `No` is better than pretending missing reproducibility details exist.
   - Run LaTeX build if tools are available; otherwise record missing tools in `build_check.md`.
   - Use `scripts/parse_build_log.py` when a LaTeX log exists.
   - Use `scripts/check_citations.py` when a `.tex`/`.bib` pair exists.
   - Use `scripts/check_todos.py` before submission packaging.

10. **Submission Packaging**
   - Load `references/submission-packaging.md`.
   - Use `scripts/camera_ready_check.py` for final/camera-ready audits.
   - Before commit/push, check `git status`, staged files, generated binary sizes, and whether the worktree is clean after commit.
   - For Overleaf-linked repos, push only after the user asks or clearly authorizes it.

## Evidence Policy

- Repository files and experiment logs outrank memory.
- Exact numbers must come from source tables, logs, notebooks, or plotting scripts.
- If a result has missing seeds, uncertainty, dataset details, or fairness assumptions, mark the caveat in `experiment_inventory.md` and in the relevant section.
- Related work citations must support the specific sentence where they appear.
- Generated diagrams may illustrate a workflow, but they cannot create new scientific evidence.
- If the user wants a stronger claim than the evidence supports, write the strongest defensible version and name the missing evidence.

## Quality Gates

- **Story gate**: no full draft before the thesis, gap, contributions, and claims-to-avoid are explicit.
- **Claim gate**: no unsupported strong claim in Abstract or Introduction.
- **Citation gate**: no unverified BibTeX unless clearly marked as a placeholder.
- **Figure gate**: no generated numeric figure; numbers must come from code or data.
- **Reviewer gate**: no final draft while high-severity reviewer objections remain unaddressed.
- **Checklist gate**: no submission without limitations, reproducibility, compute/data/code status, and LLM usage status when applicable.
- **Build gate**: attempt compilation or record why compilation could not run.
- **Packaging gate**: no commit/push without status, citation, TODO, and artifact-size checks.

## Resource Guide

- `references/paper-story.md`: narrative, contribution, and claim boundaries.
- `references/abstract-introduction.md`: Abstract/Introduction templates, reverse outline, and claim checks.
- `references/section-writing.md`: Abstract/Introduction/section revision rules.
- `references/figure-workflow.md`: figure planning and backend selection.
- `references/figure-spec.md`: required figure role/message/entities/layout/backend schema.
- `references/style-presets.md`: figure style presets and venue dimensions.
- `references/example-bank.md`: reusable abstract, introduction, method, and experiment patterns.
- `references/citation-workflow.md`: programmatic citation search, verification, and BibTeX retrieval.
- `references/citation-checklist.md`: citation and checklist verification rules.
- `references/venue-profiles.md`: NeurIPS/ICML/ICLR/ACL/systems venue requirements and checklist expectations.
- `references/venue-templates.md`: venue-specific section/checklist templates.
- `references/reviewer-guidelines.md`: reviewer scoring dimensions and rebuttal-facing concerns.
- `references/reviewer-self-review.md`: adversarial reviewer-risk audit.
- `references/submission-packaging.md`: build, artifact, Git, and Overleaf submission workflow.
- `scripts/extract_claims.py`: bootstrap claim-evidence maps from Abstract/Introduction.
- `scripts/make_latex_table.py`: generate booktabs LaTeX tables from CSV.
- `scripts/parse_build_log.py`: summarize LaTeX errors, warnings, undefined refs/cites, and box issues.
- `scripts/camera_ready_check.py`: run a static camera-ready readiness audit.
- `scripts/check_citations.py`: detect missing `.bib` keys used in LaTeX citations.
- `scripts/check_todos.py`: detect unresolved TODO/placeholder markers before submission.

## Response Style

- For long tasks, report concrete artifacts changed and checks run.
- For writing tasks, include a compact rationale only when it helps the user revise.
- For review tasks, lead with the most important risks and file/section references.
- Preserve the user's scientific intent, but do not preserve unsupported wording.
