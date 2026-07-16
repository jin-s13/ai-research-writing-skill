# Full-Paper Workflow

Use this state machine for full-paper generation, major revision, or submission preparation. Load `artifacts.md` with it. Do not skip a failed gate; weaken the claim or record a blocker.

## 1. Declare the Contract

- If an upstream system supplied `research_handoff.json`, load `research-handoff.md`, validate the handoff, and carry every blocker forward before creating paper state.
- Detect target venue, template, anonymity mode, main `.tex`, bibliography, page/checklist constraints, and paper stage.
- Create `paper_state.json`, one task packet, and `plan/progress.md`.
- Run `research_quality_gate.py` early so missing inputs are visible before drafting.

## 2. Inventory Evidence

- Inspect code, documentation, notes, logs, tables, notebooks, existing drafts, figures, and citations.
- Create a repository inventory and experiment inventory without duplicating an existing project overview.
- Record datasets, splits, seeds, baselines, metrics, uncertainty, compute, and missing evidence.

## 3. Fix the Story and Literature Position

- Load `paper-story.md`; define thesis, task boundary, gap, technical insight, contributions, claims to make, and claims to avoid.
- Load `literature-review.md` and `citation-workflow.md`; inventory close papers and baselines before Related Work prose.
- Build the initial claim-evidence map. Unsupported claims must be weakened, removed, or explicitly classified as claims to avoid.

## 4. First Draft Pass: Evidence-Bearing Core

Write a provisional title and abstract only to constrain scope, then draft in this order:

1. Method / System Design.
2. Experiments / Evaluation.
3. Results, ablations, failure analysis, and limitations.
4. Figures and tables tied to those sections.

Do not polish the provisional abstract as final copy. Let the completed evidence-bearing sections determine the final framing.

For long papers, use one bounded agent/model call per numbered block. Each call receives the paper story, claim map, relevant evidence, and completed preceding sections; it must not regenerate unrelated sections.

## 5. Second Draft Pass: Framing and Synthesis

1. Related Work from the literature matrix and verified corpus.
2. Introduction from the final gap, method, and evidence.
3. Conclusion from demonstrated results and limitations.
4. Rewrite the title and Abstract last.

Run a terminology pass and reverse-outline pass across the complete manuscript.

## 6. Produce Figure and Table Assets

- Load `figure-workflow.md` and `figure-spec.md`.
- Classify each asset as `evidence-result` or `concept-method` and record role, message, entities, layout, backend, source, and backup.
- Use deterministic plotting or LaTeX tables for numbers, axes, metrics, benchmarks, and comparisons.
- For overview, method, framework, pipeline, architecture, and teaser figures, use built-in image generation as the default paper asset. Inspect generated images before inclusion; regenerate or edit when labels or structure are wrong.
- Wire every required asset into LaTeX and write takeaway-driven captions.

## 7. Verify Citations

- Fetch structured metadata; do not write BibTeX from memory.
- Add concrete entries to `references.bib` and record provenance plus sentence-level relation in `citation_verification.md`.
- Run `check_citations.py`; for terminal stages, every cited key must have a verified record.

## 8. Review, Build, and Package

- Run two reviews: task/spec compliance, then skeptical paper-quality review.
- In the paper-quality review, use methodology, domain/positioning, and statistics/evidence lenses. Merge duplicate objections before revision.
- Convert high-risk objections into edits, experiments, limitations, or blockers.
- Revise targeted sections first. Avoid whole-paper regeneration unless the story itself changed; rerun numeric, citation, and build checks after every substantive revision.
- Run marker, citation, quality, venue, and build-log checks.
- Compile the actual LaTeX package with `record_build.py --run` before submission-ready so the command, log, tool version, exit code, and hashes are attested together.
- For submission, complete the venue checklist and `submission_readiness.md`, then follow `submission-packaging.md`.
- Update `plan/progress.md` with completed checks and remaining scientific risks before reporting completion.
