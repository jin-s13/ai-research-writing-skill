# Figure Workflow Reference

Use this reference when planning, generating, or revising figures for a paper.

Load `figure-spec.md` before creating a figure plan, and `style-presets.md` when visual style or venue sizing matters.

## Required Figure Plan

Create `figures/figure_plan.md` before producing figures. For each figure, specify:

- **Role**: overview, method detail, result summary, ablation, teaser, failure analysis.
- **Message**: the single claim the figure should communicate.
- **Entities**: modules, inputs, outputs, metrics, or datasets.
- **Relationships**: arrows, grouping, feedback loops, comparisons.
- **Layout**: horizontal pipeline, two-row process, grouped bars, heatmap, grid, etc.
- **Backend**: deterministic plot, TikZ/SVG, image generation, or hybrid.
- **Fallback**: how the paper compiles if generated assets are absent.

For larger projects, use the schema in `figure-spec.md` and store specs in `figures/figure_specs.yaml` or `figures/figure_specs.md`.

## Backend Selection

- Use deterministic plotting for numerical results. Prefer matplotlib/seaborn or direct SVG/PDF generation. Never use image generation for exact numbers.
- Use `scripts/make_latex_table.py` for exact CSV-to-LaTeX tables when table values must remain auditable.
- Use TikZ/SVG for diagrams that require exact text, labels, and arrows.
- Use the environment's built-in image generation capability for polished overview diagrams or teaser-style visuals only when text accuracy is non-critical or a fallback exists.
- Do not require or name a specific external image API/model for generated diagrams unless the user explicitly asks for one.
- For generated diagrams with labels, inspect the image before committing. If text is distorted, use TikZ/SVG instead.

## Figure Types

Choose the figure type by the claim it supports:

| Claim type | Recommended figure | Notes |
|---|---|---|
| System/workflow contribution | Pipeline or architecture diagram | Show artifacts, control flow, feedback, and deterministic/LLM boundaries. |
| Main quantitative comparison | Table or grouped bar chart | Tables are often better when many exact numbers matter. |
| Progress over time/iterations | Line plot | Include uncertainty when runs exist. |
| Ablation | Grouped bars or small multiples | Highlight the removed component and the consequence. |
| Difficulty breakdown | Stratified table, heatmap, or faceted bars | Keep level definitions visible in the caption or surrounding text. |
| Failure analysis | Grid of qualitative cases + short labels | Use only examples that illustrate a paper-level point. |

Avoid figures that are decorative. A figure should earn space by making a claim easier to understand or verify.

## Data Plot Standards

For numerical plots:

- Source data must live in a script, CSV/JSON, notebook-exported table, or documented result file.
- The plotting script should regenerate the exact asset from the source data.
- Prefer PDF/SVG for vector output; include PNG only when the venue/toolchain needs raster.
- Use at least 300 DPI for raster figures.
- Use colorblind-safe palettes for comparisons. The Okabe-Ito palette is a safe default:
  `#E69F00`, `#56B4E9`, `#009E73`, `#F0E442`, `#0072B2`, `#D55E00`, `#CC79A7`.
- Highlight the proposed method consistently across plots.
- Do not use 3D bars, pie charts for ML comparisons, heavy gridlines, or unexplained dual axes.
- Include metric direction in axis labels or captions.

Recommended matplotlib defaults:

```python
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "legend.fontsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
})
```

Use single-column width for simple comparisons and full-width figures only when density requires it.

## Diagram Prompt Template

For image-generated diagrams, include:

1. Venue and figure purpose.
2. Visual style with exact palette.
3. Canvas aspect ratio.
4. Layout regions.
5. Exact labels.
6. Arrows and feedback paths.
7. Constraints: no logos, no watermarks, no unsupported terminology, no tiny text.

Generated diagrams should be produced through the agent's built-in image-generation tool when available. Store the prompt or spec as the source, not vendor-specific API code.

### Diagram Prompt Structure

For generated overview diagrams, use this six-part prompt:

1. **Framing**: venue, section, reader takeaway, and tone.
2. **Visual style**: clean academic, sketch, modern minimal, or technical illustration.
3. **Color palette**: exact hex codes and consistent semantic meaning.
4. **Layout**: regions, panels, components, spacing, and reading order.
5. **Connections**: every arrow, feedback path, dashed failure path, and label.
6. **Constraints**: no hallucinated labels, no tiny text, no logos, no fake numbers, no unsupported claims.

Generated diagrams are strongest when they minimize text. If exact labels matter, make a TikZ/SVG version.

## LaTeX Fallback Pattern

Use this pattern for generated diagrams:

```latex
\IfFileExists{figures/name_generated.png}{%
  \includegraphics[width=\linewidth]{figures/name_generated.png}
}{%
  \input{figures/name_tikz}
}
```

For result plots, prefer PDF first:

```latex
\IfFileExists{figures/result.pdf}{%
  \includegraphics[width=\linewidth]{figures/result.pdf}
}{%
  \includegraphics[width=\linewidth]{figures/result.png}
}
```

## Figure Quality Checklist

- Does the figure communicate one message?
- Is the text readable at final paper size?
- Are exact numbers generated by code rather than image models?
- Are colors colorblind-safe where comparisons matter?
- Is there a source file or prompt for regeneration?
- Is the caption self-contained?
- Does the paper text refer to the figure and explain its takeaway?

## Caption Pattern

Use captions as miniature arguments:

1. Define what is shown.
2. State the metric direction or visual encoding.
3. Give the takeaway.
4. Mention caveats only when needed for interpretation.

Example pattern:

```text
Figure X: Overview of METHOD. The workflow converts ... into ... by separating ...
Dashed arrows indicate reflection or retry paths. This separation lets ... while preserving ...
```

## QA Before Submission

- View the figure at final paper width.
- Check grayscale readability when color encodes comparisons.
- Confirm every label matches the paper terminology.
- Confirm all numbers match the source data.
- Confirm figure files are not unnecessarily large.
- Confirm every figure is referenced in the text before or near its appearance.
