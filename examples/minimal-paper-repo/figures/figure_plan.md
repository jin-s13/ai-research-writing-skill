# Figure Plan

## Figure 1: ToyCalib Workflow

- Type: concept-method.
- Message: A frozen classifier produces logits; ToyCalib uses entropy-conditioned corrections to improve calibration.
- Source: `notes.md`.
- Backend: image generation or deterministic diagram fallback.
- Fallback: simple Mermaid/TikZ pipeline with three boxes.
- Risk: do not include numeric metric values in generated artwork.

## Figure 2: Main Result Table or Bar Plot

- Type: evidence-result.
- Message: ToyCalib has lower ECE than baseline in the demo table.
- Source: `results/main_results.csv`.
- Backend: deterministic Python/LaTeX table.
- Risk: label as demo data, not benchmark evidence.
