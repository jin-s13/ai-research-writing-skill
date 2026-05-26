# Paper Writing Suite

[中文说明](README.zh-CN.md)

**Turn a research repo into a submission-ready paper — with evidence, not hallucination.**

Paper Writing Suite is an agent skill for ML / AI / CV / NLP researchers. Point your coding agent at code, experiment logs, notes, and a venue template; it helps you produce an **auditable, evidence-backed** LaTeX draft and submission package — not a polished fiction.

> **Claim-evidence engineering, not prose generation.**  
> Every major claim should trace to code, results, notes, or verified citations.

---

## Why this skill

| Typical AI paper help | Paper Writing Suite |
|---|---|
| Fluent paragraphs from memory | Claims mapped to repo evidence |
| Citations guessed or invented | BibTeX from arXiv / DOI / Semantic Scholar |
| Figure “plans” that never ship | Generated overview/method figures + deterministic result plots |
| Stops at an outline | Concrete artifacts: `paper_story.md`, `claim_evidence_map.md`, `references.bib`, figure files |
| Generic writing tips | Venue checklists, reviewer self-review, build & packaging gates |

**Supported venues (templates & checklists):** NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, ACL, AAAI, COLM, and related ML/AI conferences. Always verify [official author instructions](references/venue-templates.md) before submission.

---

## Quick start

**1. Install** (symlink into your agent’s skills directory):

```bash
git clone https://gitlab.tetras.ai/jinsheng/paper-writing-suite.git
ln -s "$(pwd)/paper-writing-suite" ~/.cursor/skills/paper-writing-suite   # Cursor global
```

See [Installation](#installation) for Codex, Claude Code, Gemini, and project-level paths.

**2. Open your paper repo** in the agent and run:

```text
Use paper-writing-suite to inspect this repo and create paper_story.md and claim_evidence_map.md.
```

**3. Iterate by section** — for example:

```text
Use paper-writing-suite to revise Related Work: build a literature inventory and positioning analysis before drafting.
```

```text
Use paper-writing-suite to plan Figure 1 (method overview), generate the figure asset, and wire it into main.tex.
```

Bundled helper scripts use **Python 3 stdlib only** — no extra dependencies.

---

## What you get

End-to-end coverage from idea to camera-ready:

| Stage | Outputs |
|---|---|
| **Story** | Thesis, gap, contributions, claims to avoid |
| **Evidence** | `claim_evidence_map.md` tied to code / logs / tables |
| **Writing** | Abstract, Intro, Related Work, Method, Experiments, Limitations, Conclusion |
| **Literature** | Local corpus, positioning, verified `references.bib` |
| **Figures** | Plan + assets: **generated** overview/method diagrams; **deterministic** plots for numbers |
| **Review** | Reviewer-style risks, rejection diagnosis, self-review |
| **Submit** | Venue checklist, LaTeX build check, TODO/citation audit, packaging |

### Operating modes

The agent loads only what the task needs:

| Mode | When to use |
|---|---|
| Full-paper | Repo + results + template → draft or submission package |
| Story | Clarify thesis, gap, and contribution boundaries |
| Section | Revise one section with the right reference loaded |
| Figure | Plan diagrams and result plots; produce real files |
| Citation | Find, verify, repair BibTeX |
| Reviewer | Pre-submission risk scan |
| Submission | Checklist, build log, camera-ready checks |
| Automation | `scripts/` for claims, citations, TODOs, build logs |

Details: [`SKILL.md`](SKILL.md) and [`references/README.md`](references/README.md).

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

Clone this repo, then symlink (or copy) into your agent’s skills folder.

| Agent | Global path |
|---|---|
| **Cursor** | `~/.cursor/skills/paper-writing-suite` |
| **Codex** | `$CODEX_HOME/skills/paper-writing-suite` |
| **Claude Code** | `$HOME/.claude/skills/paper-writing-suite` |
| **Gemini** | `$HOME/.gemini/skills/paper-writing-suite` |

**Cursor — global**

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/paper-writing-suite ~/.cursor/skills/paper-writing-suite
```

**Cursor — project-level**

```bash
mkdir -p .cursor/skills
ln -s /path/to/paper-writing-suite .cursor/skills/paper-writing-suite
```

**Codex**

```bash
mkdir -p "$CODEX_HOME/skills"
ln -s /path/to/paper-writing-suite "$CODEX_HOME/skills/paper-writing-suite"
```

**Claude Code — global / project**

```bash
mkdir -p "$HOME/.claude/skills"
ln -s /path/to/paper-writing-suite "$HOME/.claude/skills/paper-writing-suite"
# or: .claude/skills/ for project-level
```

**Gemini**

```bash
mkdir -p "$HOME/.gemini/skills"
ln -s /path/to/paper-writing-suite "$HOME/.gemini/skills/paper-writing-suite"
```

---

## Repository layout

```text
paper-writing-suite/
├── SKILL.md              # Agent entry: modes, gates, evidence policy
├── references/           # Workflow, writing, citations, figures, venues, review
│   └── assets/           # Figure pattern references (figures4papers-style)
├── scripts/              # Claims, citations, TODOs, build-log, camera-ready checks
├── templates/            # NeurIPS / ICML / CVPR / ACL / … LaTeX starters
└── README.zh-CN.md
```

**Start here when digging in:**

| File | Purpose |
|---|---|
| [`references/workflow.md`](references/workflow.md) | Full-paper state machine |
| [`references/artifacts.md`](references/artifacts.md) | What to create in *your* paper repo |
| [`references/figure-workflow.md`](references/figure-workflow.md) | Diagrams vs plots; generation defaults |
| [`references/citation-workflow.md`](references/citation-workflow.md) | Search, verify, BibTeX |
| [`templates/README.md`](templates/README.md) | Template list and compile tips |

---

## Helper scripts

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
```

More: [`scripts/README.md`](scripts/README.md).

---

## Safety & hygiene

- Bundled templates are **convenience copies** — confirm current venue rules before submitting.  
- Do **not** commit private PDFs, proprietary logs, API keys, or reviewer-confidential material.

---

## Acknowledgements

Inspired by and building on ideas from:

- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)
- [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)

## License

MIT License.
