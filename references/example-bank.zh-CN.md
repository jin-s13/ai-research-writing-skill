# 示例库参考文档

把它当作一个“紧凑的模式库（pattern bank）”。它会吸收 `research-paper-writing` 里的示例库思想，但在默认情况下不会加载过长的例子。

## 摘要模式（Abstract Patterns）

### 挑战 -> 贡献（Challenge -> Contribution）

```text
[任务/工作（Task）] 对于 [应用（application）] 很重要，但仍然很难，因为 [技术挑战（technical challenge）]。
现有方法 [它们做什么（what they do）]，但由于 [根本原因（root reason）]，仍会在 [失败模式（failure mode）] 上失败。
我们提出 [method]，其核心贡献是 [core contribution]。
通过 [机制/洞察（mechanism/insight）]， [method] 实现了 [优势（advantage）]。
在 [基准（benchmarks）] 上的实验表明 [主要证据（main evidence）]。
```

### 挑战 -> 洞察 -> 贡献（Challenge -> Insight -> Contribution）

```text
[Task] 需要 [capability]。
既有工作在 [challenge] 上感到困难。
我们观察到 [insight]。
基于这一洞察，我们引入 [method] 来完成 [operation]。
[Evidence sentence].
```

### 多重贡献（Multiple Contributions）

```text
[Task/缺口（gap）句子]。
首先，我们在 [advantage] 方面做出贡献： [contribution]。
其次，我们在 [advantage] 方面做出贡献： [contribution]。
第三，我们在 [advantage] 方面做出贡献： [contribution]。
[Evidence sentence].
```

## 引言模式（Introduction Patterns）

### 新任务挑战的拆解（Novel Task Challenge Decomposition）

```text
在这项工作中，我们的目标是 [goal]。
这个设定之所以具有挑战性，原因有三点。
第一， [challenge 1 + reason]。
第二， [challenge 2 + reason]。
最后， [challenge 3 + reason]。
```

### 已有任务但仍有瓶颈（Existing Task With Remaining Bottleneck）

```text
近期的方法通过 [approach] 在 [task] 上取得了进展。
然而，它们仍然无法实现 [capability]，因为 [root technical reason]。
该瓶颈之所以重要，是因为 [application/evaluation requirement]。
```

### 由观察驱动的方法（Observation-Driven Method）

```text
我们观察到 [surprising or useful property]。
这一观察提示： [design principle]。
我们通过 [method/workflow] 把这一原则落地实现。
```

## 方法模式（Method Patterns）

### 模块三元组（Module Triad）

```text
目的（Purpose）：解释这个模块为什么存在（为什么需要它）。
输入/输出（Input/Output）：该模块接收 [input] 并返回 [output]。
操作（Operation）：它执行 [core operation]。
不变性/约束（Invariant）：它保证/检查 [property]。
失败处理（Failure handling）：如果出现 [failure]，它会 [retry/fallback/limitation]。
```

### 智能体工作流模块（Agent Workflow Module）

```text
智能体/工具 [agent/tool] 将语义推理与确定性执行分离。
LLM 负责 [decision]，而 [tool/script] 用于验证 [property]。
这种边界能减少 [failure mode]，因为 [reason]。
```

## 实验模式（Experiment Patterns）

### 主要结果段落（Main Result Paragraph）

```text
本实验关注：是否 [method] 能提升 [capability]。
我们在 [dataset/benchmark] 上进行评估，使用 [metrics, direction]。
在 [fairness condition] 条件下，我们与 [baselines] 进行对比。
结果表明 [specific finding]。
主要的局限是 [scope/limitation]。
```

### 消融段落（Ablation Paragraph）

```text
为了隔离 [component] 的贡献，我们移除/替换 [component]。
性能从 [number] 变化到 [number]，表明 [interpretation]。
这支持我们的设计选择，因为 [reason]。
```

## 审稿回复模式（Reviewer Response Patterns）

### 带局限意识的主张（Limitation-Aware Claim）

```text
我们的结果显示，在已评估的设定中，[claim]。
这些结果尚未建立更广泛的 [broader claim]，我们把它留作未来工作。
```

### 并行工作（Concurrent Work）

```text
并行工作研究了 [setting]。
我们的工作在 [task/input/output/evaluation] 上有所不同。
这两个方向是互补的，因为 [reason]。
```

