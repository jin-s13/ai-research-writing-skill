# Citation Workflow Reference

Use this reference when finding, adding, or repairing citations. Never generate BibTeX from memory; always verify metadata and claim support.

## Non-Negotiable Rule

Do not invent citations. A fluent but false bibliography is an academic integrity failure. If a citation cannot be verified, mark it as a placeholder or remove the claim.

## Six-Step Verified Citation Workflow

```text
1. SEARCH   -> find candidates from authoritative scholarly sources
2. VERIFY  -> confirm title/authors/year/DOI/arXiv in reliable metadata
3. SAVE     -> save important papers locally when access and licensing permit
4. RETRIEVE -> fetch BibTeX from DOI, arXiv, publisher, or official metadata
5. VALIDATE -> check that the cited work supports the sentence-level claim
6. RECORD  -> add .bib entry and log verification in citation_verification.md
```

## Source Selection

| Need | Preferred source |
|---|---|
| ML/AI paper search | Semantic Scholar, OpenAlex, arXiv |
| DOI metadata | Crossref, DOI content negotiation |
| Preprint metadata | arXiv API or arXiv page |
| Publisher version | official proceedings or publisher page |
| Software/library citation | official docs, release page, repository citation metadata |
| Dataset citation | dataset card, official dataset page, paper, or license page |

Google Scholar has no official public API. Avoid workflows that depend on scraping it.

## Query Strategy

Search in this order:

1. Exact known title.
2. Method name + task/domain.
3. Baseline name + benchmark/task.
4. Author name + keyword when title is uncertain.
5. Existing `.bib` keys and citations in the codebase.

Record failed searches when they affect the paper story.

## Local Paper Corpus

For Related Work or positioning tasks, maintain a local literature corpus before drafting prose:

- Save important papers in `literature/papers/` when access and licensing permit.
- Record all important candidates in `literature/paper_inventory.md`, including official URL, local path, status, and relevance.
- Create short notes under `literature/notes/` for close works and baselines before using them for contrast.
- Do not commit copyrighted PDFs or private downloads to an open-source repository unless redistribution is allowed and the user explicitly wants them included.

Use `references/literature-review.md` for the full corpus, matrix, and positioning workflow.

## Metadata Verification

A citation is verified when:

- title, first author, year, and venue/preprint source are consistent;
- DOI or arXiv ID is present when applicable;
- BibTeX was fetched or derived from an authoritative source;
- the citation supports the claim it is attached to.

Use two sources when metadata conflicts or the work is obscure.

## BibTeX Key Convention

Use stable, readable keys:

```text
firstauthor_year_shorttitle
```

Examples:

```text
vaswani_2017_attention
kirillov_2023_segment
```

Keep keys lowercase, ASCII, and stable once used in the paper.

## Claim Validation

For each citation sentence, classify the support:

- `direct`: paper directly supports the claim.
- `background`: paper motivates the area only.
- `contrast`: paper is being contrasted.
- `software`: citation documents a tool/library/dataset.
- `weak`: citation does not support the claim.

Strong claims require `direct`, `contrast`, or `software` support depending on sentence type.

## `citation_verification.md` Template

```markdown
| Key | Source checked | Claim supported | Relation | Status | Notes |
|---|---|---|---|---|---|
| author_2026_short | DOI / arXiv / publisher URL | Sentence or claim | direct | verified | ... |
```

Status values:

- `verified`
- `software-doc`
- `placeholder`
- `needs-license-check`
- `removed`

## Placeholder Policy

Use visible placeholders only when the draft needs to preserve intent:

```latex
\cite{PLACEHOLDER_author_year_verify}
```

Then record the placeholder in `citation_verification.md` and tell the user. Do not leave hidden placeholder citations in a final draft.

## Citation Repair Procedure

When a citation key is missing or suspicious:

1. Search the key in `.bib`, `.tex`, notes, and downloaded PDFs.
2. Search the title or nearby prose online/API if network tools are available.
3. Replace with a verified primary source.
4. If no source supports the sentence, revise the sentence.
5. Run `scripts/check_citations.py`.

## Common Failure Modes

- Real authors with fabricated titles.
- Wrong year for arXiv versus proceedings.
- Citing a survey for a specific technical claim from the original paper.
- Using software repository metadata as evidence for a scientific result.
- Citing concurrent work as a baseline when task definitions are not comparable.
