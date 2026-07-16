# Artifact Contract

Create artifacts in the target paper project, not in this skill repository. Use the smallest set that preserves evidence and verification.

## Machine State

Full-paper and submission modes require `paper_state.json`:

```json
{
  "schema_version": "ai-research-writing/paper-state-v1",
  "mode": "full-paper",
  "stage": "drafting",
  "target_venue": "ICML 2026",
  "main_tex": "paper/main.tex",
  "bibliography": "paper/references.bib",
  "required_artifacts": ["experiment_inventory.md"],
  "blockers": [],
  "build": {
    "status": "not-run",
    "command": "tectonic main.tex",
    "pdf": "paper/main.pdf",
    "external_inputs": [],
    "input_sha256": "",
    "pdf_sha256": ""
  }
}
```

Use `stage: complete` or `submission-ready` only after checks pass. Drafts may record an existing PDF as `artifact-only`; before declaring `submission-ready`, execute the declared build command and record its log, exit code, tool version, source hash, and PDF hash:

```bash
python3 /path/to/skill/scripts/record_build.py /path/to/paper-project --run
python3 /path/to/skill/scripts/research_quality_gate.py /path/to/paper-project
```

The complete JSON schema is `paper-state.schema.json`.

## Core Artifacts

| Concern | Artifact |
|---|---|
| Scope and execution | `plan/task-packets/<task>.md`, `plan/progress.md` |
| Repository and experiments | `project_inventory.md` or existing overview; `experiment_inventory.md` when experiments exist |
| Quantitative provenance | `numeric_evidence.json` for numbers used in evidence-sensitive sections |
| Story and claims | `paper_story.md`, `claim_evidence_map.md` |
| Literature | `literature/paper_inventory.md`, `literature/related_work_matrix.md`, `literature/positioning.md` |
| Citations | `references.bib`, `citation_verification.md` |
| Figures and tables | `figures/figure_plan.md`, specs/prompts, generated assets, deterministic plot/table sources |
| Review | `reviewer_analysis.md` or `plan/review/` reports |
| Build and submission | `build_check.md`, plus `submission_readiness.md` in submission mode |

Do not commit copyrighted or private paper PDFs unless redistribution is permitted and the user explicitly requests it. Record inaccessible papers as `metadata-only` or `needs-access` rather than silently omitting them.

## Minimal Sets

| Request | Minimum durable output |
|---|---|
| Story | `paper_story.md` |
| Section revision | revised section plus claim/evidence notes |
| Related Work | inventory, matrix, positioning, citation updates |
| Figure work | plan/spec, final asset, source or prompt |
| Citation repair | `references.bib`, `citation_verification.md` |
| Full paper | machine state plus applicable core artifacts above |
| Submission | full-paper set, checklist, `submission_readiness.md`, recorded build |

When an upstream research system supplies evidence, validate `research_handoff.json` using `research-handoff.md` before creating the paper artifacts. For quantitative papers, add `numeric_evidence.json` to `required_artifacts`; the quality gate validates it automatically when present. Its schema is `numeric-evidence.schema.json`.
