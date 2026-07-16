# Numeric Evidence

Use this for quantitative papers. `numeric_evidence.json` is a platform-independent whitelist of manuscript numbers and their provenance.

```json
{
  "schema_version": "ai-research-writing/numeric-evidence-v1",
  "entries": [
    {
      "value": 0.912,
      "source": "experiments/results.json#/accuracy",
      "locator": "condition=method-a, seed aggregate",
      "representations": ["raw", "percent"],
      "tolerance": 0.0001,
      "note": "Mean test accuracy over five seeds"
    }
  ]
}
```

Every source path must exist inside the project. A JSON fragment must be an RFC 6901-style pointer; the checker resolves it and verifies the registered source value. `raw` permits `0.912`; `percent` permits `91.2`. Keep tolerance narrow and intentional. Register result values, uncertainty, sample/seed counts, dataset statistics, hyperparameters, and constants when they appear in evidence-sensitive sections.

Run:

```bash
python3 scripts/check_numeric_evidence.py /path/to/paper-project
```

The checker audits all tables plus Results, Experiments, Evaluation, Ablation, Analysis, Findings, and Benchmark sections. An unregistered number is a failure; add real provenance, revise the number, or remove the unsupported statement. Do not solve failures with broad tolerances or fabricated registry entries.

This check establishes that a manuscript number was deliberately registered against a source file. It does not prove the experiment was scientifically valid or that a summary statistic was computed correctly; inspect source generation and statistical methodology separately.
