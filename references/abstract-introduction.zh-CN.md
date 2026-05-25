# 摘要与引言参考文档

当你要写最“高风险”的段落时，使用本参考文档：摘要（Abstract）与引言（Introduction）。
它吸收了 `research-paper-writing` 中的摘要/引言模板、先反向（backward-first）的逻辑，以及反向大纲（reverse-outline）的工作流。

## 共享规则（Shared Rule）

每一条主要的摘要/引言主张（claim）都必须在“主张-证据映射表（claim-evidence map）”里有一行。
如果证据缺失或呈现混合态，就在润色文句前先削弱该主张。

## 摘要写作前问题（Abstract Pre-Writing Questions）

在开始起草前回答：

1. 解决了什么技术问题？
2. 为什么没有成熟的既有解法？
3. 核心贡献是什么？
4. 方法“本质上”为什么能工作？
5. 提供了什么技术优势或洞察？
6. 主张的核心证据是什么？

## 摘要模板（Abstract Templates）

### 模板 A：挑战 -> 贡献（Challenge -> Contribution）

适用于一个核心方法或工作流。

1. 任务或应用需求。
2. 既有工作中的技术挑战。
3. 方法名称与核心贡献。
4. 贡献带来的收益（benefit）。
5. 结合基准/指标名称给出主要证据（main evidence）。

### 模板 B：挑战 -> 洞察 -> 贡献（Challenge -> Insight -> Contribution）

适用于论文有明确的设计洞察（design insight）。

1. 任务。
2. 技术挑战。
3. 用一句话写清洞察（insight）。
4. 实现洞察的方法。
5. 实现带来的优势（advantage）。
6. 主要证据。

### 模板 C：多重贡献（Multiple Contributions）

适用于系统论文（systems papers）中需要多块“必要组件”的情况。

1. 任务与缺口（gap）。
2. 贡献 1 + 优势。
3. 贡献 2 + 优势。
4. 贡献 3 + 优势。
5. 实验总结。

## 摘要诊断（Abstract Diagnostics）

如果摘要出现以下任意症状，就拒绝并重写：

- 第一句之后，任务仍不清楚；
- 在问题/缺口讲清楚之前先给出模块名称；
- 贡献听起来像是在列实现步骤；
- 只报告结果，但没有指标方向或基准语境；
- 摘要中说“general / unified / robust / first / state-of-the-art”，但没有证据；
- 任务定义与近相关工作或并行工作差异被隐藏了。

## 引言逻辑地图（Introduction Logic Map）

先倒着想（Think backward first）：

1. 评审会记住的核心贡献是什么？
2. 有哪些证据支撑这一贡献？
3. 什么技术挑战让该贡献不那么容易？
4. 哪个既有工作缺口自然地产生了这个挑战？
5. 什么任务/应用背景让这个缺口变得重要？

然后再正着写（Then write forward）：

1. 任务与应用。
2. 既有工作与仍未解决的缺口。
3. 根本技术挑战。
4. 提出的方法/工作流，以及为什么它有效。
5. 证据。
6. 贡献。

## 引言开头模式（Introduction Opening Patterns）

### 开头 A：先写任务（Task First）

适用于任务比较小众或是新定义的。

```text
[Task] aims to produce [output] from [input]. This setting matters for ...
```

### 开头 B：先写应用（Application First）

适用于读者已经熟悉该任务。

```text
[Application area] increasingly requires ... Existing systems therefore need ...
```

### 开头 C：由一般到具体（General to Specific）

适用于具体设定是新的，但属于某个已知领域。

```text
[General area] has enabled ... This paper focuses on [specific setting], where ...
```

### 开头 D：以挑战开场（Open With Challenge）

适用于失败模式（failure mode）是熟悉且具有动机的。

```text
Although recent methods can ..., they still fail when ... because ...
```

## 技术挑战模式（Technical Challenge Patterns）

### 既有任务（Existing Task）

```text
This problem is challenging because ...
Traditional methods ... However, ...
Recent methods ... However, ... because ...
```

### 既有任务 + 经典洞察（Existing Task With Classical Insight）

```text
A classical way to address this is ...
However, classical methods still ...
Modern methods improve ..., but still fail to ... because ...
```

### 新任务（Novel Task）

```text
在这项工作中，我们的目标是 ...
这个问题之所以有挑战性，原因有三点。
第一， ...
第二， ...
最后， ...
```

## 流水线式引言模式（Pipeline Introduction Patterns）

### 一个贡献，多种优势（One Contribution, Multiple Advantages）

```text
我们提出 [method/workflow] 来完成 [task]。
关键想法是 ...
具体而言， ...
该设计使得 ...
```

### 两个贡献（Two Contributions）

```text
我们提出 [framework]。
它的第一个部分 ...
然而，这会带来 ...
为了解决这个问题，我们加入第二个部分 ...
```

### 在既有流水线上引入新模块（New Module on Existing Pipeline）

```text
既有流水线已经 ...
剩余的瓶颈是 ...
我们加入 [module]，用于 ...
```

### 由观察驱动（Observation Driven）

```text
我们观察到 ...
这提示 ...
我们通过 ... 把这一洞察落地实现。
```

## 反向大纲（Reverse Outline）

起草之后，创建这个表：

```markdown
| Paragraph | 角色 | 第一句话的信息 | Evidence（证据） | Risk（风险） | Revision（修改） |
|---|---|---|---|---|---|
| P1 | motivation/task（动机/任务） | ... | citation/result（引用/结果） | ... | ... |
```

规则：

- 如果第一句话没有说明该段落的角色，就重写。
- 如果某条“强主张”的证据列是空的，就削弱或删除该主张。
- 如果两段落有相同的角色，就合并或拆分它们的“消息（messages）”。
- 如果某段落的角色不能支撑该分节的主旨（section thesis），就裁掉。

## 引言贡献要点（Introduction Contribution Bullets）

每条要点应遵循：

```text
贡献工件/想法 + 为什么重要 + 证据或评估位置。
```

避免那种只说“我们实现了……（we implement）”的要点，除非实现本身就是一个可衡量的系统贡献。

