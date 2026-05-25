# Citation and Checklist Reference

Use this reference for bibliography, citation verification, conference checklist, reproducibility, and build readiness.

For finding and adding new references, load `citation-workflow.md` first. This file is the final audit layer.

## Citation Rules

- Never write BibTeX from memory.
- Prefer primary sources: arXiv, DOI/Crossref, Semantic Scholar, official publisher pages, or official software documentation.
- Record each citation source in `citation_verification.md`.
- If a citation cannot be verified, use a visibly named placeholder such as `PLACEHOLDER_author_year_verify` and state it in the final response.
- Do not cite a paper for a claim unless the paper actually supports that claim.
- For concurrent work, avoid strong comparative claims unless the methods and metrics are clearly comparable.

## Five-Step Citation Workflow

Use this workflow whenever adding new citations:

1. **Search**: find candidate papers with Semantic Scholar, Crossref, arXiv, OpenAlex, publisher pages, or web search.
2. **Verify existence**: confirm title/authors/year in at least one authoritative source; use two sources when metadata conflicts.
3. **Retrieve BibTeX**: prefer DOI/arXiv/publisher BibTeX, not hand-written entries.
4. **Validate claim support**: check that the cited work supports the sentence-level claim.
5. **Record**: add the BibTeX entry and log the source in `citation_verification.md`.

If any step fails, do not silently cite the work. Use a visible placeholder or remove the sentence.

## Source Preference

Use this priority:

1. DOI/publisher page or official proceedings.
2. arXiv page for preprints.
3. Semantic Scholar / OpenAlex / Crossref metadata.
4. Official software documentation for tools and libraries.
5. Project repositories only for software artifacts, not paper claims.

Avoid citing secondary summaries for technical claims unless the claim is about the summary itself.

## Claim-Level Citation Audit

For each citation sentence, classify the relation:

- `direct`: the cited work directly establishes the sentence.
- `background`: the cited work motivates the area but does not prove the specific claim.
- `contrast`: the cited work is being contrasted with this paper.
- `software`: the citation supports a tool/library/dataset.
- `weak`: the citation does not support the sentence and should be changed.

Only `direct`, `contrast`, and `software` should support strong claims.

## Verification Table

`citation_verification.md` should contain:

| Key | Source checked | Status | Notes |
|---|---|---|---|

Status values:

- `verified`
- `software-doc`
- `placeholder`
- `needs-license-check`
- `removed`

Recommended columns for full papers:

| Key | Source checked | Claim supported | Relation | Status | Notes |
|---|---|---|---|---|---|

## Checklist Rules

- Match the checklist to the actual target venue and template.
- If target venue and template conflict, state the conflict and ask only if it changes the submission requirements.
- Fill checklists honestly. `No` with a concrete plan is acceptable; unsupported `Yes` is dangerous.
- Include sections for limitations, broader impacts, reproducibility, data/code access, compute, licenses, and LLM usage when applicable.

## Venue Checklist Themes

Most ML venues ask for some combination of:

- Claim/evidence consistency.
- Limitations and failure modes.
- Reproducibility details: code, data, parameters, seeds, hardware, runtime, and licenses.
- Experimental protocol: splits, baselines, metrics, statistical significance, and compute budget.
- Ethics and broader impacts.
- Human subjects, privacy, safety, and safeguards when applicable.
- LLM usage or AI-assistance disclosure when applicable.
- New assets: dataset/model/code documentation, hosting, maintenance, licenses, and consent.

For NeurIPS-style checklists, answer every item explicitly and cite the relevant paper section where possible.

## Build Check

Create `build_check.md` with:

- Build command tried.
- Whether TeX tools were available.
- Errors or warnings.
- Missing citations or references.
- Remaining action items.

Recommended full build:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Use the actual main `.tex` filename.

## Pre-Commit Check

Before committing or pushing:

- `git status --short`
- `git diff --cached --stat`
- Check generated image/PDF sizes.
- Verify no unresolved TODOs unless intentionally documented.
- Verify `.tex` citation keys exist in `.bib`.

Recommended commands:

```bash
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
```

Use the actual paths in the paper repository.
