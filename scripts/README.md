# Script Reference

The scripts in this directory are lightweight helpers for paper-writing audits. They intentionally use only the Python standard library.

## Scripts

| Script | Purpose | Typical use |
|---|---|---|
| `extract_claims.py` | Bootstrap a claim-evidence map from Abstract/Introduction text | `python3 scripts/extract_claims.py main.tex > claim_evidence_map.md` |
| `check_citations.py` | Check that citation keys in LaTeX exist in a BibTeX file | `python3 scripts/check_citations.py main.tex references.bib` |
| `verify_citations.py` | Resolve DOI/arXiv metadata, optionally cross-check OpenAlex, and write a fail-closed lock | `python3 scripts/verify_citations.py /path/to/paper-project --mailto you@example.org` |
| `check_citation_lock.py` | Validate request, metadata, and claim-support digests without network access | `python3 scripts/check_citation_lock.py /path/to/paper-project` |
| `check_todos.py` | Detect unresolved TODO-like markers | `python3 scripts/check_todos.py main.tex references.bib figures` |
| `check_numeric_evidence.py` | Check numbers in evidence-sensitive sections and tables against declared provenance | `python3 scripts/check_numeric_evidence.py /path/to/paper-project` |
| `check_research_handoff.py` | Validate evidence exported by an upstream research system | `python3 scripts/check_research_handoff.py /path/to/handoff-project --require-unblocked` |
| `parse_build_log.py` | Summarize LaTeX build log errors, undefined refs/cites, and box warnings | `python3 scripts/parse_build_log.py main.log` |
| `camera_ready_check.py` | Run a static final/camera-ready readiness audit | `python3 scripts/camera_ready_check.py main.tex` |
| `fetch_template.py` | Fetch a pinned official author-kit archive with SHA-256 and extraction checks | `python3 scripts/fetch_template.py icml2026 --output paper/.venue-template` |
| `research_quality_gate.py` | Enforce the mode-aware `paper_state.json` contract, artifact/citation state, complete LaTeX inputs, and recorded build hashes | `python3 scripts/research_quality_gate.py /path/to/paper-project` |
| `record_build.py` | Execute the declared build and record its log, environment, and hashes | `python3 scripts/record_build.py /path/to/paper-project --run` |
| `make_latex_table.py` | Generate a booktabs LaTeX table from CSV | `python3 scripts/make_latex_table.py results.csv --caption "Main results." --label tab:main` |

## Scope

All scripts use the Python standard library and fail explicitly on missing or unreadable declared inputs. They enforce mechanical contracts; they do not replace semantic citation review, scientific judgment, official venue instructions, or a real LaTeX build.
