# Literature Review Reference

Use this reference before writing Related Work or when the paper's positioning is uncertain. Related Work should be based on a verified local literature corpus, not on memory or one-off search snippets.

## Core Principle

Important papers should be saved, verified, and summarized before they are used to position the work. Do not cite or contrast a paper unless its title, authors, venue/year, and claim relevance have been checked.

## Literature Corpus Artifacts

For full-paper tasks, create or update:

- `literature/paper_inventory.md`: all important candidate papers, metadata, local file path or URL, status, and relevance.
- `literature/related_work_matrix.md`: lines of work, representative papers, what they solve, what they miss, and how this paper relates.
- `literature/positioning.md`: closest works, task differences, contribution boundary, and claims to avoid.
- `literature/papers/`: local copies of important papers when access and licensing permit.
- `literature/notes/`: short paper notes for close papers or baselines.

Do not commit copyrighted PDFs or private downloads unless the user explicitly wants that and redistribution is allowed. For open-source repositories, prefer storing metadata, official URLs, notes, and BibTeX while keeping downloaded PDFs local or gitignored.

## Paper Inventory Template

```markdown
| Key | Title | Year/Venue | Local file / URL | Role | Status | Notes |
|---|---|---|---|---|---|---|
| author_2024_short | ... | ... | literature/papers/...pdf | close work / baseline / background / dataset | downloaded / metadata-only / needs read | ... |
```

Status values:

- `downloaded`
- `metadata-only`
- `read`
- `summarized`
- `verified-citation`
- `needs-access`
- `not-relevant`

## Paper Note Template

For close works and baselines, create a compact note:

```markdown
# [Paper Title]

## Bibliographic Metadata
- Key:
- Title:
- Authors:
- Venue / year:
- DOI / arXiv / URL:
- Local file:

## Problem Setting
- Input:
- Output:
- Assumptions:
- Evaluation setting:

## Core Idea

## Evidence
- Datasets:
- Baselines:
- Metrics:
- Main results:

## Relation to This Paper
- Same task?
- Same input/output assumptions?
- What it solves:
- What it does not cover:
- How we should cite it:
- Claims we must avoid:
```

## Related Work Matrix

Before writing Related Work, create `literature/related_work_matrix.md`:

```markdown
| Line of work | Representative papers | What they solve | What they do not cover | How we relate | Citation role |
|---|---|---|---|---|---|
| ... | ... | ... | ... | background / contrast / baseline / concurrent |
```

Use this matrix to prevent citation soup and strawman contrasts.

## Positioning Analysis

Create `literature/positioning.md` for author-facing decisions:

```markdown
# Positioning

## Closest Works
| Paper | Similarity | Difference | Risk if not discussed |
|---|---|---|---|

## Our Position
- Task boundary:
- Main distinction:
- Evidence supporting distinction:
- Claims to make:
- Claims to be careful about:
- Claims to avoid:

## Related Work Paragraph Plan
1. Line of work:
2. Message:
3. Representative citations:
4. Gap relative to this paper:
```

## Workflow

1. Search from known titles, existing `.bib`, paper lists, baselines, benchmarks, and close method names.
2. Download or save official accessible copies of important papers when permitted.
3. Verify metadata and create stable BibTeX keys.
4. Read and summarize close works before contrasting them.
5. Build the related work matrix and positioning analysis.
6. Only then draft Related Work paragraphs.

## Writing Rules

- Group by research problem, not chronology.
- Cite representative papers for each line of work.
- Use primary sources for specific technical claims.
- Treat concurrent work calmly and precisely.
- If a close work has a different task definition, state the difference without making it look weak.
- Do not claim novelty by ignoring papers that solve a nearby problem.
