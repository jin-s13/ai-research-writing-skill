# Related Work Example: Line of Work Paragraph

Use this pattern when summarizing a broad line of work. The paragraph should explain the line's contribution, cite representative papers, and then identify the gap that motivates the current paper.

## Pattern

```text
[Line of work] studies [problem or setting]. Representative methods [shared technical idea], enabling [main capability]. However, these methods usually assume [assumption] or optimize for [objective], which leaves [gap] underexplored. Our work is closest in its interest in [shared concern], but differs by [task boundary / input-output setting / evidence target].
```

## Annotated Example

```text
Learning-based 3D reconstruction methods estimate scene geometry from sparse or posed image collections. Representative neural rendering and implicit-field approaches improve view synthesis quality by optimizing continuous scene representations, making them strong references for geometry-aware visual modeling. However, many of these methods are designed for reconstruction or rendering fidelity rather than the downstream decision setting considered in this paper. Our work is closest in its use of learned scene representations, but differs by treating geometry as evidence for [your task] rather than as the final output.
```

## Why It Works

- Sentence 1 names the research problem.
- Sentence 2 states what the line of work solves.
- Sentence 3 identifies the assumption or coverage gap.
- Sentence 4 positions the paper without making prior work look weak.

Replace the generic citations and task names with verified papers from `literature/related_work_matrix.md`.
