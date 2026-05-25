# Abstract and Introduction Reference

Use this reference for the highest-risk writing sections: Abstract and Introduction.

## Shared Rule

Every major Abstract and Introduction claim must have a row in the claim-evidence map. If the evidence is absent or mixed, weaken the claim before polishing prose.

## Abstract Pre-Writing Questions

Answer before drafting:

1. What technical problem is solved?
2. Why is there no well-established solution?
3. What is the core contribution?
4. Why can the method work in essence?
5. What technical advantage or insight does it provide?
6. What evidence supports the main claim?

## Abstract Templates

### Template A: Challenge -> Contribution

Use for one central method or workflow.

1. Task or application need.
2. Technical challenge in prior work.
3. Method name and core contribution.
4. Benefit of the contribution.
5. Main evidence with benchmark/metric names.

### Template B: Challenge -> Insight -> Contribution

Use when the paper has a clear design insight.

1. Task.
2. Technical challenge.
3. Insight in one sentence.
4. Method that implements the insight.
5. Advantage of the implementation.
6. Main evidence.

### Template C: Multiple Contributions

Use for multi-component papers with several necessary pieces.

1. Task and gap.
2. Contribution 1 + advantage.
3. Contribution 2 + advantage.
4. Contribution 3 + advantage.
5. Experiment summary.

## Abstract Diagnostics

Reject and rewrite the abstract if:

- the task is unclear after the first sentence;
- module names appear before the problem/gap is clear;
- the contribution sounds like a list of implementation steps;
- results are reported without metric direction or benchmark context;
- the abstract says "general", "unified", "robust", "first", or "state-of-the-art" without evidence;
- task definition differences from close or concurrent work are hidden.

## Introduction Logic Map

Think backward first:

1. What should the reviewer remember as the central contribution?
2. What evidence supports that contribution?
3. What technical challenge makes the contribution nontrivial?
4. Which prior-work gap naturally creates that challenge?
5. What task/application context makes the gap matter?

Then write forward:

1. Task and application.
2. Prior work and unresolved gap.
3. Root technical challenge.
4. Proposed method/workflow and why it works.
5. Evidence.
6. Contributions.

## Introduction Opening Patterns

### Opening A: Task First

Use when the task is niche or newly defined.

```text
[Task] aims to produce [output] from [input]. This setting matters for ...
```

### Opening B: Application First

Use when readers already know the task.

```text
[Application area] increasingly requires ... Existing methods therefore need ...
```

### Opening C: General to Specific

Use when the specific setting is new but belongs to a known area.

```text
[General area] has enabled ... This paper focuses on [specific setting], where ...
```

### Opening D: Open With Challenge

Use when the failure mode is familiar and motivating.

```text
Although recent methods can ..., they still fail when ... because ...
```

## Technical Challenge Patterns

### Existing Task

```text
This problem is challenging because ...
Traditional methods ... However, ...
Recent methods ... However, ... because ...
```

### Existing Task With Classical Insight

```text
A classical way to address this is ...
However, classical methods still ...
Modern methods improve ..., but still fail to ... because ...
```

### Novel Task

```text
In this work, our goal is to ...
This problem is challenging for three reasons.
First, ...
Second, ...
Finally, ...
```

## Pipeline Introduction Patterns

### One Contribution, Multiple Advantages

```text
We introduce [method/workflow] for [task].
The key idea is ...
Specifically, ...
This design enables ...
```

### Two Contributions

```text
We introduce [framework].
Its first component ...
However, this leaves ...
To address this, the second component ...
```

### New Module on Existing Pipeline

```text
Existing pipelines already ...
The remaining bottleneck is ...
We add [module] that ...
```

### Observation Driven

```text
We observe that ...
This suggests ...
We operationalize this insight by ...
```

## Reverse Outline

After drafting, create this table:

```markdown
| Paragraph | Role | First-sentence message | Evidence | Risk | Revision |
|---|---|---|---|---|---|
| P1 | motivation/task | ... | citation/result | ... | ... |
```

Rules:

- If the first sentence does not state the paragraph role, rewrite it.
- If the evidence column is empty for a strong claim, weaken or remove the claim.
- If two paragraphs have the same role, merge or separate their messages.
- If a paragraph's role does not support the section thesis, cut it.

## Introduction Contribution Bullets

Each bullet should follow:

```text
Contribution artifact/idea + why it matters + evidence or evaluation location.
```

Avoid contribution bullets that only say "we implement" unless implementation is itself a measurable system contribution.
