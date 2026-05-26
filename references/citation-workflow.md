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

This workflow must produce concrete files when possible. For full-paper work, citation completion means `references.bib` has been created or updated, `citation_verification.md` records the checked source, and important accessible papers are saved or explicitly marked as `metadata-only`/`needs-access` in the literature inventory.

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

## Source Reliability Tiers

Prefer structured, authoritative sources before broad discovery tools:

1. **Tier 1: authoritative structured metadata**: DOI/Crossref, arXiv, PubMed/PMID when applicable, publisher/proceedings pages, official software or dataset citation metadata.
2. **Tier 2: scholarly discovery APIs**: Semantic Scholar, OpenAlex, domain preprint servers, and citation graph services. Use these for discovery and cross-checking, then verify against Tier 1 when possible.
3. **Tier 3: unstable or access-limited search**: Google Scholar, institutional indexes, Web of Science/Scopus pages, CNKI/万方 manual search. Use only as last resort and mark results as potentially incomplete.

For citation verification, route from strongest identifier to weaker search: DOI -> arXiv ID/PMID -> exact title -> title plus first author -> method/task query.

## Segment-to-Citation Workflow

When adding citations to prose, do not search the whole paragraph as one vague query:

1. Split text into citable claims or short segments.
2. For each segment, extract the exact claim and its boundary.
3. Generate 2-4 English search queries: precise title/term query, synonym query, broader background query, and method/dataset query when relevant.
4. Search candidates using the source tiers above.
5. Assign support status before citing: `direct`, `partial`, `background`, `contrast`, `software`, `weak`, or `metadata-only`.
6. Only cite `direct`, `contrast`, or `software` for strong claims. Use `partial` or `background` only for scoped context sentences.

Never cite a `metadata-only` candidate as claim support before checking the abstract, publisher page, or paper text.

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

Do not treat a list of search results as a downloaded corpus. If the paper is open access or otherwise accessible, save the official PDF or stable local copy. If it cannot be saved, keep the official URL and status in the inventory so the missing local copy is visible.

## BibTeX Retrieval Output

When adding citations:

1. Create `references.bib` if it does not exist.
2. Fetch BibTeX or structured metadata from DOI/Crossref, arXiv, publisher pages, Semantic Scholar, OpenAlex, or official docs.
3. Normalize only the key and obvious formatting; do not invent missing metadata.
4. Add the entry to `references.bib`.
5. Record the source URL/API and claim relation in `citation_verification.md`.

If no authoritative BibTeX is available, use a visible placeholder key and record the blocker. Do not leave citations only in prose or only in the verification table.

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
4. Add or update the corresponding `references.bib` entry.
5. If no source supports the sentence, revise the sentence.
6. Run `scripts/check_citations.py`.

## Common Failure Modes

- Real authors with fabricated titles.
- Wrong year for arXiv versus proceedings.
- Citing a survey for a specific technical claim from the original paper.
- Using software repository metadata as evidence for a scientific result.
- Citing concurrent work as a baseline when task definitions are not comparable.
