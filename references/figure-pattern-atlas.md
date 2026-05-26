# Figure Pattern Atlas

Use this reference for Class 1 figures: deterministic evidence/result figures, including result figures, ablation figures, trend plots, heatmaps, radar plots, qualitative evidence grids, and publication-style multi-panel evidence figures.

Vendored local reference assets live in:

- `references/assets/figures4papers/`

Use these files as local pattern references. Do not copy demo data, manuscript-specific labels, or scientific claims into a target paper. Reuse the visual pattern, layout logic, palette discipline, and export conventions.

## When To Use

Load this after `figure-workflow.md` and `figure-spec.md` when:

- a result figure needs more than a simple bar or line plot;
- multiple panels must support one paper claim;
- the user asks for Nature-style, high-impact, publication-ready, or figures4papers-style plots;
- the figure needs SVG/PDF/high-DPI outputs with editable text.

When using the atlas, inspect the closest local `plot_*.py` files under `references/assets/figures4papers/` before writing a new deterministic plotting script.

For Class 2 concept/method diagrams, follow `figure-workflow.md`: generated image is the visual/inspiration version, while TikZ/SVG is the exact-text backup. Use this atlas mainly for Class 1 deterministic result panels and exact-text/vector backups.

## Pattern Routing

| Figure need | Pattern to inspect | Typical implementation |
|---|---|---|
| Main comparison across methods and metrics | Ultra-wide grouped bars with a legend-only panel | inspect `figure_ImmunoStruct`, `figure_CellSpliceNet`, or `figure_brainteaser` |
| Ablation across module variants | Same-hue alpha gradient or compact horizontal bars | inspect `figure_ImmunoStruct`, `figure_CellSpliceNet`, or `figure_Cflows` |
| Training, scaling, or progress over steps | Trend lines with uncertainty bands and event annotations | inspect `figure_VIGIL` or `figure_ophthal_review` |
| Matrix, pairwise score, or subset breakdown | Heatmap with readable colorbar and cell annotations | inspect `figure_RNAGenScape` or `figure_ophthal_review` |
| Model-family comparison over several criteria | Radar or polar comparison | inspect `figure_VIGIL` |
| Qualitative result plus quantification | Image plate + small quantitative support panels | representative examples, scale/label clarity, traceable source paths |
| Survey or composition figure | Stacked bars, composition heatmap, or timeline trend | consistent category order and compact legend |
| Concept or motivation panel | Simple 2D/3D schematic only when it supports a claim | inspect `figure_Dispersion`, `figure_Cflows`, or `figure_FPGM`; prefer generated visual + exact-text SVG/TikZ backup |

## Reusable Design Rules

- Start from the figure's core conclusion and evidence hierarchy, not from a favorite template.
- Give one panel the hero role when the claim has a main piece of evidence; supporting panels should validate or explain, not compete.
- Prefer coherent hue families over many saturated category colors.
- Keep the proposed method, baseline family, and ablation variants color-consistent across panels.
- Reserve green/red for directional gains, drops, errors, thresholds, or failure annotations.
- Use direct labels when they reduce eye travel; use a legend-only panel when categories are numerous.
- Avoid fixed 0-100 axes when values occupy a narrow range; tighten limits while preserving honest interpretation.
- For ablations, encode completeness or removed components with alpha, hatch, or ordered variants rather than unrelated colors.
- For grayscale safety, use hatches, markers, or line styles in addition to color.

## Export Contract

For deterministic plots:

- Save editable vector output first: `figures/name.svg` and/or `figures/name.pdf`.
- Save high-DPI raster preview when useful: `figures/name.png` or `figures/name.tiff` at 300-600 DPI.
- Keep text editable in SVG/PDF where possible (`svg.fonttype = "none"`, `pdf.fonttype = 42` for matplotlib).
- Store the plotting script and source data beside or near the generated asset.
- Never use generated images for exact numbers, axes, metric values, or tables.

## Matplotlib Baseline

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
    "savefig.bbox": "tight",
})
```

## Palette Families

Use restrained families for dense multi-panel pages:

```python
PALETTE_NMI_PASTEL = {
    "baseline_dark": "#484878",
    "baseline_mid": "#7884B4",
    "baseline_soft": "#B4C0E4",
    "ours_tiny": "#E4E4F0",
    "ours_base": "#E4CCD8",
    "ours_large": "#F0C0CC",
    "delta_up": "#2E9E44",
    "delta_down": "#E53935",
}
```

Use the same method family color in every panel. Do not recolor a method just because a later panel has space for more hues.

## Attribution and Licensing

Treat vendored figure assets as reference material and preserve attribution in this repository. Prefer rewriting the pattern in the target paper's own plotting script rather than copying demo content verbatim.
