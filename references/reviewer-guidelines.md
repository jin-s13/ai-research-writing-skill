# Reviewer Guidelines Reference

Use this for evidence-based peer review and author-side diagnosis of ML/AI/CV/NLP papers. For author revision planning, also load [reviewer-self-review.md](reviewer-self-review.md).

## Select the Review Context

- **Author self-review / simulation**: diagnose the draft and propose revisions. Label simulated recommendations; do not present them as actual venue decisions.
- **Assigned peer review**: assess the submitted version and available supplements, produce a concise review with evidence notes, and leave final judgment to the human reviewer. Do not rewrite the manuscript unless asked.

Keep confidential review material within the authorized workspace. Never fabricate a human reviewer’s original assessment, expertise, or completed reproduction work.

## Evidence-First Review Procedure

1. **Inventory coverage**: record the submission version, main text, relevant appendices, code/data availability, and inaccessible or unprovided material. An access failure is not evidence that authors supplied nothing. State partial-read limits explicitly.
2. **Restate the strongest supported contribution**: distinguish full-system performance from the controlled contribution of a component. Recognize useful negative results, simple methods, careful measurements, and new tasks without demanding leaderboard gains.
3. **Check before objecting**: inspect relevant appendices and captions before claiming something is missing. Visually verify consequential equations, table columns, and figures when text extraction is ambiguous. If verification is impossible, retain the uncertainty rather than assert a contradiction. Recompute decisive differences or ratios where feasible, recording inputs and assumptions; a toy calculation is not a reproduced benchmark.
4. **Build the evidence notes** below before drafting verdicts. Record what is already supplied, what it supports, and what remains unestablished. Separate direct observations, interpretations, and questions for clarification.
5. **Prioritize by decision impact**: merge duplicate concerns and foreground the few that can change the recommendation. Around three may be a useful concise starting point, never a quota or a cap on independent material issues. Omit peripheral requests from formal reviews; keep optional editorial suggestions separate when requested.
6. **Calibrate the recommendation**: weigh reliable contributions against unresolved risks to central claims, not the number of complaints. State decisive reasons and the evidence still needed to assess central claims. Report confidence from actual reading, technical verification, and remaining uncertainty, independently of the recommendation.

### Evidence Notes

For each material concern, use an ID shared by the review and evidence notes:

```text
ID / affected claim:
Location: page, section, equation, table row, appendix, or artifact path
Already supplied / checked:
Observation and evidence:
Interpretation or uncertainty: fact / inference / needs clarification
Impact on the central claim and severity:
Question for authors:
Minimum evidence that would resolve or narrow this concern:
```

Record strengths with concrete locations and why the evidence matters too. Detailed derivations and checks belong in evidence notes, leaving the review concise. For file-based work, use `review.md` and `review_evidence.md` (or the user’s existing paths); keep confidential material in the authorized review workspace, outside this skill repository. For a chat-only review, provide concise evidence notes in the response without creating a paper project.

### Fairness and Burden

- Match requests to the actual claim. Prefer an existing table, configuration, bounded calculation, or small diagnostic over a new research project. Explain why any additional experiment is necessary to assess the submitted claim.
- Missing detail or an unclear split supports a clarification request, not an accusation of leakage, fabrication, or misconduct. Ethics concerns need specific evidence and the venue’s appropriate reporting channel; scientific limitations alone are not ethics violations.
- For novelty objections, identify concrete technical overlap and differences in verified close work. Apply the target venue’s rules for contemporaneous and non-peer-reviewed work; do not turn every newly found paper into a mandatory baseline.
- Use literature to assess contributions, not infer anonymous authors. Do not rank a submission against other confidential submissions as a basis for judgment.
- Do not penalize non-SOTA results, missing optional extensions, or cosmetic defects unless they materially undermine the paper’s stated contribution or its assessment.

## Concise Review Format

Use this concise working format:

```text
Review context: submitted version, AI-assisted or simulated status
Summary: problem, method, strongest supported contribution, scope
Strengths: specific evidence and value
Major concerns: IDs, locations, evidence, impact on claims
Questions: map each to a concern ID and bounded resolving evidence
Recommendation: textual stance and decisive reasons
Confidence and coverage: what was checked, not checked, and remains uncertain
Ethics: evidence-based concern if any; no identified concern is not an ethics clearance
```

When the available material cannot support an overall judgment, explain why and provide only the supported partial assessment. Do not manufacture a stance merely to fill the format.

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

Before submission, identify the highest-impact reviewer criticisms and make sure the main paper already answers them. During rebuttal or discussion, be open to changing the paper's framing when reviewers reveal a real gap. Do not rely on rebuttal for substantial new experiments unless the venue explicitly allows them; use rebuttal primarily for clarification, corrections, and small supporting evidence.
