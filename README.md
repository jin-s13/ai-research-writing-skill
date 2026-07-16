# AI Research Writing Skill

[中文说明](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: stdlib only](https://img.shields.io/badge/Python-stdlib%20only-blue.svg)](scripts/README.md)
[![Entrypoint](https://img.shields.io/badge/Entrypoint-SKILL.md-purple.svg)](SKILL.md)
[![Template sources](https://img.shields.io/badge/Templates-official%20sources-orange.svg)](templates/README.md)

Turn an ML/AI research repo into an **evidence-backed, build-ready conference paper draft**.

Point your coding agent at code, experiment logs, notes, and a venue template. This skill helps it produce an auditable LaTeX draft and submission package: story, claim-evidence map, verified citations, figures, reviewer-style critique, rebuttal risks, and build notes.

> **Claim-evidence engineering, not prose generation.**  
> Every major claim should trace to code, results, notes, or verified citations.

![AI Research Writing Skill teaser](examples/paper-about-ai-research-writing-skill/paper/figures/teaser_imagegen.png)

---

## End-to-End Demo

```text
Use AI Research Writing Skill to write a complete system paper about this repository itself.
Treat ai-research-writing-skill as the research artifact.
Inspect SKILL.md, references/, scripts/, templates/, examples/, and README.
Create paper_story.md, claim_evidence_map.md, literature positioning, verified citations, ICML-style method figures/tables, and a build-ready ICML LaTeX paper under examples/paper-about-ai-research-writing-skill/paper/.
Do not invent performance numbers. Use repository facts as evidence.
```

The example already includes the expected final paper package, so you can inspect what an end-to-end output looks like:

- **Read the generated ICML-style paper PDF:** [`paper/main.pdf`](examples/paper-about-ai-research-writing-skill/paper/main.pdf)
- `evidence/repository_inventory.md`: repository facts used as evidence.
- `paper_story.md` and `claim_evidence_map.md`: story and claim boundaries.
- `literature/positioning.md` and `citation_verification.md`: related-project positioning.
- `paper/figures/method_overview.tex` and `paper/tables/*.tex`: ICML-style paper assets.
- `paper/main.tex`: complete paper draft about this project.
- `paper/main.pdf`: compiled paper for quickly judging output quality.
- `build_check.md`: compilation command, expected result, and residual risks.
- [`evaluation/auto_research_handoff_results.json`](examples/paper-about-ai-research-writing-skill/evaluation/auto_research_handoff_results.json): real CLI-to-validator compatibility result between auto-research and this skill.

![AI Research Writing Skill method overview](examples/paper-about-ai-research-writing-skill/paper/figures/overview_imagegen.png)

## User Journeys

Use the skill at different stages of a research project. Start with the journey that matches what you already have.

| Journey | You have | Ask the agent to do |
|---|---|---|
| **Brainstorm and plan** | A topic, rough idea, or possible method | Clarify the thesis, research gap, contribution boundary, evidence needed, and next experiment/writing plan. |
| **Repo to full paper** | Ideas, method design, code, notes, experiment logs, partial results, or a venue template | Build `paper_story.md`, `claim_evidence_map.md`, literature positioning, figures, tables, BibTeX, LaTeX draft, and build checks. |
| **Draft review** | A complete or partial paper draft | Act as a skeptical reviewer: write reviewer-style comments, identify rejection risks, and turn major issues into concrete edits. |
| **Targeted revision** | A draft plus known weaknesses, reviewer feedback, or a section to improve | Revise the section or whole paper while preserving claim-evidence boundaries and avoiding unsupported stronger claims. |
| **Figures and tables** | Results, logs, CSVs, method notes, or a rough figure idea | Produce figure/table plans, generated overview or method figures, deterministic result plots/tables, captions, and LaTeX wiring. |
| **Submission readiness** | A near-final paper package | Run citation, marker, build, venue, reviewer-risk, checklist, and packaging checks before submission or Overleaf/Git handoff. |

Copyable prompts:

```text
I only have a rough idea. Use AI Research Writing Skill to brainstorm the paper story, identify the research gap, define claims to make/avoid, and create a concrete plan for evidence, experiments, figures, and writing.
```

```text
I have code, notes, method design, and some experiment logs/results. Use AI Research Writing Skill to generate a complete paper package: paper_story.md, claim_evidence_map.md, literature positioning, verified BibTeX, figures, tables, LaTeX draft, and build_check.md.
```

```text
I have a paper draft. Use AI Research Writing Skill as a skeptical ICML reviewer: write detailed reviewer comments, identify rejection risks, and convert the high-risk issues into concrete revisions.
```

```text
I have a draft and want to revise it. Use AI Research Writing Skill to improve the paper section by section, preserve supported claims, weaken unsupported claims, fix citations, improve figures/tables, and update the LaTeX package.
```

## Why this skill

| Typical AI paper help | AI Research Writing Skill |
|---|---|
| Fluent paragraphs from memory | Claims mapped to repo evidence |
| Citations guessed or invented | BibTeX from arXiv / DOI / Semantic Scholar |
| Figure “plans” that never ship | Generated overview/method figures + deterministic result plots |
| Stops at an outline | Concrete artifacts: `paper_story.md`, `claim_evidence_map.md`, `references.bib`, figure files |
| Generic writing tips | Reviewer-style comments, rejection-risk diagnosis, venue checklists, build & packaging gates |

**Venue profiles and audited template sources:** NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, ACL, AAAI, COLM, and related ML/AI conferences. Templates are fetched from recorded official sources rather than redistributed when licensing is unclear. Always verify [official author instructions](references/venue-templates.md) before submission.

## Before / After

| Before using this skill | After using this skill |
|---|---|
| Scattered notes, logs, and half-written sections | `paper_story.md` and scoped task packets |
| Claims that sound plausible | `claim_evidence_map.md` with evidence status |
| Candidate citations from memory | BibTeX fetched or verified from authoritative metadata |
| Figure ideas in prose | Generated concept figures and deterministic result plots |
| "Looks done" | Reviewer-style critique, build, TODO, citation, and submission checks |

## What you get

End-to-end coverage from idea to camera-ready:

| Stage | Outputs |
|---|---|
| **Story** | Thesis, gap, contributions, claims to avoid |
| **Evidence** | `claim_evidence_map.md` tied to code / logs / tables |
| **Writing** | Abstract, Intro, Related Work, Method, Experiments, Limitations, Conclusion |
| **Literature** | Local corpus, positioning, verified `references.bib` |
| **Figures** | Plan + assets: **generated** overview/method diagrams; **deterministic** plots for numbers |
| **Review** | Reviewer-style comments, rejection-risk diagnosis, self-review, concrete revision plan |
| **Submit** | Venue checklist, LaTeX build check, TODO/citation audit, packaging |

### Quality gates (built in)

The skill enforces checkpoints agents must not skip:

- **Evidence** — numbers from data/logs/scripts, not image models  
- **Story** — no full draft before contributions are explicit  
- **Literature** — positioning before Related Work prose  
- **Citation** — no unverified BibTeX without a visible placeholder  
- **Figures** — concept diagrams via image generation (default); TikZ/SVG only as optional reference  
- **Reviewer** — high-severity objections addressed before “done”  
- **Build** — compile or document why not  

---

## Installation

**Simple rule:** the only canonical entrypoint is the root [`SKILL.md`](SKILL.md).  
The rest of the repository is supporting material loaded as needed: `references/`, deterministic `scripts/`, audited template sources, and an optional end-to-end example.

### Agent-Assisted Install

Ask your agent to install this repository as a local skill:

```text
Install https://github.com/jin-s13/ai-research-writing-skill as a local skill.
Use the repository root SKILL.md as the canonical entrypoint.
If your platform needs a skills directory, copy or symlink the whole repository there.
```

### Manual Install

```bash
git clone https://github.com/jin-s13/ai-research-writing-skill.git
# Then copy or symlink this repository into your agent's local skills directory.
```

You can also use it without installing by opening this repository and asking:

```text
Use the AI Research Writing Skill in this repository.
Follow SKILL.md and load only the relevant references for my task.
```

---

## Repository layout

```text
ai-research-writing-skill/
├── examples/             # Minimal demo paper repo
├── SKILL.md              # Canonical agent entrypoint
├── references/           # Workflow, writing, citations, figures, venues, review
├── scripts/              # Claims, citations, TODOs, build-log, camera-ready checks
├── templates/            # Audited official-source manifest; no vendored author kits
└── README.zh-CN.md
```

**Start here when digging in:**

| File | Purpose |
|---|---|
| [`references/workflow.md`](references/workflow.md) | Full-paper state machine |
| [`references/artifacts.md`](references/artifacts.md) | What to create in *your* paper repo |
| [`references/research-handoff.md`](references/research-handoff.md) | Evidence contract for upstream research systems |
| [`references/figure-workflow.md`](references/figure-workflow.md) | Diagrams vs plots; generation defaults |
| [`references/citation-workflow.md`](references/citation-workflow.md) | Search, verify, BibTeX |
| [`templates/README.md`](templates/README.md) | Audited official sources and pinned template fetches |
| [`examples/paper-about-ai-research-writing-skill/`](examples/paper-about-ai-research-writing-skill/) | End-to-end paper about this project |

---

## Helper scripts

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/verify_citations.py /path/to/paper-project --mailto you@example.org
python3 scripts/check_citation_lock.py /path/to/paper-project
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/check_numeric_evidence.py /path/to/paper-project
python3 scripts/check_research_handoff.py /path/to/handoff-project --require-unblocked
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
python3 scripts/fetch_template.py icml2026 --output /path/to/paper/.venue-template
python3 scripts/record_build.py /path/to/paper-project --run
python3 scripts/research_quality_gate.py /path/to/paper-project
```

More: [`scripts/README.md`](scripts/README.md).

---

## Safety & hygiene

- Conference author kits are fetched from audited official sources and verified by SHA-256 when pinned; confirm current venue rules before submitting.
- Do **not** commit private PDFs, proprietary logs, API keys, or reviewer-confidential material.

---

## Acknowledgements

This project is inspired by and builds on the excellent research-writing and figure-making projects below. It does not try to replace them; it narrows their ideas into one opinionated workflow: **turn an ML/AI research repository into an evidence-backed, build-ready conference paper package**.

| Project | What it is excellent at | How this project is different |
|---|---|---|
| [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | A compact skill package for ML/CV/NLP paper writing, adapted from research-writing notes into reusable agent skills. | Adds a full repo-to-paper production contract: inventories, claim-evidence maps, verified BibTeX, figure assets, build checks, and submission packaging. |
| [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | A broad, multi-platform research-writing assistant for thesis writing, chapter workflows, literature review, LaTeX output, and process tracking. | Specializes in AI conference papers from code, logs, experiments, and venue templates instead of general thesis/chapter writing. |
| [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | A comprehensive AI research and engineering skills library for agents, spanning the broader research lifecycle from idea to paper. | Focuses on one deep vertical: paper-writing execution and submission readiness for an existing ML/AI research repo. |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | Nature/CNS-style academic writing, polishing, reviewer response, data availability, citation, and publication-quality figure workflows. | Targets ML/AI conference workflows and templates such as NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, ACL, AAAI, and COLM. |
| [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | High-quality Python scripts and examples for publication figures in top AI conferences and journals. | Integrates figure planning into a larger paper pipeline: figures are tied to claims, evidence, captions, LaTeX references, and submission checks. |

In short: the related projects provide writing wisdom, broad skill ecosystems, Nature-style publication craft, or figure-making expertise. This project packages those inspirations into a **claim-evidence-engineering workflow for AI paper agents working inside real research repositories**.

## License

MIT License.
