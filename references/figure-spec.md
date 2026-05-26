# Figure Specification Reference

Use this before making any paper figure. It makes the role/message/entities/layout/backend workflow explicit enough for review.

## Required Figure Spec

For every figure, create this spec before generating assets:

```yaml
figure_id: fig:overview
filename: figures/fig_overview
role: overview | method-detail | result-summary | ablation | failure-analysis | teaser | appendix
message: "One sentence claim the figure supports."
entities:
  - name: "Input"
    type: artifact | module | dataset | metric | baseline | output
    description: "What it represents."
relationships:
  - source: "Input"
    target: "Planner"
    relation: data-flow | control-flow | feedback | comparison | failure-path
layout: left-to-right pipeline | framework overview | horizontal bands | two-row process | grouped bars | line plot | heatmap | table
backend: deterministic-plot | latex-table | generated-image | hybrid | tikz-fallback | svg-fallback
source: "CSV/log/script/prompt path"
fallback: "TikZ/SVG/PDF/PNG fallback path"
caption_takeaway: "The sentence the caption must communicate."
evidence_status: exact-data | illustrative-only | qualitative-example
```

## Figure Role Taxonomy

| Role | Purpose | Typical backend |
|---|---|---|
| overview | Explain the whole method or system | generated-image with fallback |
| method-detail | Explain one module, invariant, or interface | generated-image or hybrid |
| result-summary | Support the main quantitative claim | deterministic plot or table |
| ablation | Show which design choices matter | deterministic plot or table |
| difficulty breakdown | Explain performance by subset/level | deterministic plot or heatmap |
| failure-analysis | Show systematic failure modes | qualitative grid + labels |
| teaser | Make the task and output intuitive | generated-image or curated examples |
| framework/pipeline | Show the paper's method, architecture, or processing stages | generated-image with fallback |

## Backend Rules

- `deterministic-plot`: required for all numerical charts.
- `latex-table`: use for exact values, many metrics, or leaderboard-style comparison.
- `generated-image`: default for non-numeric paper diagrams, including method, teaser, framework, pipeline, architecture, and overview figures. Use the agent's built-in image-generation capability, not a specific external API/model.
- `hybrid`: use when a generated visual is paired with deterministic labels, LaTeX text, SVG annotations, or a TikZ/SVG fallback.
- `tikz-fallback`/`svg-fallback`: use as fallback assets or exact-label overlays; do not make TikZ the default backend for method, framework, teaser, or pipeline figures.

Never use image generation for exact numbers, axes, metric values, or tables.

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
- Is backend risk appropriate for the content?
- Is the source file listed?
- Is there a fallback for generated diagrams?
- Is the caption takeaway written before final styling?

## Caption Contract

Captions should not merely describe visual elements. Use:

```text
Figure X: [What is shown]. [How to read it]. [Takeaway]. [Caveat if needed].
```

For quantitative figures, include metric direction and whether values are mean, median, standard deviation, confidence interval, or single-run.
