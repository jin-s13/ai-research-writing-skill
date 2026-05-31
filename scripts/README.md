# Script Reference

The scripts in this directory are lightweight helpers for paper-writing audits. They intentionally use only the Python standard library.

## Scripts

| Script | Purpose | Typical use |
|---|---|---|
| `extract_claims.py` | Bootstrap a claim-evidence map from Abstract/Introduction text | `python3 scripts/extract_claims.py main.tex > claim_evidence_map.md` |
| `check_citations.py` | Check that citation keys in LaTeX exist in a BibTeX file | `python3 scripts/check_citations.py main.tex references.bib` |
| `check_todos.py` | Detect unresolved TODO-like markers | `python3 scripts/check_todos.py main.tex references.bib figures` |
| `parse_build_log.py` | Summarize LaTeX build log errors, undefined refs/cites, and box warnings | `python3 scripts/parse_build_log.py main.log` |
| `camera_ready_check.py` | Run a static final/camera-ready readiness audit | `python3 scripts/camera_ready_check.py main.tex` |
| `research_quality_gate.py` | Run project-level checks for required planning artifacts, placeholders, process text, citation markers, and prose/list balance | `python3 scripts/research_quality_gate.py /path/to/paper-project` |
| `make_latex_table.py` | Generate a booktabs LaTeX table from CSV | `python3 scripts/make_latex_table.py results.csv --caption "Main results." --label tab:main` |

## Scope

These scripts are static checks and format helpers. They do not replace manual review, venue instructions, or a real LaTeX build.
