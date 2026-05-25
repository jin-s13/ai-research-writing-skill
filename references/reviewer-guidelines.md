# Reviewer Guidelines Reference

Use this to align a draft with how reviewers judge ML/AI/systems papers. It absorbs the practical reviewer-guideline material from `ml-paper-writing`.

## Universal Reviewer Dimensions

| Dimension | Reviewer asks | Author action |
|---|---|---|
| Quality / soundness | Are claims supported? Are methods and experiments correct? | Tie claims to evidence; document protocols. |
| Clarity | Can the reader understand and reproduce the work? | Define terms, keep flow, include details. |
| Significance | Does the result matter to the community? | Connect to a real gap and use meaningful tasks. |
| Originality | What is new or insightful? | State novelty type precisely. |
| Reproducibility | Can results be verified? | Provide code/data/settings/seeds/compute. |

Originality does not always require a new model. A new task, benchmark, system workflow, evaluation finding, or explanation can be original if it changes what the community can do or understand.

## Common Reviewer Concerns

- Main contribution is unclear or too incremental.
- Method modules lack motivation.
- Baselines are weak, missing, or unfair.
- Evaluation metrics do not match the claimed capability.
- Experiments are too easy or too narrow.
- Results are reported without variance or enough details.
- Claims in Abstract/Introduction exceed experiments.
- Limitations are obvious but unstated.
- Related work omits close papers or misstates task differences.

## Venue Tendencies

### NeurIPS / ICML / ICLR

- Strong story and clear technical insight matter.
- Experimental rigor and fair baselines are heavily scrutinized.
- Reproducibility and limitations are expected.
- LLM usage and ethics disclosures may matter depending on year and venue.

### ACL / NLP

- Limitations and ethics are central.
- Dataset, annotation, language scope, and human evaluation details matter.
- Claims about bias, language coverage, or human preference need careful support.

### Systems

- A working prototype, system design rationale, and end-to-end evaluation matter.
- Real workloads and deployment lessons can be as important as algorithmic novelty.
- Reviewers expect overhead, stress tests, breakdowns, and clear design boundaries.

## Review-Ready Section Checks

### Abstract

- Can the reviewer identify task, gap, contribution, and evidence in one pass?
- Are all strong words justified?

### Introduction

- Does the first page make the paper's novelty and importance obvious?
- Does it avoid the "naive baseline + small patch" framing?

### Method

- Is each module motivated by a challenge?
- Are inputs, outputs, invariants, and failure handling clear?

### Experiments

- Does each experiment answer a research question?
- Are baselines and metrics fair?
- Are ablations sufficient?

### Limitations

- Are scope constraints and failure modes stated honestly?
- Do limitations weaken any central claim?

## Rebuttal-Aware Writing

Before submission, imagine the top three reviewer criticisms and make sure the main paper already answers them. Good writing reduces rebuttal load.
