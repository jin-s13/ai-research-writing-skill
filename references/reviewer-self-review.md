# Reviewer Self-Review Reference

Use this reference before major revisions and before submission. The goal is to find rejection risks before reviewers do.

## Five-Dimension Review

Score each dimension as `pass`, `needs revision`, or `needs evidence`.

| Dimension | Reviewer question | Common failure |
|---|---|---|
| Contribution | What is new and why does it matter? | The paper reads like an implementation report. |
| Writing clarity | Can the reviewer restate the paper after reading the introduction? | The narrative is a list of modules. |
| Experimental strength | Do the experiments support the main claims? | Main claims rely on partial or cherry-picked numbers. |
| Evaluation completeness | Are baselines, metrics, and splits fair? | Missing ablations, unclear settings, or weak baselines. |
| Method soundness | Are design choices justified and reproducible? | The method depends on undocumented prompts, heuristics, or hidden manual steps. |

Use `references/reviewer-guidelines.md` for venue-facing reviewer expectations and score calibration.

## Acceptance Signals

A paper becomes reviewer-ready when:

- contribution type is explicit: task, method, system, benchmark, dataset, analysis, or finding;
- the main result is supported by fair baselines and suitable metrics;
- ablations cover the key design choices;
- the first page makes novelty and significance clear;
- limitations are honest and do not contradict the central claim.

## Rejection-Risk Audit

Create `submission_readiness.md` with:

1. **Paper thesis**.
2. **Top five reviewer objections**.
3. **Evidence that addresses each objection**.
4. **Remaining gaps**.
5. **Planned fix**: edit, experiment, limitation, or remove claim.
6. **Severity**: high, medium, low.

High-severity unresolved issues should block a final submission response unless the user explicitly accepts the risk.

## Adversarial Questions

Ask these as a skeptical reviewer:

- What exactly is the task? Is it defined more clearly than prior work?
- Is the claimed novelty a method, system, benchmark, dataset, workflow, or evaluation protocol?
- Could a reviewer say the method is just prompt engineering? If so, what execution, verification, representation, or evaluation contribution makes it more than that?
- Are the strongest claims in the Abstract backed by the strongest experiments?
- Are negative or mixed results acknowledged?
- Are baselines comparable under the same input/output assumptions?
- Are evaluation metrics aligned with what the paper says it cares about?
- Are examples cherry-picked, or do they illustrate systematic behavior?
- Are any citations being used as decoration rather than evidence?
- Are limitations obvious but unstated?

## Claim Audit

For each Abstract and Introduction claim:

```text
Claim:
Evidence:
Citation or result:
Risk:
Revision:
Status: keep / weaken / remove / needs experiment
```

Rules:

- Strong claims need direct evidence.
- Broad capability claims need task boundaries.
- "First", "general", "unified", "end-to-end", "robust", and "state-of-the-art" require extra scrutiny.
- If a term can be misunderstood, define it near first use.

## Experiment Audit

For each experiment:

- What research question does it answer?
- Which main paper claim does it support?
- Are baselines fair and named?
- Are metrics defined with direction?
- Are variance, seeds, or repeats needed?
- Are failure cases analyzed?
- Could a reviewer ask for a missing ablation?
- Is the caption sufficient for standalone interpretation?

## Writing Audit

For each section:

- Does the opening sentence state the section's role?
- Does each paragraph have one message?
- Are transitions based on logic rather than chronology?
- Are method names used consistently?
- Does the paper avoid overloading the reader with implementation detail before motivation?
- Is Figure 1 introduced before method details become hard to follow?

## Reviewer-Ready Revision Plan

Convert risks into actions:

| Risk | Fix type | Concrete action | Owner/status |
|---|---|---|---|
| Unsupported claim | Edit | Weaken claim in Abstract and Introduction. | |
| Missing evidence | Experiment | Add ablation on ... | |
| Confusing method | Writing/Figure | Add overview diagram and method invariant. | |
| Weak citation | Citation | Replace with verified primary source. | |
| Scope gap | Limitation | Add limitation paragraph. | |

## Final Self-Review Statement

Before finalizing, write:

```text
The paper is currently strongest on ...
The highest remaining reviewer risk is ...
The main evidence supporting the central claim is ...
Claims intentionally weakened or removed:
Submission-blocking issues:
```
