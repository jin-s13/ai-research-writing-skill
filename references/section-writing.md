# Section Writing Reference

Use this reference when drafting or revising Abstract, Introduction, Related Work, Method, Experiments, Limitations, or Conclusion.

For Abstract/Introduction specifically, load `abstract-introduction.md` first. This file covers the broader section-writing contract.

## Global Writing Loop

For each section, use this loop before polishing sentences:

1. **Section thesis**: one sentence saying what the section must convince the reviewer of.
2. **Paragraph roles**: assign one role per paragraph before drafting.
3. **Claim-evidence pass**: mark each strong claim as supported, needs evidence, or should be weakened.
4. **Reverse outline**: after drafting, list each paragraph's first-sentence message and evidence.
5. **Flow repair**: revise paragraphs whose first sentence does not support the section thesis.
6. **Terminology pass**: make terms, method names, task names, dataset names, and metric names consistent.

Use one paragraph for one message. The first sentence should tell the reader why the paragraph exists; later sentences should justify, contrast, refine, or exemplify that message.

## Abstract

Before writing, answer:

1. What technical problem is solved?
2. Why is there no established solution?
3. What is the central contribution?
4. Why does it work?
5. What evidence supports it?

Choose one structure:

### Abstract A: Challenge -> Contribution

Use for one central method.

1. Task or application need.
2. Technical challenge in prior work.
3. Method name and core contribution.
4. Benefit of the contribution.
5. Main evidence with numbers.

### Abstract B: Challenge -> Insight -> Contribution

Use when the paper has a clear design insight.

1. Task.
2. Technical challenge.
3. Insight in one sentence.
4. Method that implements the insight.
5. Main evidence.

### Abstract C: Multiple Contributions

Use for systems papers with several modules.

1. Task and prior gap.
2. Contribution 1 + advantage.
3. Contribution 2 + advantage.
4. Contribution 3 + advantage.
5. Experiment summary.

Rules:

- One paragraph only unless venue allows otherwise.
- Avoid packing too many module names into one sentence.
- Mention only results that support the main claims.
- If a metric is mixed, do not imply uniform improvement.
- Technical names must be self-contained and introduced before reuse.
- Avoid "we achieve SOTA" unless all comparisons are fair and complete.

### Abstract Diagnostics

Reject and rewrite an abstract if it has any of these symptoms:

- It names modules before the task and gap are clear.
- It says the method is "general" or "unified" without defining what is actually supported.
- It reports numbers without naming the benchmark or metric direction.
- It compares to prior work without naming the task difference.
- It hides the paper's main limitation by using vague words such as "robust" or "effective".

## Introduction

Use 5-7 paragraphs:

1. **Motivation**: why the task matters.
2. **Prior work gap**: what existing lines cover and miss.
3. **Technical challenge**: why the gap is hard.
4. **Method overview**: method stages and Figure 1.
5. **Design insight**: the principle behind the method.
6. **Evidence**: main results and careful scope.
7. **Contributions**: reviewer-facing bullets.

After drafting, create a reverse outline:

- Paragraph role.
- First-sentence message.
- Evidence used.
- Risk or unsupported claim.

### Backward-Then-Forward Process

First reason backward from the contribution:

1. What exact claim do we want the reviewer to remember?
2. What experiment or analysis proves it?
3. What technical challenge makes the result nontrivial?
4. Which prior-work gap naturally creates that challenge?
5. What opening context makes the gap matter?

Then write forward:

1. Context and task.
2. Prior work and missing capability.
3. Technical challenge.
4. Method idea.
5. Evidence and contributions.

This prevents introductions that start broad but never land on a precise paper.

### Introduction Opening Choices

- **Task first**: define a niche task before motivating applications.
- **Application first**: use when readers already know the task.
- **General-to-specific**: start from broad area, then define the paper setting.
- **Open with challenge**: if the target failure mode is clear and familiar.

### Technical Challenge Patterns

- **Existing task**: prior methods solve X, but fail at Y because Z.
- **Novel task**: define the task and decompose why it is hard.
- **Tradition-backed insight**: connect the method insight to a classical idea, then explain why modern methods still need a new implementation.

### Pipeline Introduction Patterns

- **One contribution, multiple advantages**: introduce one framework, then list advantages.
- **Two contributions**: first contribution solves the main gap, second solves a remaining bottleneck.
- **Module on existing pipeline**: show why the new module is necessary and not an obvious add-on.
- **Observation-driven**: state the observation first, then method.

### Contribution Bullets

Each contribution bullet should have:

`artifact or idea + why it matters + evidence or evaluation location`

Avoid bullets that only say "we implement" unless the implementation creates a measurable or conceptual advantage.

## Related Work

Group by research problem, not by chronology.

For each group:

- State what the group solves.
- Cite representative papers.
- State the remaining gap relative to this paper.
- Avoid strawman comparisons.
- Treat concurrent work briefly unless it is the central baseline.
- Do not use Related Work as a dumping ground. Each paragraph should prepare the reader for the paper's gap.
- If a work is very close but task definitions differ, state the difference calmly and precisely.

### Related Work Matrix

Before writing, create a compact matrix:

| Line of work | Representative papers | What they solve | What they do not cover | How we relate |
|---|---|---|---|---|

Use the matrix to prevent two common failures:

- **Citation soup**: many papers listed without a gap.
- **Strawman contrast**: prior work framed as weak when it solves a different task.

For concurrent work, use restrained language:

```text
Concurrent work studies ... In contrast, our work focuses on ... The two settings are complementary because ...
```

## Method

For each module:

- Motivation: why the module is needed.
- Inputs and outputs.
- Core operation.
- Design advantage.
- Failure or limitation when relevant.

Avoid only listing implementation files. Convert implementation details into method concepts.

For systems/workflow papers, include:

- Stage overview.
- Data/artifact flow.
- Control flow and retry/failure paths.
- Interfaces between learned/agentic and deterministic components.
- Why each boundary is placed where it is.

### Method Writing Contract

For each method subsection, include:

1. **Purpose**: the failure mode or requirement this module addresses.
2. **Input/Output**: concrete artifacts, not vague "information".
3. **Operation**: algorithm, prompt, parser, optimizer, verifier, or execution step.
4. **Invariant**: what the module guarantees or checks.
5. **Failure handling**: retry, reflection, fallback, or limitation.

When the method is an agent workflow, make the boundary between LLM reasoning and deterministic tools explicit. Reviewers should know which parts are learned, which parts are scripted, and which parts are verified by execution.

## Experiments

For each experiment:

- Research question.
- Dataset / benchmark.
- Baseline and fairness assumptions.
- Metrics and direction.
- Main result.
- Interpretation and caveat.

Do not hide negative metrics. Explain them if they matter.

Recommended experiment paragraph:

1. "This experiment asks whether ..."
2. "We evaluate on ..."
3. "We compare against ..."
4. "We report ..."
5. "The result shows ..."
6. "The main caveat is ..."

Recommended table caption:

- Include metric direction.
- Define abbreviations.
- State whether values are mean, median, std, or confidence intervals.

### Experiment Set Design

A strong experiments section usually contains:

- **Main comparison**: does the method solve the paper's central task?
- **Ablation**: which design choices matter?
- **Stress or breakdown analysis**: where does it fail by task level, dataset subset, or metric?
- **Qualitative examples**: what do successes and failures look like?
- **Efficiency/cost**: runtime, calls, tokens, compute, or human effort when relevant.

If one of these is missing, mention the reason or make it a limitation.

### Evidence Language

Use precise verbs:

- `shows` only when the result directly supports the claim.
- `suggests` when evidence is indirect or based on a limited setting.
- `is consistent with` when the result supports an interpretation but does not prove it.
- `does not address` when a missing experiment limits scope.

## Limitations

Include limitations that a reviewer can infer from the paper:

- Scope restrictions.
- Assumptions.
- Failure modes.
- Missing ablations.
- Reproducibility gaps.
- Runtime or cost issues.

Honest limitations often strengthen the paper by showing controlled claims.

Write limitations as scoped scientific constraints, not apologies:

```text
Our evaluation focuses on ... This leaves ... as future work.
```

## Conclusion

Use 1-2 paragraphs:

1. Restate problem and contribution.
2. Summarize evidence.
3. Name the most important remaining limitation or future direction.

Do not introduce new results in the conclusion.

## Claim-Evidence Map

For every major claim, record:

`Claim: ... | Evidence: ... | Status: supported / needs evidence / weaken`

Any `needs evidence` claim must be revised before final submission.

For existing LaTeX drafts, bootstrap this table with:

```bash
python scripts/extract_claims.py main.tex > claim_evidence_map.md
```

Then manually fill evidence and revision status.

## Paragraph Quality Checklist

For each paragraph:

- Does the first sentence state the paragraph's message?
- Does every sentence refine, justify, contrast, or exemplify the previous one?
- Are hidden terms defined before use?
- Does the paragraph support the section thesis?
- Would a skeptical reviewer know what evidence supports it?

## Revision Output Format

When revising a section, return or create:

- **Mini-outline**: 3-7 bullets showing paragraph roles.
- **Revised text**: polished prose.
- **Reverse outline**: paragraph role, first sentence, evidence.
- **Claim-evidence notes**: unsupported claims to weaken.
- **Residual risks**: missing experiments, citations, or definitions.
