# Task Management and Completion

Use this for multi-file writing, full papers, major revisions, or submission work. Small one-shot edits need only a compact scope/evidence/check note.

## Task Packet

Create one file under `plan/task-packets/` with:

```markdown
# Task
- Scope:
- Target venue/template:
- Inputs and evidence:
- Files allowed to edit:
- Required artifacts:
- Rejection checks:
- Validation commands:
- Acceptance criteria:
```

## Progress

Keep `plan/progress.md` current:

```markdown
# Progress
- Stage:
- Inputs consumed:
- Artifacts produced:
- Verification run:
- Remaining scientific risk:
```

Do not leave phrases such as `verification planned`, `to be recorded`, or `待验证` in a terminal-stage package.

## Completion

Before reporting completion:

1. Check scope and required artifacts against the task packet.
2. Check claim support, citation fit, manuscript cleanliness, and reviewer risk.
3. Run the commands declared in the task packet and inspect their output.
4. Update `paper_state.json`, record the successful build, and rerun the quality gate.
5. Fix failures or record explicit blockers; no verification means drafted, not complete.
