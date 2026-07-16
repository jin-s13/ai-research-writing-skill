# Citation Verification Workflow

Use this when finding, adding, or repairing citations. Verification has three separate dimensions; never collapse them into one `verified` label:

1. **Existence and metadata**: the work and its bibliographic fields are real.
2. **BibTeX integrity**: LaTeX keys resolve to one structurally valid entry.
3. **Claim support**: the abstract or paper text supports the attached sentence.

`check_citations.py` covers only the second dimension and declared-input completeness.

## Source Routing

Resolve from the strongest identifier available:

| Input | Primary verification | Secondary cross-check |
|---|---|---|
| DOI | DOI resolver, publisher/proceedings, Crossref or the relevant registration agency | OpenAlex |
| arXiv ID | Official arXiv API/page | OpenAlex or Semantic Scholar |
| PMID/PMCID | PubMed/PMC | OpenAlex |
| Exact title only | OpenAlex or Semantic Scholar discovery | DOI/arXiv/publisher after identification |
| Software/dataset | Official repository, docs, release, dataset card, or CITATION metadata | OpenAlex only when a scholarly work also exists |

Official references:

- Crossref REST/content negotiation: `https://www.crossref.org/documentation/retrieve-metadata/`
- OpenAlex API: `https://developers.openalex.org/api-reference/works`
- arXiv API: `https://info.arxiv.org/help/api/`
- Semantic Scholar Academic Graph API: `https://api.semanticscholar.org/api-docs/`

## OpenAlex: Recommended Role

OpenAlex is useful for broad scholarly discovery, exact-title search, DOI/PMID/OpenAlex identifier resolution, citation graphs, authorship/institution normalization, open-access locations, and batched DOI lookup. Its current API uses a free API key and credit-based limits; record API errors and rate-limit status rather than silently returning an empty result.

Do not use OpenAlex as the sole authority when a DOI, arXiv record, official proceedings page, or publisher record exists. OpenAlex aggregates metadata, so venue/version fields can differ, abstracts or identifiers can be missing, and it does not establish sentence-level claim support. Use it as resolver and cross-check, not as the final source of truth.

## Six-Step Procedure

1. **Segment** the manuscript into individual citable claims.
2. **Discover** candidates using exact title, method/task, baseline/benchmark, and author queries.
3. **Resolve** DOI, arXiv ID, PMID, or stable official software/dataset identity.
4. **Verify metadata** against the primary source; use a second source when fields conflict.
5. **Read for support** and classify the sentence relation.
6. **Record** BibTeX, provenance, relation, access status, and unresolved conflicts.

Do not cite a search-result record before resolving it to a primary identifier or official artifact.

## Claim Relations

Use one status per citation-sentence pair:

- `direct`: directly establishes the sentence.
- `background`: motivates the area but not the specific claim.
- `contrast`: accurately describes the compared setting.
- `software`: documents a tool, dataset, model, or repository.
- `partial`: supports only a narrower statement; revise the sentence.
- `weak`: does not support the sentence; remove or replace it.
- `metadata-only`: existence checked, content not inspected; cannot support a claim yet.

Strong technical or comparative claims require `direct`, `contrast`, or `software` as appropriate.

## Durable Records

For each cited key, store at least:

```markdown
| Key | Identifier | Primary source | Cross-check | Claim supported | Relation | Status | Checked at |
|---|---|---|---|---|---|---|---|
| author_2026_work | doi:... | Crossref/publisher URL | OpenAlex URL | Exact scoped sentence | direct | verified | 2026-07-16 |
```

Use these terminal statuses:

- `verified`: scholarly metadata and claim relation checked.
- `software-doc`: official software/dataset artifact checked.
- `repository-verified`: official repository identity checked for project positioning only.

Use visible non-terminal statuses such as `metadata-only`, `conflict`, `needs-access`, or `placeholder`. Terminal paper stages must fail while any cited key remains non-terminal.

Create `citation_requests.json` from `citation-requests.schema.json`, with a DOI or arXiv identifier and one or more sentence-level support records for every scholarly citation. Then run:

```bash
python3 scripts/verify_citations.py /path/to/paper-project --mailto you@example.org
python3 scripts/check_citation_lock.py /path/to/paper-project
```

The verifier uses Crossref for Crossref DOI metadata, DataCite after a Crossref 404, and the official arXiv API for arXiv identifiers. Set `OPENALEX_API_KEY` or pass `--openalex-api-key` for a secondary comparison. OpenAlex conflicts are blocking and never replace an available primary record. `citation_lock.json` stores provider URLs, normalized metadata, checked time, request and claim-support digests, optional cross-check data, and an explicit status. Network errors, 404s, conflicts, incomplete metadata, and rate limits are non-terminal.

## BibTeX Rules

- Retrieve BibTeX through DOI content negotiation, arXiv, publisher/proceedings, or structured metadata; do not type it from memory.
- Keep stable lowercase ASCII keys such as `vaswani_2017_attention`.
- Normalize formatting only; never invent missing authors, venue, year, pages, DOI, or URL.
- Distinguish preprint and proceedings versions. Cite the version actually supporting the sentence.
- Run `check_citations.py` after every bibliography change.

## Local Corpus and Access

Save close papers under `literature/papers/` only when access and licensing permit. Record every important candidate in the paper inventory with official URL, local path, version, and `available`, `metadata-only`, or `needs-access` status. Never commit copyrighted/private downloads to a public repository without permission.

## Failure Rules

- Conflicting metadata: show both records and resolve against the primary source.
- No primary identifier: keep `metadata-only` until the official artifact is inspected.
- No support for the sentence: revise the sentence or remove the citation.
- API unavailable or rate-limited: record the failure; do not treat an empty response as no matching literature.
- Placeholder in a final draft: fail the citation gate.
