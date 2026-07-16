# Build Check

## Command

```bash
python3 scripts/fetch_template.py icml2026 \
  --output examples/paper-about-ai-research-writing-skill/paper/.venue-template
cd examples/paper-about-ai-research-writing-skill/paper
tectonic -Z search-path=.venue-template main.tex
cd ../../../
python3 examples/paper-about-ai-research-writing-skill/evaluation/run_evaluation.py
python3 scripts/record_build.py examples/paper-about-ai-research-writing-skill
python3 scripts/research_quality_gate.py examples/paper-about-ai-research-writing-skill
```

## Result

Verified with Tectonic 0.16.9. The command produced `paper/main.pdf` using the official ICML 2026 archive identified in `paper_state.json`. The state records SHA-256 hashes for the paper input graph, external template archive, and resulting PDF, so source or declared-template changes invalidate the recorded build.

Known warnings:

- Bibliography URLs can produce harmless underfull-line warnings depending on the TeX engine.
- Narrow ICML table columns can produce harmless underfull-line warnings in descriptive comparison tables.
- Image-generated figures increase PDF size; the compiled demo PDF is about 2 MB.

## Expected Files

The command should produce `main.pdf` from:

- `main.tex`
- `.venue-template/` fetched from the official archive recorded in `paper_state.json`
- `figures/teaser_imagegen.png`
- `figures/overview_imagegen.png`
- `figures/method_overview.tex`
- `tables/repository_evidence.tex`
- `tables/related_projects.tex`
- `references.bib`

## Remaining Risks

- The paper is an example package, not a submitted manuscript.
- Related project citations are repository citations, not peer-reviewed paper citations.
- The example does not include an empirical user study or benchmark.
- Image-generated overview figures are conceptual and must not be used as numerical evidence.
