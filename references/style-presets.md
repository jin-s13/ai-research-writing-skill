# Style Presets Reference

Use this reference when creating figures or unifying a paper's visual language. Exact data must remain deterministic.

## Universal Figure Rules

- Prefer PDF/SVG for deterministic plots and overlays; use high-resolution PNG/PDF exports for built-in image-generated diagrams.
- Use 300 DPI or higher for raster images.
- Use colorblind-safe palettes and never rely on color alone.
- Keep all text readable at final paper size; no text below 7 pt.
- Avoid 3D effects, decorative gradients, clip art, watermarks, and fake UI chrome.
- Keep style consistent across figures in the same paper.

## Venue Figure Sizes

| Venue | Single-column / main width | Full width | Notes |
|---|---:|---:|---|
| NeurIPS / ICLR single-column style | 5.5 in | 5.5 in | Main paper often single-column. |
| ICML two-column style | 3.25 in | 6.75 in | Use `figure*` for full width. |
| ACL / EMNLP two-column style | 3.3 in | 6.8 in | Full-width figures require `figure*`. |
| AAAI two-column style | 3.3 in | 7.0 in | Keep labels compact. |

Always check the actual template.

## Data Plot Preset

Recommended matplotlib defaults:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.18,
    "grid.linewidth": 0.6,
})
```

## Palettes

### Okabe-Ito

Use when comparison accuracy matters:

```python
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]
```

### Ocean Dusk

Use for polished ML/system charts:

```python
OCEAN_DUSK = {
    "teal": "#264653",
    "cyan": "#2A9D8F",
    "gold": "#E9C46A",
    "orange": "#F4A261",
    "coral": "#E76F51",
    "gray": "#8C8C8C",
}
OURS = "#E76F51"
BASELINE = "#B0BEC5"
BEST_BASELINE = "#264653"
```

## Diagram Styles

### Classic Academic

Use when a diagram needs exact labels or deterministic overlays.

- White background.
- Pale section bands.
- Thin gray borders.
- Solid arrows for data flow.
- Dashed red arrows for failure/retry.
- Minimal icons.

### Modern Minimal

Use for clean image-generated method, framework, pipeline, and overview figures.

- Sparse layout.
- One accent color per group.
- No decorative icons.
- Large whitespace.
- Thin gray arrows.

### Sketch / Whiteboard

Use for memorable overview figures when exact text is limited.

- Warm off-white background.
- Charcoal outlines.
- Soft washed fills.
- Hand-drawn line quality.
- Use only if labels remain readable.

### Illustrated Technical

Use for explanatory documentation-style diagrams.

- Small consistent line icons.
- Soft group regions.
- Curved arrows.
- Keep text short.

## Arrow Conventions

| Semantic relation | Style |
|---|---|
| data flow | solid arrow, colored by source group |
| control flow | solid gray arrow |
| feedback/reflection | dashed curved arrow |
| error/failure | dashed red arrow |
| optional path | dotted gray arrow |
| equivalence/comparison | double-headed or bracket annotation |

Use the same conventions in all method figures.
