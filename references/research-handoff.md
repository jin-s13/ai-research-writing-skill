# Research-System Handoff

Use this when an upstream system has already completed research planning, experiments, or analysis and this skill should own paper writing from that point onward.

The upstream system must export evidence, not writing prompts. The skill remains the canonical source for story construction, drafting, figures, citations, review, revision, LaTeX, and completion gates.

## Handoff Contract

Create `research_handoff.json` using `research-handoff.schema.json`. Paths are relative to the handoff project.

```json
{
  "schema_version": "ai-research-writing/research-handoff-v1",
  "research_question": "Does method X improve metric Y under condition Z?",
  "paper_type": "empirical ML paper",
  "target_venue": "ICML",
  "quantitative": true,
  "artifacts": {
    "project_inventory": "evidence/project_inventory.md",
    "analysis": "evidence/analysis.md",
    "decision": "evidence/decision.md",
    "experiment_inventory": "evidence/experiment_inventory.md",
    "numeric_evidence": "numeric_evidence.json",
    "literature_inventory": "literature/paper_inventory.md",
    "figure_inventory": "figures/figure_inventory.md"
  },
  "blockers": []
}
```

For quantitative work, `experiment_inventory` and numeric-evidence v2 are required. A handoff may retain blockers for inspection, but full-paper drafting must use `--require-unblocked`. Exploratory partial writing must carry every blocker into `paper_state.json` and weaken affected claims.

Validate before drafting:

```bash
python3 scripts/check_research_handoff.py /path/to/handoff-project --require-unblocked
```

## Ownership Boundary

The upstream system owns the truth of exported evidence and stable file paths. It must not summarize away negative runs, failed conditions, missing baselines, uncertainty, or contradictory outcomes.

This skill owns all manuscript decisions after handoff. It creates `paper_state.json`, the paper story, claim map, prose, figures/tables, citation records, reviews, LaTeX, and build record. Never copy upstream writing prompts into the skill contract.

## Acceptance Procedure

1. Validate the handoff and inspect every declared artifact.
2. Reconcile contradictions between analysis, decision, raw evidence, and blockers.
3. Create the paper project contract and copy blockers without weakening them.
4. Build the story and claim map from evidence, not from an upstream proposed title.
5. Continue with `workflow.md` from the evidence-bearing core draft.
