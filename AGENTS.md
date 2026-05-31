# AI Research Writing Skill

This repository provides a cross-platform agent skill for ML/AI/CV/NLP research paper writing.

## Entry Point

When a user asks for research paper drafting, revision, citation repair, literature positioning, figure/table design, LaTeX work, reviewer self-review, or submission packaging, load and follow:

- `SKILL.md`

Then load only the narrow reference files needed from `references/`.

Plugin hosts that discover skills from a `skills/` directory may first load `skills/ai-research-writing-skill/SKILL.md`; that file is a thin wrapper back to the root `SKILL.md`.

## Core Rules

- Treat paper writing as claim-evidence engineering, not prose generation.
- Do not invent citations or BibTeX.
- For medium or full-paper tasks, create task state: `plan/task-packets/<task>.md` and `plan/progress.md` when appropriate.
- Run or record verification before claiming completion.
- Keep generated paper artifacts in the user's target paper repository, not in this skill library.

## Useful References

- `references/README.md` for reference routing.
- `references/workflow.md` for full-paper workflow.
- `references/artifacts.md` for expected durable outputs.
- `references/task-management.md` for task packets, progress logs, and completion audit.
- `scripts/README.md` for helper scripts.
