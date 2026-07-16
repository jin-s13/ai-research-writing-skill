# Numeric Evidence

Use `numeric_evidence.json` for quantitative papers. Version 2 verifies manuscript numbers by recomputing them from JSON, JSONL, CSV, or TSV sources.

```json
{
  "schema_version": "ai-research-writing/numeric-evidence-v2",
  "entries": [
    {
      "value": 0.912,
      "source": "experiments/raw_results.csv",
      "selector": {"kind": "csv", "column": "accuracy", "where": {"method": "ours"}},
      "aggregate": "mean",
      "representations": ["raw", "percent"],
      "tolerance": 0.0001,
      "note": "Mean test accuracy over matching rows"
    }
  ]
}
```

Selectors are strict:

- `json-pointer`: requires `pointer`; the selected value may be one number or an array.
- `csv` / `tsv`: requires `column`; optional `where` matches exact row values.
- `jsonl`: requires `column`; optional `where` selects records.

Aggregates are `identity`, `mean`, `sample-std`, `population-std`, `sum`, `min`, `max`, and `count`. `identity` requires exactly one selected value. The checker recomputes the aggregate and compares it with the registered value using the declared narrow tolerance.

Run:

```bash
python3 scripts/check_numeric_evidence.py /path/to/paper-project
```

The checker audits all tables plus Results, Experiments, Evaluation, Ablation, Analysis, Findings, and Benchmark sections. An unregistered or unreproducible number is a failure. Version 1 registries must be migrated explicitly; source fragments such as `results.json#/score` become `source: results.json` plus a `json-pointer` selector.
