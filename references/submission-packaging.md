# Submission Packaging Reference

Use this reference when preparing a draft for local build, Overleaf, arXiv, camera-ready, or Git submission.

## Packaging Principle

A submission package should be buildable, auditable, and free of accidental placeholders. Do not treat a polished PDF as sufficient if the source tree contains unresolved citations, broken figure paths, stale generated assets, or hidden TODOs.

## Build Workflow

1. Identify the main `.tex` file.
2. Identify the bibliography file and bibliography tool: BibTeX, biblatex, or natbib.
3. Run the venue-compatible build command if available.
4. Record the result in `build_check.md`.
5. If TeX tools are missing, record the missing command and still run static checks when possible.

Recommended BibTeX build:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Recommended latexmk build when available:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## Static Checks

Run when applicable:

```bash
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
```

Also inspect:

- Missing figure files.
- Duplicate BibTeX keys.
- Overfull/underfull box warnings when build logs exist.
- Undefined references and citations.
- Placeholder author names in anonymous submissions.
- Accidental acknowledgments in anonymous submissions.

## Artifact Hygiene

Before committing:

- Keep source files for plots and diagrams.
- Prefer vector formats for exact plots and diagrams.
- Compress large PNGs only if quality remains acceptable.
- Remove `.DS_Store`, temporary TeX files, stale PDFs, and failed generation attempts unless intentionally archived.
- Do not commit private datasets, API keys, credentials, or local absolute paths.
- Check that generated figures match the paper text and captions.

## Overleaf / Git Workflow

For an Overleaf-linked repository:

1. Run `git status --short`.
2. Inspect modified files and generated assets.
3. Run citation/TODO/build checks.
4. Stage only intended files.
5. Commit with a concise message.
6. Push only when the user has asked for it or clearly authorized it.
7. Confirm the remote branch and push result.

Never revert unrelated user edits while packaging.

## Submission Readiness Template

Create or update `submission_readiness.md`:

```text
Target venue:
Template:
Main tex:
Build status:
Citation check:
TODO/placeholder check:
Checklist status:
Limitations status:
Reproducibility status:
Figure/source status:
Known reviewer risks:
Known packaging risks:
Next actions:
```

## Camera-Ready Differences

For final/camera-ready mode, additionally check:

- Author names, affiliations, and acknowledgments.
- License and data/code links.
- Updated arXiv or supplementary references.
- Reviewer-requested changes.
- Appendix cross-references.
- Final page limits and file-size limits.

## Final Response Contract

When reporting packaging work, include:

- Files changed.
- Checks run and their results.
- Build status.
- Remaining blockers.
- Commit or push hash if performed.
