# Figure Specification Reference

Use this before making any paper figure. It makes the role/message/entities/layout/backend workflow explicit enough for review.

## Required Figure Spec

For every figure, create this spec before generating assets:

```yaml
figure_id: fig:overview
filename: figures/fig_overview
figure_class: evidence-result | concept-method
role: overview | method-detail | result-summary | ablation | failure-analysis | teaser | appendix
message: "One sentence claim the figure supports."
core_conclusion: "The conclusion this figure must make defensible."
evidence_hierarchy:
  hero_evidence: "Primary visual or quantitative evidence."
  supporting_evidence: "Secondary panels, controls, ablations, or examples."
entities:
  - name: "Input"
    type: artifact | module | dataset | metric | baseline | output
    description: "What it represents."
relationships:
  - source: "Input"
    target: "Planner"
    relation: data-flow | control-flow | feedback | comparison | failure-path
layout: left-to-right pipeline | framework overview | horizontal bands | two-row process | grouped bars | line plot | heatmap | table
backend: deterministic-plot | latex-table | generated-image | hybrid
source: "CSV/log/script/prompt path"
backup: "optional TikZ/SVG reference or compile fallback path"
caption_takeaway: "The sentence the caption must communicate."
evidence_status: exact-data | illustrative-only | qualitative-example
reviewer_risk: "What a skeptical reviewer may question about this figure."
```

## Figure Role Taxonomy

| Role | Class | Purpose | Typical backend |
|---|---|---|---|
| overview | concept-method | Explain the whole method or system | generated-image (default); optional TikZ/SVG reference |
| method-detail | concept-method | Explain one module, invariant, or interface | generated-image or hybrid |
| framework/pipeline | concept-method | Show the paper's method, architecture, or processing stages | generated-image (default); optional TikZ/SVG reference |
| teaser | concept-method | Make the task and output intuitive | generated-image or curated examples |
| result-summary | evidence-result | Support the main quantitative claim | deterministic plot or table |
| ablation | evidence-result | Show which design choices matter | deterministic plot or table |
| difficulty breakdown | evidence-result | Explain performance by subset/level | deterministic plot or heatmap |
| failure-analysis | evidence-result | Show systematic failure modes | qualitative grid + labels |

## Backend Rules

- `evidence-result`: use `deterministic-plot` or `latex-table`. This class covers numerical charts, tables, result summaries, ablations, benchmark comparisons, trend plots, heatmaps, and metric-driven qualitative grids.
- `concept-method`: use `generated-image` or `hybrid`. This class covers method, teaser, framework, pipeline, architecture, overview, and mechanism-style diagrams.
- `generated-image`: for `concept-method`, use built-in image generation as the default figure in the paper. TikZ/SVG precise schematics are optional backup/reference only—not a parallel required deliverable.
- `hybrid`: use when a generated image is paired with deterministic labels, LaTeX text, or SVG annotations; optional TikZ/SVG may serve as terminology reference, not as the primary figure.
- TikZ/SVG alone is only acceptable for `concept-method` when image generation is unavailable, blocked by policy, or inappropriate for the content.

Never use image generation for exact numbers, axes, metric values, or tables.

## Figure Contract

Before generating assets, write the figure as an argument, not a decoration:

1. **Core conclusion**: the one sentence this figure must defend.
2. **Panel map**: what each panel contributes; remove panels that do not add unique evidence.
3. **Evidence hierarchy**: which panel is the hero evidence, which panels are validation, controls, ablations, examples, or failure cases.
4. **Source traceability**: data, prompts, scripts, generated assets, and exact-text backups.
5. **Reviewer risk**: what may be challenged, such as missing sample size, unclear metric direction, unverifiable qualitative example, distorted labels, or unsupported visual analogy.

## Data Chart Selection

| Data shape | Chart |
|---|---|
| steps/time x metric | line plot |
| methods x metrics | grouped bar chart or table |
| many methods sorted by one metric | horizontal bar chart |
| matrix or pairwise scores | heatmap |
| distribution | box/violin/histogram |
| two continuous variables | scatter plot |
| exact benchmark report | LaTeX table |

When in doubt, use a table for exact numbers and a plot for trends.

## Figure Plan Checklist

- Does the figure have one message?
- Does the message map to a paper claim?
- Are all entities named with the same terminology as the paper?
- Does the layout match the relationship type?
- Does each panel carry unique evidence for the core conclusion?
- Is the evidence hierarchy clear, with a hero panel or main visual message?
- Is backend risk appropriate for the content?
- Is the source file listed?
- Is the generated image produced, or is there a documented blocker? (Optional TikZ/SVG reference only when needed.)
- Is reviewer risk recorded before final styling?
- Is the caption takeaway written before final styling?

## Caption Contract

Captions should not merely describe visual elements. Use:

```text
Figure X: [What is shown]. [How to read it]. [Takeaway]. [Caveat if needed].
```

For quantitative figures, include metric direction and whether values are mean, median, standard deviation, confidence interval, or single-run.
