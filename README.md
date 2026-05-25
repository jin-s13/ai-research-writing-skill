# Paper Writing Suite

**Paper Writing Suite** is an end-to-end Codex skill for turning a research repository, experiment notes, and a conference template into a structured, evidence-backed paper draft.

It is designed for ML, AI, CAD, robotics, systems, and related research projects where paper writing is not just prose generation, but a full workflow:

```text
repo / notes / results
-> paper story
-> claim-evidence map
-> LaTeX draft
-> figures and tables
-> verified citations
-> venue checklist
-> build check
-> Overleaf / Git submission
```

The core philosophy is simple:

> Treat paper writing as a claim-evidence-engineering workflow, not prose generation.

Every major claim should be backed by code, experiments, notes, or verified citations. If evidence is missing, the claim should be weakened, marked as a gap, or removed.

## Why This Skill Exists

Research-paper writing often fails in the spaces between otherwise good tools:

- A writing assistant may produce fluent prose but lose contact with actual experiments.
- A literature workflow may gather citations but not shape a coherent paper story.
- A plotting workflow may generate nice figures but not connect them to reviewer-facing claims.
- A LaTeX template may compile, but the submission may still lack citation verification, limitations, checklist answers, or reproducibility notes.

Paper Writing Suite connects these pieces into one controlled workflow.

## Relationship to Existing Skills

Paper Writing Suite was created by consolidating and refining three complementary skill patterns:

| Source skill | Strength | Limitation when used alone | How Paper Writing Suite integrates it |
|---|---|---|---|
| `ml-paper-writing` | Strong conference-oriented workflow: repo mining, paper story, citation discipline, checklist awareness | Broad controller, but output artifacts and intermediate gates can vary between runs | Becomes the top-level submission workflow: intake, story, verified citations, checklist, build, and packaging |
| `research-paper-writing` | Strong section-level writing quality: Abstract/Introduction structure, paragraph roles, reverse outlines, claim-evidence alignment | Excellent for polishing sections, but not a full LaTeX/repo/submission pipeline | Becomes the section-quality layer: claim-evidence maps, paragraph roles, reviewer-facing revisions |
| `academic-plotting` | Strong figure thinking: role, entities, relationships, layout, numerical plotting, architecture diagrams | Figure backend can be too tool-specific, and image generation can distort labels or numbers | Becomes the figure-quality layer: deterministic plots for numbers, editable diagram fallbacks, generated polish only when safe |

The result is not a loose bundle of three skills. It is a single paper-production state machine with explicit artifacts, gates, and failure modes.

## Key Advantages

### 1. End-to-End Paper Engineering

Paper Writing Suite covers the whole path from research artifacts to submission-ready files:

- repository and experiment inventory
- paper story construction
- claim-evidence mapping
- section drafting and revision
- related work organization
- figure planning and generation
- citation verification
- venue checklist completion
- build checks
- Git / Overleaf packaging

### 2. Claim-Evidence Discipline

The skill requires a claim-evidence map for major claims, especially in the Abstract and Introduction.

This prevents common paper-writing failures:

- overclaiming beyond experiments
- hiding negative metrics
- citing papers for claims they do not support
- producing polished but unsupported prose

### 3. Stable Intermediate Artifacts

For full paper-generation tasks, the skill encourages consistent artifacts:

```text
paper_story.md
claim_evidence_map.md
references.bib
citation_verification.md
figures/figure_plan.md
build_check.md
```

These files make the writing process auditable and easy to resume.

### 4. Venue-Aware Submission Workflow

The skill handles target-venue details such as:

- NeurIPS / ICML / ICLR-style checklist expectations
- anonymity mode
- page-limit awareness
- reproducibility and compute reporting
- broader impacts and limitations
- citation and license audit reminders

If the user request conflicts with the template, the skill is designed to notice and explain the mismatch.

### 5. Safer Figure Generation

Paper Writing Suite separates figure generation by risk:

- **Exact numerical results**: deterministic scripts only.
- **Architecture / workflow diagrams**: editable TikZ/SVG fallback preferred.
- **Generated polished diagrams**: allowed, but only with prompt/source files and fallback.
- **Text-heavy generated images**: must be visually inspected before use.

This avoids the common failure mode where an image model produces beautiful but incorrect labels or numbers.

### 6. Citation Verification by Default

The skill explicitly forbids hallucinated BibTeX entries.

Preferred sources:

- arXiv BibTeX
- DOI / Crossref
- Semantic Scholar
- official publisher pages
- official software documentation

Every reference should be recorded in `citation_verification.md`.

## Skill Structure

```text
paper-writing-suite/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── abstract-introduction.md
│   ├── citation-checklist.md
│   ├── citation-workflow.md
│   ├── example-bank.md
│   ├── figure-spec.md
│   ├── figure-workflow.md
│   ├── paper-story.md
│   ├── reviewer-self-review.md
│   ├── reviewer-guidelines.md
│   ├── section-writing.md
│   ├── style-presets.md
│   ├── submission-packaging.md
│   ├── venue-templates.md
│   └── venue-profiles.md
└── scripts/
    ├── camera_ready_check.py
    ├── check_citations.py
    ├── check_todos.py
    ├── extract_claims.py
    ├── make_latex_table.py
    └── parse_build_log.py
```

## What Each Reference Does

### `references/paper-story.md`

Defines the paper narrative workflow:

- thesis
- gap
- technical challenge
- method insight
- contributions
- evidence
- claims to make
- claims to avoid
- reviewer risks

### `references/section-writing.md`

Defines section-level writing rules for:

- Abstract
- Introduction
- Related Work
- Method
- Experiments
- Limitations
- Conclusion

It emphasizes paragraph roles, reverse outlines, and claim-evidence alignment.

### `references/abstract-introduction.md`

Defines high-stakes Abstract/Introduction templates, backward-first introduction logic, technical-challenge patterns, pipeline patterns, and reverse-outline checks.

### `references/figure-workflow.md`

Defines the figure design process:

- figure role
- message
- entities
- relationships
- layout
- backend
- fallback

It also gives rules for deterministic plotting versus image generation.

### `references/figure-spec.md`

Defines the required role/message/entities/relationships/layout/backend/source/fallback schema for every figure.

### `references/style-presets.md`

Defines deterministic data-chart styling, venue figure sizes, palettes, diagram styles, and arrow conventions.

### `references/citation-checklist.md`

Defines:

- citation verification rules
- checklist rules
- build-check expectations
- pre-commit checks

### `references/citation-workflow.md`

Defines the programmatic citation workflow: search, verify, retrieve BibTeX, validate claim support, and record verification.

### `references/venue-profiles.md`

Defines venue-aware expectations for NeurIPS, ICML, ICLR, ACL/NLP, systems, and CAD/robotics/graphics-adjacent papers.

### `references/venue-templates.md`

Defines reusable limitations, reproducibility, compute, ethics, LLM usage, checklist, and camera-ready text templates.

### `references/reviewer-guidelines.md`

Defines how reviewers judge soundness, clarity, significance, originality, reproducibility, and venue-specific concerns.

### `references/reviewer-self-review.md`

Defines the adversarial reviewer audit: contribution, clarity, experimental strength, evaluation completeness, and method soundness.

### `references/submission-packaging.md`

Defines build checks, static checks, artifact hygiene, Overleaf/Git workflow, and camera-ready checks.

### `scripts/check_citations.py`

Checks whether citation keys used in a LaTeX file exist in a BibTeX file.

Example:

```bash
python scripts/check_citations.py paper.tex references.bib
```

### `scripts/check_todos.py`

Checks for unresolved TODO-like markers before submission.

Example:

```bash
python scripts/check_todos.py paper.tex checklist.tex references.bib figures
```

### Automation scripts

```bash
python scripts/extract_claims.py main.tex > claim_evidence_map.md
python scripts/make_latex_table.py results.csv --caption "Main results." --label tab:main --precision 3
python scripts/parse_build_log.py main.log
python scripts/camera_ready_check.py main.tex
```

## Example Usage

Ask Codex:

```text
Use paper-writing-suite to turn this repo and experiment folder into a NeurIPS paper draft.
```

Or:

```text
Use paper-writing-suite to revise the Abstract and Introduction. Make sure every claim is supported by the experiments.
```

Or:

```text
Use paper-writing-suite to design Figure 1 and the main experiment figure. Use deterministic plotting for numbers and keep editable fallbacks for diagrams.
```

## Recommended Workflow

1. Inspect the project.
2. Create `paper_story.md`.
3. Create or update the claim-evidence map.
4. Draft Abstract and Introduction.
5. Draft Related Work and Method.
6. Build Figure 1 and main result figures.
7. Draft Experiments, Limitations, and Conclusion.
8. Verify citations.
9. Complete checklist and build check.
10. Commit and push to Overleaf or the target paper repo.

## Design Principles

- **Evidence first**: prose follows evidence, not the other way around.
- **No hallucinated citations**: every BibTeX entry must be verified.
- **Figures are arguments**: every figure must support a paper claim.
- **Generated images need fallbacks**: editable diagrams and deterministic plots remain the source of truth.
- **Checklists are not paperwork**: they expose missing reproducibility, ethics, data, and compute details.
- **A good draft is auditable**: future collaborators should be able to see where claims, numbers, citations, and figures came from.

## Current Status

Paper Writing Suite is intended as a practical research-writing assistant for Codex-style agents. It is especially useful when a paper is being written from a live codebase rather than from a clean, finished manuscript.

The skill has been validated with:

- skill structure validation
- citation-key checking on a NeurIPS-style LaTeX project
- an end-to-end paper draft workflow involving story construction, section drafting, figure planning, citation verification, checklist completion, and Overleaf Git submission

## License

Add your preferred open-source license before publishing.
