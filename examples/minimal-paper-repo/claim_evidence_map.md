# Claim-Evidence Map

| Claim | Evidence | Status | Risk |
|---|---|---|---|
| ToyCalib reduces expected calibration error in the demo table. | `results/main_results.csv`: ECE 0.071 to 0.039 | Supported | Demo-only result |
| ToyCalib keeps accuracy nearly unchanged. | `results/main_results.csv`: accuracy 0.842 to 0.845 | Supported | No uncertainty or seeds |
| The method is lightweight. | `notes.md`: two-layer calibration head over logits | Partially supported | Parameter count not recorded |
| ToyCalib is broadly robust. | No evidence | Unsupported | Must not be claimed |
