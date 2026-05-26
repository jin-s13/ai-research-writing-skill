# Reviewer Guidelines Reference

Use this to align a draft with how reviewers judge ML/AI/CV/NLP papers.

## Core Reviewer Questions

Reviewers ultimately ask whether the paper brings enough reliable value to the community. Before submission, make sure the draft answers:

1. **What problem or question does the paper tackle?**
2. **Is the approach well motivated and placed in the literature?**
3. **Do the experiments, theory, analysis, or artifacts support the claims?**
4. **What is significant or useful about the contribution?**

Lack of state-of-the-art numbers is not by itself a rejection reason. A paper can be strong through a new task, benchmark, workflow, finding, explanation, dataset, or careful negative result if it contributes new knowledge and supports its claims.

## Universal Review Dimensions

| Dimension | Reviewer asks | Author action |
|---|---|---|
| Originality | What is new, and how is it different from prior work? | State novelty type precisely; cite close work and explain task/assumption differences. |
| Quality / soundness | Are methods, theory, and experiments technically correct? | Tie every strong claim to evidence; document protocols and assumptions. |
| Clarity | Can an expert understand and reproduce the work? | Define terms, organize sections by logic, and include enough implementation detail. |
| Significance | Will the community use, build on, or learn from this result? | Connect the contribution to a real gap, use meaningful tasks, and state the takeaway early. |
| Reproducibility | Can results be checked? | Provide code/data/settings/seeds/compute, or clearly state what cannot be released and why. |
| Ethics / responsibility | Are risks, data use, and human-subject issues handled? | Discuss limitations, data licenses, consent/IRB when relevant, and negative societal impact. |

## Common Reviewer Concerns

- Main contribution is unclear, too incremental, or reads like an implementation report.
- Method modules lack motivation or are introduced before the problem is clear.
- Baselines are weak, missing, unfair, or use different input/output assumptions.
- Evaluation metrics do not match the capability claimed in the paper.
- Experiments are too easy, too narrow, or lack ablations and failure analysis.
- Results are reported without variance, seeds, repeated runs, or tuning details when needed.
- Claims in Abstract/Introduction exceed the experiments.
- Limitations are obvious but unstated.
- Related work omits close papers, overstates novelty, or misstates task differences.
- Data, code, prompts, supplementary material, or linked assets are not anonymized or not citable.

## Constructive Specificity Standard

A reviewer-quality objection should be specific enough that an author can act on it. Write the paper so reviewers do not need to guess:

- If novelty depends on prior work, name the closest papers and explain the technical difference.
- If writing may be unclear, point to the exact section, term, figure, or missing definition in your own self-review.
- If a baseline is omitted, explain whether it is unavailable, incomparable, too recent, or out of scope.
- If supplementary material contains essential details, reference it clearly from the main paper.
- If a limitation or ethics issue exists, disclose it honestly; many venues reward transparency rather than penalize it.

## Venue Tendencies

### NeurIPS / ICML / ICLR

- Strong story and clear technical insight matter.
- Experimental rigor, fair baselines, and claim support are heavily scrutinized.
- Reviewers often evaluate originality, quality, clarity, significance, reproducibility, limitations, and ethics together.
- OpenReview-style venues reward papers that can survive public clarification and discussion.
- Rebuttal should clarify, correct misunderstandings, and provide small additional evidence, not introduce a substantially different paper.

### CVPR / ICCV / ECCV

- Visual task definition, dataset protocol, evaluation metric, and qualitative examples must be precise.
- Dataset and code assets should be cited like papers when used.
- Dataset contributions need a credible release plan; private datasets cannot be claimed as public scientific assets.
- Personal data, human subjects, withdrawn datasets, or sensitive applications need careful handling.
- Supplementary material can clarify details, but should not contain an improved or materially changed version of the submission.

### ACL / NLP

- Limitations and ethics are central.
- Dataset, annotation, language scope, and human evaluation details matter.
- Claims about bias, language coverage, safety, or human preference need careful evidence.
- Prompt, model, decoding, and annotation details should appear where reproducibility requires them.

## Review-Ready Section Checks

### Abstract

- Can the reviewer identify task, gap, contribution, and evidence in one pass?
- Are all strong words justified?
- Does the abstract avoid implying SOTA, generality, robustness, or firstness without direct evidence?

### Introduction

- Does the first page make the paper's novelty and importance obvious?
- Does it avoid the "naive baseline + small patch" framing?
- Does it state the closest gap and the technical reason that gap exists?

### Method

- Is each module motivated by a challenge?
- Are inputs, outputs, invariants, and failure handling clear?
- Can a reviewer distinguish the scientific idea from implementation details?

### Experiments

- Does each experiment answer a research question?
- Are baselines, splits, metrics, tuning, seeds, and compute fair and documented?
- Are ablations and failure cases sufficient to support the design choices?
- Are negative or mixed results acknowledged rather than hidden?

### Limitations / Ethics / Reproducibility

- Are scope constraints and failure modes stated honestly?
- Do limitations weaken any central claim?
- Are data/code licenses, human-subject concerns, privacy risks, or potential misuse addressed when relevant?
- Is LLM usage disclosed when required by the venue?

## Rebuttal-Aware Writing

Before submission, imagine the top three reviewer criticisms and make sure the main paper already answers them. During rebuttal or discussion, be open to changing the paper's framing when reviewers reveal a real gap. Do not rely on rebuttal for substantial new experiments unless the venue explicitly allows them; use rebuttal primarily for clarification, corrections, and small supporting evidence.
