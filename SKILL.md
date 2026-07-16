---
name: ai-research-writing-skill
description: End-to-end research paper generation, review, and revision for ML/AI/CV/NLP projects from repositories, notes, experiment logs, drafts, and conference templates. Use when building a paper story, mapping claims to evidence, writing or revising sections, producing figures and tables, verifying citations, acting as a skeptical reviewer, running venue or build checks, or preparing a LaTeX/Overleaf/Git submission package.
---

# AI Research Writing Skill

## Mandate

Treat paper writing as claim-evidence engineering, not prose generation.

- Ground claims in repository files, experiment artifacts, notes, or verified citations.
- Never invent citations or numeric results. Mark missing evidence visibly and weaken unsupported claims.
- For full papers, produce concrete LaTeX, BibTeX, figure, table, review, and build artifacts; do not stop at an outline.
- Keep human judgment in the loop for scientific correctness, visual inspection, reviewer risk, and final submission decisions.

## Route the Task

Choose the smallest route that covers the request. Load only the listed references first.

| Route | Load first |
|---|---|
| Full paper or major revision | `references/workflow.md`, `references/artifacts.md` |
| Upstream research-system handoff | `references/research-handoff.md`, `references/artifacts.md` |
| Story, thesis, gap, or contribution | `references/paper-story.md` |
| Section writing or revision | `references/README.md`, then the section-specific reference |
| Figures and tables | `references/figure-workflow.md`, `references/figure-spec.md` |
| Citation search or repair | `references/citation-workflow.md` |
| Reviewer diagnosis | `references/reviewer-guidelines.md`, `references/reviewer-self-review.md` |
| Submission or camera-ready audit | `references/submission-packaging.md`, `references/citation-checklist.md` |
| Deterministic checks or formatting | `scripts/README.md` |

## Execution Contract

For full-paper and submission work:

1. Create `paper_state.json` from the contract in `references/artifacts.md`; declare mode, stage, venue, main TeX, bibliography, required artifacts, blockers, and build record.
2. If `research_handoff.json` exists, run `check_research_handoff.py --require-unblocked` first. Otherwise inventory the repository and experiments before drafting. Create one task packet and update `plan/progress.md` at the start and end.
3. Establish the story, claim boundaries, and literature position before long-form prose.
4. Follow the two-pass drafting order in `references/workflow.md`: write evidence-bearing core sections first, then finalize framing sections.
5. Run the mode-aware quality gate. A terminal stage is invalid when inputs are missing, claims/citations remain unresolved, verification is pending, blockers remain, or build hashes are stale.

Keep process instructions in plan/review files, never in manuscript prose.

## Gates

- **Evidence**: exact numbers must trace to data, logs, tables, notebooks, or scripts. Quantitative papers maintain numeric-evidence v2 selectors and recomputable aggregates.
- **Story**: define thesis, gap, contribution boundary, and claims to avoid before a full draft.
- **Literature**: position close work before writing Related Work.
- **Citation**: scholarly `verified` records require `citation_requests.json` and a fresh `citation_lock.json`; metadata verification and sentence-level support are separate checks.
- **Figures**: generated images may explain concepts but cannot create numeric evidence. For overview, method, framework, pipeline, architecture, and teaser figures, use built-in image generation as the default paper asset; use deterministic plots/tables for results.
- **Review**: resolve high-severity reviewer objections or record them as blockers.
- **Build**: compile the real package with `record_build.py --run` before submission-ready; preserve command, log, tool version, exit code, and hashes.
- **Completion**: do not say "done" until required artifacts and checks pass or explicit blockers are reported.

## Evidence Boundaries

- Treat negative, mixed, missing-seed, or incomplete results as scope constraints, not material to hide.
- Verify that each citation supports the attached sentence, not merely the topic.
- Save important papers locally only when access and redistribution permit; otherwise record stable metadata and access status.
- Generated diagrams communicate a workflow or idea; they are never experimental evidence.

## Finish

Report the concrete artifacts changed, checks run, and remaining scientific risks. Preserve the author's intent, but not unsupported wording.
