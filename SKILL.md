---
name: paper-writing-suite
description: End-to-end research paper generation and revision for ML/AI/CV/NLP papers from repositories, notes, experiments, and conference templates. Use when turning a research project into a publication-ready LaTeX draft, building a paper story, writing or revising Abstract/Introduction/Related Work/Method/Experiments, designing figures and tables, verifying citations, completing NeurIPS/ICML/ICLR/CVPR/ICCV/ECCV/ACL-style checklists, running build checks, or preparing an Overleaf/Git submission.
---

# Paper Writing Suite

## Core Mandate

Treat paper writing as a **claim-evidence-engineering workflow**, not prose generation.

Every major claim must be backed by code, results, notes, or verified citations. If evidence is missing, weaken the claim or mark the gap explicitly.

Never invent citations. Fetch BibTeX from arXiv, DOI/Crossref, Semantic Scholar, publisher pages, or official software/documentation sources. If a citation cannot be verified, use an explicit placeholder and tell the user.

When the user asks for a full paper, do not stop at an outline. Produce concrete paper artifacts, then iterate.

For full-paper work, do not stop at plans for figures or citations. Generate or fetch the concrete assets whenever tools and access allow: image files for non-numeric diagrams, deterministic plot/table files for results, `references.bib` entries for citations, and local paper copies or metadata records for the literature corpus.

## Operating Modes

Choose the smallest mode that satisfies the user request.

| Mode | Use when | Load first |
|---|---|---|
| Full-paper mode | Turn a repo, notes, results, and template into a draft or submission package | `references/README.md`, `references/workflow.md`, `references/artifacts.md` |
| Story mode | Clarify thesis, gap, contributions, and claims to make or avoid | `references/paper-story.md` |
| Section mode | Write or revise Abstract, Introduction, Related Work, Method, Experiments, Limitations, or Conclusion | `references/README.md`, then the section-specific reference |
| Figure mode | Design publication figures, tables, diagrams, or teaser visuals | `references/figure-workflow.md`, `references/figure-spec.md`, `references/figure-pattern-atlas.md` as needed |
| Citation mode | Find, verify, repair, or add references | `references/citation-workflow.md` |
| Reviewer mode | Diagnose reviewer risks or prepare author-facing self-review | `references/reviewer-guidelines.md`, `references/reviewer-self-review.md` |
| Submission mode | Run checklist, build checks, TODO/citation checks, or Overleaf/Git packaging | `references/submission-packaging.md`, `references/citation-checklist.md` |
| Automation mode | Use bundled scripts for claims, tables, logs, citations, TODOs, or camera-ready checks | `scripts/README.md` |

If the user asks for multiple named skills that this suite subsumes, apply this suite as the coordinator and load the relevant reference files.

## Loading Strategy

Do not load the entire `references/` tree by default.

1. Start with `references/README.md` when the needed reference is unclear.
2. For full-paper tasks, load `references/workflow.md` and `references/artifacts.md`.
3. Load examples only after choosing a writing pattern; prefer one narrow example file over the whole `references/examples/` folder.
4. Keep generated paper artifacts in the user's target paper repo, not in this skill library.

## Non-Negotiable Gates

- **Evidence gate**: repository files, experiment logs, notes, and verified citations outrank memory.
- **Story gate**: no full draft before thesis, gap, contributions, and claims-to-avoid are explicit.
- **Literature gate**: no Related Work draft before close papers, baselines, and major lines of work are inventoried and positioned.
- **Claim gate**: no unsupported strong claim in Abstract or Introduction.
- **Citation gate**: no unverified BibTeX unless clearly marked as a placeholder.
- **Citation asset gate**: every cited work must be added to `references.bib` from an authoritative source, or be recorded as a visible placeholder/blocker. Important related papers should be downloaded or saved locally when access and licensing permit.
- **Figure gate**: no generated numeric figure; numbers must come from code, data, tables, or logs.
- **Figure asset gate**: after writing a figure plan, actually produce the figure assets when the environment provides the needed tools. For method, teaser, framework, pipeline, architecture, and overview diagrams, invoke built-in image generation and save the generated image as the default figure used in the paper. TikZ/SVG precise schematics are optional backup/reference only (exact labels, terminology alignment, or compile fallback)—not a parallel required deliverable. If image generation is unavailable, record the blocker instead of treating the plan as complete.
- **Reviewer gate**: no final draft while high-severity reviewer objections remain unaddressed.
- **Checklist gate**: no submission without limitations, reproducibility, compute/data/code status, and LLM usage status when applicable.
- **Build gate**: attempt compilation or record why compilation could not run.
- **Packaging gate**: no commit/push without status, citation, TODO, and artifact-size checks.

## Evidence Policy

- Exact numbers must come from source tables, logs, notebooks, or plotting scripts.
- If a result has missing seeds, uncertainty, dataset details, or fairness assumptions, mark the caveat in the relevant artifact and paper section.
- Related work citations must come from verified metadata and support the specific sentence where they appear.
- Close or important related papers should be saved locally when permitted and summarized before they are used for contrast or positioning.
- Generated diagrams may illustrate a workflow, but they cannot create new scientific evidence.
- If the user wants a stronger claim than the evidence supports, write the strongest defensible version and name the missing evidence.

## Output Discipline

For full-paper work, follow `references/artifacts.md`. For smaller requests, produce only the relevant subset while preserving claim-evidence discipline.

For long-running tasks, maintain auditable intermediate artifacts such as `paper_story.md`, `claim_evidence_map.md`, `literature/positioning.md`, `citation_verification.md`, `figures/figure_plan.md`, and `build_check.md`.

## Response Style

- For long tasks, report concrete artifacts changed and checks run.
- For writing tasks, include a compact rationale only when it helps the user revise.
- For review tasks, lead with the most important risks and file/section references.
- Preserve the user's scientific intent, but do not preserve unsupported wording.
