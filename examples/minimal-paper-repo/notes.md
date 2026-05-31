# Research Notes

## Project

ToyCalib studies whether a lightweight calibration head can improve confidence calibration for a small image classifier without changing the backbone.

## Method

The method freezes a baseline classifier and trains a two-layer calibration head on validation logits. The head outputs temperature-like corrections conditioned on logit entropy.

## Evidence Available

- `results/main_results.csv` contains the demo metrics.
- The strongest supported claim is improved expected calibration error on this toy setup.
- The demo does not support broad claims about robustness, state-of-the-art performance, or transfer to real benchmarks.

## Target Venue

Use a generic ML workshop style for the demo. Do not claim conference readiness.
