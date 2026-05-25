# Reviewer Self-Review Reference

Use this reference before major revisions and before submission. The goal is to find rejection risks before reviewers do and to produce an author-facing diagnosis, not only automatic edits.

Reviewer self-review has two outputs:

1. **Author analysis**: explain the paper's strengths, weaknesses, likely reviewer objections, and trade-offs in a form the author can evaluate.
2. **Revision plan**: convert the highest-impact risks into edits, experiments, citation work, limitations, or claims to weaken.

Do not silently "fix" a paper in ways that hide scientific trade-offs from the author. If a risk requires new experiments, different framing, or a weaker claim, state that clearly.

## Five-Dimension Review

Score each dimension as `pass`, `needs revision`, or `needs evidence`. Use `references/reviewer-guidelines.md` for venue-facing reviewer expectations and score calibration.

| Dimension | Reviewer question | Common failure |
|---|---|---|
| Contribution | What is new and why does it matter? | The paper reads like an implementation report. |
| Writing clarity | Can the reviewer restate the paper after reading the introduction? | The narrative is a list of modules. |
| Experimental strength | Do the experiments support the main claims? | Main claims rely on partial or cherry-picked numbers. |
| Evaluation completeness | Are baselines, metrics, and splits fair? | Missing ablations, unclear settings, or weak baselines. |
| Method soundness | Are design choices justified and reproducible? | The method depends on undocumented prompts, heuristics, or hidden manual steps. |
| Responsibility | Are limitations, data use, ethics, and release claims handled? | Obvious risks, data issues, or limitations are unstated. |

## Acceptance Signals

A paper becomes reviewer-ready when:

- contribution type is explicit: task, method, system, benchmark, dataset, analysis, or finding;
- the main result is supported by fair baselines and suitable metrics;
- ablations cover the key design choices;
- the first page makes novelty and significance clear;
- limitations are honest and do not contradict the central claim;
- code/data/supplementary claims are anonymized, citable, and consistent with venue rules.

## Reviewer-Review Simulation

Before finalizing, write a short simulated review:

```text
Summary:
Strengths:
Weaknesses:
Key reason for accept/reject:
Questions for authors:
Actionable suggestions:
Confidence:
```

Rules:

- The summary should be something authors would recognize as accurate.
- Weaknesses must cite specific sections, claims, experiments, missing baselines, or unclear terms.
- If the simulated review sounds generic, the paper story is not yet concrete enough.
- If the simulated reviewer cannot name the main evidence, strengthen Abstract/Introduction and the results presentation.

## Author-Facing Reviewer Analysis

Create or update `reviewer_analysis.md` when doing a major review or pre-submission audit:

```text
# Reviewer Analysis

## Executive Summary
Current likely reviewer stance:
Strongest part of the paper:
Highest rejection risk:
Recommended next decision:

## Strengths
- Strength:
- Evidence:
- Why reviewers may value it:

## Major Risks
| Risk | Why reviewers may care | Evidence status | Severity | Recommended action |
|---|---|---|---|---|

## Claim and Evidence Gaps
| Claim | Current evidence | Reviewer concern | Recommendation |
|---|---|---|---|

## Author Decisions Needed
- Decision:
- Options:
- Trade-off:
- Recommendation:

## Revision Priorities
1. Must fix before submission:
2. Should fix if time allows:
3. Safe to leave as limitation:
```

Use this report to help the author decide what to do. Keep it analytical and specific; do not turn it into a generic checklist.

## Rejection-Risk Audit

Create `submission_readiness.md` or include this in `reviewer_analysis.md` with:

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
- Would a reviewer say "this has been done before"? If so, which exact prior work must be distinguished?
- Would a reviewer ask for a substantial new experiment that cannot fit into rebuttal? If so, address it before submission or weaken the claim.
- Are supplementary details necessary for understanding the main claim? If yes, move the critical detail into the main paper.
- Are dataset, code, prompt, or model assets cited and anonymized where required?

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
- Are tuning budgets, pretraining data, compute, and implementation details comparable across methods?
- If a requested comparison would require reimplementing closed or unavailable work, is that limitation explained?

## Responsibility Audit

Check the paper for review-process and policy risks:

- **Limitations**: Are scope restrictions and failure modes explicit?
- **Data assets**: Are datasets, annotations, licenses, and withdrawn/sensitive data issues handled?
- **Human subjects / personal data**: Is consent, IRB, or equivalent ethics handling stated when relevant?
- **Societal impact**: Are plausible negative uses or harms acknowledged when relevant?
- **LLM usage**: Is author-side LLM assistance disclosed if the venue requires it?
- **Anonymity**: Are author names, acknowledgments, repository links, file metadata, and supplementary assets anonymized for review?
- **Supplementary material**: Does it clarify rather than replace or materially change the main submission?

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
| Policy / ethics risk | Responsibility | Add disclosure, anonymize asset, or remove unsupported release claim. | |

## Rebuttal Readiness

Before submission, prepare concise answers to likely reviewer questions:

1. What is the closest prior work and why is this different?
2. Why are the chosen baselines fair?
3. Which result directly supports the central claim?
4. What happens in failure cases or harder subsets?
5. Which limitation is real but does not invalidate the main claim?

If any answer requires a large new experiment, do not assume rebuttal can save it. Revise the paper, add the experiment, or weaken the claim before submission.

## Final Self-Review Statement

Before finalizing, write:

```text
The paper is currently strongest on ...
The highest remaining reviewer risk is ...
The main evidence supporting the central claim is ...
Claims intentionally weakened or removed:
Submission-blocking issues:
```
