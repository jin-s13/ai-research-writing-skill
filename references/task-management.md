# Task Management and Completion Audit

Use this reference for medium or full-paper tasks, multi-file revisions, quality repair, or any work where the agent could lose track of scope across turns.

## When This Applies

A task is medium-sized if it affects more than one paragraph, one subsection, one section, a figure/table set, citation positioning, experiments, or submission readiness.

For small one-shot edits, do not create bureaucracy. Preserve the same discipline in a compact note: scope, evidence, changes, and checks.

## Task Packet

Create a persistent packet before substantial drafting:

```markdown
## Task Packet
- Scope:
- Target venue/template:
- Files to read:
- Files allowed to edit:
- Evidence/data inputs:
- Required artifacts:
- Rejection checks:
- Validation commands:
- Acceptance criteria:
```

Place packets under `plan/task-packets/` when the target paper repo already has or needs a `plan/` workspace. If the repo has another planning convention, follow it.

## Progress Log

Update `plan/progress.md` at the start and end of a medium task:

```markdown
## Current task
- Stage:
- Task:
- Input files:
- Output files:
- Required artifacts:
- Verification planned:

### Capability-use audit
- Required references/scripts:
- Inputs consumed:
- Inputs not used and why:
- Artifacts produced:
- Verification run:
- Remaining risk:
```

## Two Review Gates

Run both before calling the work complete:

1. **Spec compliance**: output files, scope, required artifacts, and acceptance criteria match the task packet.
2. **Quality review**: claims are supported, citations fit the sentence-level claim, prose is manuscript-ready, and process notes did not leak into the draft.

If either review fails, fix the issue or record a visible blocker.

## Manuscript Cleanliness

Keep planning language out of the paper body. These belong in plan or review files, not in `.tex` or chapter prose:

- user instructions such as "write naturally", "avoid AI tone", or "replace later";
- unresolved placeholders such as TODO, TBD, fill later, citation needed;
- process headings such as experiment purpose, table position, figure position, or discussion prompt;
- claims that something is verified when no verification artifact exists.

## Completion Rule

Before reporting completion:

1. Confirm required artifacts exist.
2. Run the relevant script checks, build, or citation validation when available.
3. Read the output and decide whether it supports the completion claim.
4. Record blockers and remaining risks explicitly.

No verification means "drafted" or "prepared", not "complete".
