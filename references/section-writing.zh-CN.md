# 分节写作参考文档

当你要撰写或修改摘要（Abstract）、引言（Introduction）、相关工作（Related Work）、方法（Method）、实验（Experiments）、局限（Limitations）或结论（Conclusion）时使用本参考文档。

如果只针对摘要/引言：请先加载 `abstract-introduction.zh-CN.md`。本文件会覆盖更广泛的分节写作契约（section-writing contract）。

## 全局写作循环（Global Writing Loop）

对每个分节，在润色句子之前按以下循环：

1. **分节主旨（Section thesis）**：用一句话说明该分节必须让审稿人相信什么。
2. **段落角色（Paragraph roles）**：在起草前给每个段落分配一个角色（role）。
3. **主张-证据（Claim-evidence pass）**：把每条强主张标记为“已支撑（supported）/需要证据（needs evidence）/应削弱（should be weakened）”。
4. **反向大纲（Reverse outline）**：起草后列出每个段落的“首句信息（first-sentence message）”与“证据（evidence）”。
5. **流畅性修复（Flow repair）**：如果某个段落的首句不能支撑分节主旨，就修改该段落。
6. **术语检查（Terminology pass）**：让术语、方法名、任务名、数据集名、指标名保持一致。

每个段落只传达一个消息（one message）。
首句应该告诉读者：这个段落为什么存在；后续句子则用于解释、对比、细化或举例支撑该消息。

## 摘要（Abstract）

写作前回答：

1. 解决了什么技术问题？
2. 为什么没有成熟的既有解法？
3. 核心贡献是什么？
4. 为什么该方法有效？
5. 证据是什么？

选择一种结构：

### 摘要 A：挑战 -> 贡献（Challenge -> Contribution）

适用于一个核心方法。

1. 任务或应用需求。
2. 既有工作中的技术挑战。
3. 方法名称与核心贡献。
4. 贡献带来的收益。
5. 用数字呈现主要证据。

### 摘要 B：挑战 -> 洞察 -> 贡献（Challenge -> Insight -> Contribution）

适用于论文有明确的设计洞察。

1. 任务。
2. 技术挑战。
3. 用一句话写清洞察。
4. 实现该洞察的方法。
5. 主要证据。

### 摘要 C：多重贡献（Multiple Contributions）

适用于系统论文，包含多个模块。

1. 任务与先前缺口（prior gap）。
2. 贡献 1 + 优势。
3. 贡献 2 + 优势。
4. 贡献 3 + 优势。
5. 实验总结。

规则：

- 除非会议允许，否则只写一个段落（one paragraph）。
- 避免把太多模块名塞进同一句。
- 只提及能支撑主要主张的结果。
- 如果某个指标呈现混合结果，不要暗示存在“统一改进（uniform improvement）”。
- 技术名称必须自洽，并且在首次复用前先引入。
- 除非所有对比都公平且完整，否则避免使用 “we achieve SOTA（我们达到最先进）”。

### 摘要诊断（Abstract Diagnostics）

出现以下任意症状，就拒绝并重写摘要：

- 在任务与缺口讲清之前就先点名模块；
- 没有给出“具体支持了什么”，就使用 “general（通用）/unified（统一）”；
- 报告数字但没有说明基准或指标方向（metric direction）；
- 只对比既有工作但没有点出任务差异；
- 用 “robust（鲁棒）/effective（有效）” 等模糊词，把论文最主要的局限“藏起来”。

## 引言（Introduction）

用 5-7 个段落组织：

1. **动机（Motivation）**：为什么该任务重要。
2. **既有工作缺口（Prior work gap）**：哪些已有方向覆盖了，哪些遗漏了。
3. **技术挑战（Technical challenge）**：为什么这个缺口难以解决。
4. **方法概览（Method overview）**：方法阶段与 Figure 1。
5. **设计洞察（Design insight）**：方法背后的原则。
6. **证据（Evidence）**：主要结果与谨慎边界。
7. **贡献（Contributions）**：面向审稿人的要点（bullets）。

起草后创建反向大纲：

- 段落角色。
- 首句信息。
- 使用到的证据。
- 风险或无支撑主张。

### 先反向后正向流程（Backward-Then-Forward Process）

先从贡献（contribution）反推原因：

1. 我们希望审稿人记住的精确主张是什么？
2. 哪个实验或分析证明了它？
3. 什么技术挑战让结果并不“显然”？
4. 哪个既有工作缺口自然地产生了这个挑战？
5. 什么开场语境让这个缺口变得重要？

然后再正向写：

1. 上下文与任务。
2. 既有工作与仍未具备的能力。
3. 技术挑战。
4. 方法想法。
5. 证据与贡献。

这能避免出现那种：引言开得很大很泛，但最终落不到一个精确可验证的论文主旨上。

### 引言开头的选项（Introduction Opening Choices）

- **先任务（Task first）**：在动机应用之前，先定义一个小众任务。
- **先应用（Application first）**：当读者已经熟悉该任务时使用。
- **由一般到具体（General-to-specific）**：先从大领域开始，再定义论文设定。
- **以挑战开场（Open with challenge）**：如果目标失败模式清晰且读者熟悉。

### 技术挑战模式（Technical Challenge Patterns）

- **既有任务（Existing task）**：先前方法能解决 X，但因为 Z 在 Y 上失败。
- **新任务（Novel task）**：定义任务，并拆解为什么它难。
- **传统洞察支撑（Tradition-backed insight）**：把方法洞察连接到一个经典思想，然后解释为什么现代方法仍然需要新的实现方式。

### 流水线式引言模式（Pipeline Introduction Patterns）

- **一个贡献，多种优势（One contribution, multiple advantages）**：先引入一个框架，再列举优势。
- **两个贡献（Two contributions）**：第一个贡献解决主要缺口，第二个贡献解决剩余瓶颈。
- **在既有流水线上引入模块（Module on existing pipeline）**：说明新模块为什么必要，而不是一个显然的“附加品”。
- **由观察驱动（Observation-driven）**：先陈述观察，再给出方法。

### 贡献要点（Contribution Bullets）

每条贡献要点应包含：

`artifact or idea + why it matters + evidence or evaluation location`

避免那种只写“我们实现了（we implement）”的要点，除非实现本身就是一种可衡量或概念层面的优势。

## 相关工作（Related Work）

按“研究问题”分组，而不是按时间顺序分组。

对每个分组：

- 说明该组工作解决了什么。
- 引用有代表性的论文。
- 相对于本文，说明仍剩下的缺口是什么。
- 避免稻草人式对比（strawman comparisons）。
- 简要处理并行工作，除非它是最核心的基线。
- 不要把相关工作写成“倾倒区”。每个段落都要为论文将要提出的缺口做准备。
- 如果某项工作非常接近但任务定义不同，要冷静且精确地写出差异。

### 相关工作矩阵（Related Work Matrix）

写作之前先做一个紧凑矩阵：

| 研究线条（Line of work） | 代表论文（Representative papers） | 他们解决了什么（What they solve） | 他们没覆盖什么（What they do not cover） | 我们如何关联（How we relate） |
|---|---|---|---|---|

用该矩阵防止两种常见失败：

- **引用汤（Citation soup）**：列了很多论文，但没有缺口。
- **稻草人对比（Strawman contrast）**：把既有工作在“不同任务”上做得很弱，来做对比。

对于并行工作，使用克制的表达：

```text
Concurrent work studies ... In contrast, our work focuses on ... The two settings are complementary because ...
```

## 方法（Method）

对每个模块：

- 动机：为什么需要它。
- 输入与输出。
- 核心操作。
- 设计优势。
- 在相关时说明失败或局限。

不要只列“实现文件”。要把实现细节转换成方法层面的概念。

对于系统/工作流论文，还需要包含：

- 阶段概览（Stage overview）。
- 数据/工件流（Data/artifact flow）。
- 控制流与重试/失败路径（Control flow and retry/failure paths）。
- 学习/智能体式组件与确定性组件之间的接口。
- 说明每个边界为什么放在这里。

### 方法写作契约（Method Writing Contract）

对每个方法子章节，包含：

1. **目的（Purpose）**：该模块解决的失败模式（failure mode）或需求（requirement）。
2. **输入/输出（Input/Output）**：具体工件，而不是模糊的“信息（information）”。
3. **操作（Operation）**：算法、提示词（prompt）、解析器（parser）、优化器（optimizer）、验证器（verifier）或执行步骤。
4. **不变性（Invariant）**：该模块保证或检查什么。
5. **失败处理（Failure handling）**：重试（retry）、反思（reflection）、回退（fallback）或局限（limitation）。

当方法是一个智能体工作流时，要把 LLM 推理与确定性工具之间的边界讲清楚：
审稿人应当知道哪些部分是“学习出来的（learned）”、哪些部分是脚本化的（scripted）、以及哪些部分通过执行完成了验证（verified by execution）。

## 实验（Experiments）

对每个实验：

- 研究问题（Research question）。
- 数据集 / 基准（Dataset / benchmark）。
- 基线与公平性假设（Baseline and fairness assumptions）。
- 指标与方向（Metrics and direction）。
- 主结果（Main result）。
- 解释与注意事项（Interpretation and caveat）。

不要隐藏负指标。如果它们重要，就要解释。

推荐实验段落写法：

1. “本实验关注：是否 ...”
2. “我们在 ... 上评估。”
3. “我们与 ... 对比。”
4. “我们报告 ...”
5. “结果表明 ...”
6. “主要注意事项是 ...”

推荐表格 caption 写法：

- 包含指标方向。
- 定义缩写。
- 说明数值是均值（mean）、中位数（median）、标准差（std），还是置信区间（confidence intervals）。

### 实验集设计（Experiment Set Design）

一个强的实验章节通常包含：

- **主要对比（Main comparison）**：方法是否解决了论文核心任务？
- **消融（Ablation）**：哪些设计选择真正重要？
- **压力/失效分析（Stress or breakdown analysis）**：在任务层级、数据集子集或指标层级上在哪些地方失败？
- **定性示例（Qualitative examples）**：成功与失败看起来是什么样？
- **效率/成本（Efficiency/cost）**：运行时间、调用次数（calls）、token、算力（compute），或在人力投入上（when relevant）。

如果缺少其中任何一项，要么说明原因，要么把它写成局限。

### 证据语言（Evidence Language）

使用精确动词：

- 只有当结果直接支撑主张时才使用 `shows`。
- 证据是间接的、或只基于有限设定时使用 `suggests`。
- 结果支持某种解释但尚不能证明时用 `is consistent with`。
- 当缺失实验限制了适用范围时用 `does not address`。

## 局限（Limitations）

加入审稿人可以从论文推断出来的局限：

- 范围限制（Scope restrictions）。
- 假设条件（Assumptions）。
- 失败模式（Failure modes）。
- 缺失的消融（Missing ablations）。
- 可复现性差口（Reproducibility gaps）。
- 运行时间或成本问题（Runtime or cost issues）。

诚实的局限通常会通过“把主张控制在可验证范围内”而反过来增强论文。

局限写成“带范围约束的科学结论”，而不是道歉式文字：

```text
Our evaluation focuses on ... This leaves ... as future work.
```

## 结论（Conclusion）

使用 1-2 段：

1. 重述问题与贡献。
2. 概括证据。
3. 点出最重要的仍然存在的局限，或未来方向。

结论中不要引入新的结果。

## 主张-证据映射表（Claim-Evidence Map）

对每个主要主张，记录：

`Claim: ... | Evidence: ... | Status: supported / needs evidence / weaken`

任何 `needs evidence` 的主张，都必须在最终提交前修订。

对于已有的 LaTeX 草稿，可以用如下方式先生成该表：

```bash
python scripts/extract_claims.py main.tex > claim_evidence_map.md
```

然后再手动填写证据与修改状态（revision status）。

## 段落质量检查清单（Paragraph Quality Checklist）

对每个段落：

- 首句是否说明该段落的消息（message）？
- 每一句是否都在细化、证明、对比或举例上承接前一句？
- 在使用隐藏术语之前，是否给出了定义？
- 该段落是否支撑该分节的主旨？
- 一个怀疑型审稿人能否知道是什么证据支撑了它？

## 修改输出格式（Revision Output Format）

修改分节时，返回或创建：

- **迷你大纲（Mini-outline）**：3-7 条，展示段落角色（paragraph roles）。
- **修改后的文本（Revised text）**：润色后的正文段落。
- **反向大纲（Reverse outline）**：段落角色、首句、证据。
- **主张-证据注记（Claim-evidence notes）**：需要削弱的无支撑主张。
- **残余风险（Residual risks）**：缺失实验、引用或定义。

