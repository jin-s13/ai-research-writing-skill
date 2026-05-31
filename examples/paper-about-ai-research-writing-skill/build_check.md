# Build Check

## Command

```bash
cd examples/paper-about-ai-research-writing-skill/paper
tectonic main.tex
```

## Result

Verified with the bundled Tectonic engine. The command produced `paper/main.pdf`.

Known warnings:

- Bibliography URLs can produce harmless underfull-line warnings depending on the TeX engine.

## Expected Files

The command should produce `main.pdf` from:

- `main.tex`
- `figures/architecture.tex`
- `tables/repository_evidence.tex`
- `tables/related_projects.tex`
- `references.bib`

## Remaining Risks

- The paper is an example package, not a submitted manuscript.
- Related project citations are repository citations, not peer-reviewed paper citations.
- The example does not include an empirical user study or benchmark.
