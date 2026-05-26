# Reference Map

Use this file as the first stop when deciding which reference files to load. Load only the narrow references needed for the current task.

## Primary Routes

| User intent | Load first | Then load as needed |
|---|---|---|
| Full paper or major revision | `workflow.md`, `artifacts.md` | `paper-story.md`, `section-writing.md`, `citation-workflow.md`, `figure-workflow.md`, venue/reviewer references |
| Paper story, thesis, gap, or contributions | `paper-story.md` | `literature-review.md` if positioning is uncertain |
| Abstract / Introduction | `abstract-introduction.md` | `section-writing.md`, one example file after choosing a pattern |
| Related Work or positioning | `literature-review.md`, `citation-workflow.md` | `section-writing.md`, related-work examples |
| Method, Experiments, Limitations, or Conclusion | `section-writing.md` | `example-bank.md`, one narrow example file |
| Figures and tables | `figure-workflow.md`, `figure-spec.md` | `style-presets.md`, `figure-pattern-atlas.md`, `scripts/README.md` |
| Citations and BibTeX | `citation-workflow.md` | `citation-checklist.md` for final audit |
| Venue checklist text | `venue-profiles.md`, `venue-templates.md` | `reviewer-guidelines.md` |
| Reviewer diagnosis | `reviewer-guidelines.md`, `reviewer-self-review.md` | `artifacts.md` for `reviewer_analysis.md` |
| Submission or camera-ready package | `submission-packaging.md`, `citation-checklist.md` | `workflow.md`, `templates/README.md`, `templates/SOURCES.md` |
| Script usage | `../scripts/README.md` | The specific script file |

## Full-Paper Load Order

For full-paper tasks, use this order:

1. `workflow.md`: state machine and execution sequence.
2. `artifacts.md`: durable outputs to create in the target paper repo.
3. `paper-story.md`: thesis, gap, contribution, and claim boundaries.
4. `literature-review.md`: related work corpus and positioning if needed.
5. Section, figure, citation, venue, reviewer, and submission references as the workflow reaches them.

## Reference Layers

Use layers rather than numbered filenames. Semantic names are easier to maintain when references are added, removed, or reorganized.

- **Entry map**: `README.md`.
- **Core workflow**: `workflow.md`, `artifacts.md`.
- **Domain references**: story, writing, literature, figures, citations, venues, reviewers, and submission files.
- **Examples**: `examples/index.md` and one narrow example file when concrete wording patterns are needed.

## Loading Rules

- Start with `SKILL.md` for the entry contract and non-negotiable gates.
- Load this map before opening multiple reference files.
- Prefer one workflow reference plus one example file over loading the full `references/` tree.
- Use `references/examples/` only after choosing the section pattern.
- For full-paper tasks, maintain artifacts in the user's paper repo; do not modify this skill repository unless the user is editing the skill itself.

## Artifact Boundaries

The skill should produce auditable artifacts such as `paper_story.md`, `claim_evidence_map.md`, `literature/positioning.md`, `citation_verification.md`, `figures/figure_plan.md`, and `build_check.md`.

Generated paper artifacts belong in the target paper project, not in the skill library. See `artifacts.md` for the full contract.
