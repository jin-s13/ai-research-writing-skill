# Paper Writing Suite

[中文说明](README.zh-CN.md)

**Paper Writing Suite** is an agent skill for turning research artifacts into an evidence-backed paper draft and submission package.

It is designed for ML, AI, CV, NLP, and related research projects. The core idea is:

> Treat paper writing as a claim-evidence-engineering workflow, not prose generation.

The skill helps an AI assistant build a paper story, map claims to evidence, draft and revise sections, plan figures, verify citations, run checklist/build checks, and prepare Git or Overleaf submission artifacts.

## Installation

Assume this repository has been cloned locally. You can either copy it or symlink it into the skills directory used by your agent.

### Cursor

Global install:

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/paper-writing-skills ~/.cursor/skills/paper-writing-suite
```

Project-level install:

```bash
mkdir -p .cursor/skills
ln -s /path/to/paper-writing-skills .cursor/skills/paper-writing-suite
```

### Codex

```bash
mkdir -p "$CODEX_HOME/skills"
ln -s /path/to/paper-writing-skills "$CODEX_HOME/skills/paper-writing-suite"
```

### Claude Code

Global install:

```bash
mkdir -p "$HOME/.claude/skills"
ln -s /path/to/paper-writing-skills "$HOME/.claude/skills/paper-writing-suite"
```

Project-level install:

```bash
mkdir -p .claude/skills
ln -s /path/to/paper-writing-skills .claude/skills/paper-writing-suite
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
ln -s /path/to/paper-writing-skills "$HOME/.gemini/skills/paper-writing-suite"
```

## Usage

Example prompts:

```text
Use paper-writing-suite to inspect this repo and create the initial paper_story.md and claim_evidence_map.md.
```

```text
Use paper-writing-suite to revise the Related Work. Build a literature inventory and positioning analysis before drafting.
```

The bundled scripts use only the Python standard library.

## What It Covers

- Paper story and contribution positioning
- Claim-evidence mapping
- Abstract, Introduction, Related Work, Method, Experiments, Limitations, and Conclusion drafting
- Literature inventory and citation verification
- Figure/table planning with deterministic sources for numerical results
- Reviewer-style self-review and rejection-risk diagnosis
- Venue checklist, LaTeX build checks, and submission packaging

## Repository Structure

```text
paper-writing-suite/
├── SKILL.md                  # Agent-facing entry point
├── references/               # Workflow, writing, citation, figure, venue, and review guides
├── scripts/                  # Lightweight audit and formatting helpers
├── templates/                # Bundled LaTeX templates and source notes
└── README.zh-CN.md           # Chinese README for human readers
```

Key references:

- `references/README.md`: task-to-reference router.
- `references/workflow.md`: full-paper state machine.
- `references/artifacts.md`: durable output contract.
- `references/literature-review.md`: local paper corpus and positioning workflow.
- `references/citation-workflow.md`: citation search, verification, and BibTeX workflow.
- `references/figure-workflow.md`: figure planning and backend selection.

## Scripts

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
```

See `scripts/README.md` for details.

## Notes

- Bundled templates are convenience copies. Always check the official venue instructions before active submission.
- Do not commit private PDFs, proprietary experiment logs, API keys, or reviewer-confidential material.

## Acknowledgements

This project is inspired by and builds on ideas from related open-source skill collections, including:

- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## License

This project is licensed under the MIT License.