---
name: research-paper-writing
description: 提升 ML/CV/NLP 风格学术论文的写作质量，包括清晰的章节结构、段落衔接与面向审稿人的呈现。适用于起草或修订 Abstract、Introduction、Related Work、Method、Experiments、Conclusion；润色图表；检查主张与证据是否一致；或在投稿前进行自我审稿。
---
# 研究论文写作

## 概述

使用本 skill 将研究论文改写为对审稿人友好、高清晰度的稿件。
优先保证第一印象质量（图/表/版式）、逻辑连贯，以及有证据支撑的主张。

## 核心工作流

1. 在句子级润色之前，先厘清论文故事线（paper story）。
2. 使用 `references/` 中的分节指南。
3. 按段落逐段改写，每段只传达一个信息。
4. 每写完一节，做一次反向提纲（reverse outline）。
5. 检查 Abstract/Introduction 中的每条主要主张是否与实验证据一致。
6. 用 `references/paper-review.md` 做终稿对抗式审稿。

## 全局原则

1. 一段只讲一件事。
2. 在首句点明该段要传达的信息。
3. 让名词自洽；新术语在复用前先定义。
4. 保持句间衔接（因果、对比、结果或递进）。
5. 用对抗式自审迭代：以持怀疑态度的审稿人视角阅读。
6. 将视觉质量视为核心内容，而非装饰。
7. 使用清晰的 teaser 图与 pipeline 图。
8. 使用可读、少墨迹的表格。
9. 保持格式一致、整洁。

## 段落清晰度检查（重要）

当用户问某段是否「顺畅」或是否清楚时，使用此快速测试。

1. 以外部读者视角阅读：
   - 本段是否有一个明确的信息？
   - 首句是否说明本段要做什么？
   - 所有关键名词/术语是否无需隐含上下文即可读懂？
   - 每句与上一句是否有清晰关系（因果、对比、结果、递进、举例）？
2. 对当前节做反向提纲（reverse outline）：
   - 写下论点/主主张。
   - 写下每段主题句。
   - 写下每段下的证据/解释要点。
   - 检查映射：主题句 → 论点，证据 → 主题句。
   - 修订或删除无法干净映射的段落。
3. 若衔接仍弱，修订时可临时加小节标题与显式过渡语，定稿前再删去不必要标题。

本检查的来源参考：

- `references/does-my-writing-flow-source.md`

## 分节指南

仅加载所需分节文件：

- Introduction：`references/introduction.md`
- Abstract：`references/abstract.md`
- Related Work：`references/related-work.md`
- Method：`references/method.md`
- Experiments：`references/experiments.md`
- Conclusion：`references/conclusion.md`
- 论文审稿（Paper Review）：`references/paper-review.md`
- 段落清晰度来源：`references/does-my-writing-flow-source.md`
- 范例库索引：`references/examples/index.md`

## 论文审稿要点

完整清单与工作流见 `references/paper-review.md`。

1. 在稿末增加五维自审问题清单：
   - 贡献（contribution），
   - 写作清晰度，
   - 实验力度，
   - 评估完整性，
   - 方法设计合理性。
2. 将主张-证据对齐视为硬约束，尤其针对 Abstract 与 Introduction。
3. 进行对抗式写作：以持怀疑态度的审稿人审稿，并解决每个高风险问题。
4. 修订直至主要拒稿风险被明确处理。

## 执行规则

1. 写正文前先建迷你提纲。
2. 每个子节在适用时明确包含动机、设计与技术优势。
3. 避免像在朴素基线上做增量补丁的写作风格。
4. 全文术语保持稳定。
5. 若某主张无法被结果支撑，则弱化或删除该主张。
6. 定稿前补充并回答五维自审问题清单，再据未解决项修订论文。
7. 不要一次性加载所有分节参考（Introduction/Abstract/Related Work/Method/Experiments/Conclusion）；仅加载当前编辑目标对应的分节指南。

## 输出约定

当被要求改写或起草分节时，返回：

1. 紧凑的分节提纲（3–7 条要点）。
2. 修订后的段落，并标明段落角色（开篇/挑战/方法/优势/证据/局限）。
3. 简短的自审清单，覆盖清晰度、衔接、术语一致、无支撑主张与缺失证据。
4. 对修订文中每条主要主张的「主张-证据」映射：`Claim: ... | Evidence: ... | Status: supported/needs evidence`。
