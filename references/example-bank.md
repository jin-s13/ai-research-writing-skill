# Example Bank Reference

Use this as a compact pattern bank without loading long examples by default.

## Abstract Patterns

### Challenge -> Contribution

```text
[Task] is important for [application], but remains difficult because [technical challenge].
Existing methods [what they do], yet [failure mode] because [root reason].
We introduce [method], which [core contribution].
By [mechanism/insight], [method] enables [advantage].
Experiments on [benchmarks] show [main evidence].
```

### Challenge -> Insight -> Contribution

```text
[Task] requires [capability].
Prior work struggles with [challenge].
We observe that [insight].
Based on this insight, we introduce [method] to [operation].
[Evidence sentence].
```

### Multiple Contributions

```text
[Task/gap sentence].
First, we [contribution] to [advantage].
Second, we [contribution] to [advantage].
Third, we [contribution] to [advantage].
[Evidence sentence].
```

## Introduction Patterns

### Novel Task Challenge Decomposition

```text
In this work, our goal is to [goal].
This setting is challenging for three reasons.
First, [challenge 1 + reason].
Second, [challenge 2 + reason].
Finally, [challenge 3 + reason].
```

### Existing Task With Remaining Bottleneck

```text
Recent methods have made progress on [task] by [approach].
However, they still fail to [capability] because [root technical reason].
This bottleneck matters because [application/evaluation requirement].
```

### Observation-Driven Method

```text
We observe that [surprising or useful property].
This observation suggests [design principle].
We operationalize this principle through [method/workflow].
```

## Method Patterns

### Module Triad

```text
Purpose: [why this module exists].
Input/Output: The module takes [input] and returns [output].
Operation: It [core operation].
Invariant: It guarantees/checks [property].
Failure handling: If [failure], it [retry/fallback/limitation].
```

### Agent Workflow Module

```text
The [agent/tool] separates semantic reasoning from deterministic execution.
The LLM is responsible for [decision], while [tool/script] verifies [property].
This boundary reduces [failure mode] because [reason].
```

## Experiment Patterns

### Main Result Paragraph

```text
This experiment asks whether [method] improves [capability].
We evaluate on [dataset/benchmark] using [metrics, direction].
We compare with [baselines] under [fairness condition].
The results show [specific finding].
The main caveat is [scope/limitation].
```

### Ablation Paragraph

```text
To isolate the contribution of [component], we remove/replace [component].
Performance changes from [number] to [number], indicating that [interpretation].
This supports the design choice because [reason].
```

## Reviewer Response Patterns

### Limitation-Aware Claim

```text
Our results show [claim] in [evaluated setting].
They do not yet establish [broader claim], which we leave for future work.
```

### Concurrent Work

```text
Concurrent work studies [setting].
Our work differs in [task/input/output/evaluation].
The two directions are complementary because [reason].
```
