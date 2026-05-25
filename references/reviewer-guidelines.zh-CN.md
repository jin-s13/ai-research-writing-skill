# 审稿指南参考文档

使用本参考文档将你的草稿对齐到：ML/AI/系统论文的审稿人如何评判。
它吸收了 `ml-paper-writing` 中的实用 reviewer-guideline 内容。

## 通用审稿维度（Universal Reviewer Dimensions）

| 维度 | 审稿人会问 | 作者需要做什么 |
|---|---|---|
| 质量/可靠性（Quality / soundness） | 主张是否有支撑？方法与实验是否正确？ | 把主张绑定到证据上；记录协议（protocol）。 |
| 清晰度（Clarity） | 读者能否理解并复现你的工作？ | 定义术语、保持逻辑流畅、补全细节。 |
| 重要性（Significance） | 你的结果对社区是否有意义？ | 连接真实的缺口（gap），并使用有意义的任务。 |
| 新颖性（Originality） | 有什么新东西或洞察？ | 精确描述新颖性类型（novelty type）。 |
| 可复现性（Reproducibility） | 结果能否被验证？ | 提供代码/数据/设置/随机种子/算力（compute）。 |

新颖性并不一定要求“提出一个新模型（new model）”。当你提出新的任务、基准、系统工作流、评估发现或解释，并且确实改变了社区能做什么或能理解什么，那么也可以是原创的。

## 常见审稿担忧（Common Reviewer Concerns）

- 主贡献不清楚，或改进太小（incremental）。
- 方法模块缺少动机。
- 基线较弱、缺失或不公平（unfair）。
- 评估指标与宣称的能力不匹配。
- 实验过于简单或范围太窄。
- 报告结果时缺少方差或关键信息不足。
- 摘要/引言中的主张超出实验支持范围。
- 局限明显但没有写出来。
- 相关工作遗漏了“很近”的论文，或错误描述了任务差异。

## 会议趋势（Venue Tendencies）

### NeurIPS / ICML / ICLR

- 强叙事与清晰技术洞察很重要。
- 实验严谨性与公平基线被重点审查。
- 可复现性与局限通常是期待项。
- LLM 使用与伦理披露（ethics disclosures）可能会在某些年份/会议更重要。

### ACL / NLP

- 局限与伦理是核心。
- 数据集、标注范围（annotation）、语言范围（language scope）与人类评估细节很关键。
- 关于偏差（bias）、语言覆盖（language coverage）或人类偏好（human preference）的主张需要谨慎证据支持。

### 系统会议（Systems）

- 一个可工作的原型（working prototype）、系统设计理由（system design rationale）、以及端到端评估都很重要。
- 真实工作负载与部署经验可能和算法新颖性一样重要。
- 审稿人期望看到开销（overhead）、压力测试（stress tests）、拆解（breakdowns）、以及清晰的设计边界。

## 审稿可用的分节检查（Review-Ready Section Checks）

### 摘要（Abstract）

- 审稿人能否在一遍阅读中识别任务、缺口、贡献与证据？
- 所有“强烈词汇（strong words）”是否都有合理支撑？

### 引言（Introduction）

- 第一页是否让论文的新颖性与重要性显而易见？
- 是否避免了“朴素基线 + 小补丁”的叙事框架？

### 方法（Method）

- 每个模块是否都由一个挑战（challenge）驱动？
- 输入、输出、不变量（invariants）、以及失败处理（failure handling）是否清楚？

### 实验（Experiments）

- 每个实验是否回答一个研究问题？
- 基线与指标是否公平？
- 消融是否足够？

### 局限（Limitations）

- 是否诚实写明范围约束（scope constraints）与失败模式（failure modes）？
- 局限是否会削弱任何核心主张？

## 面向反驳（Rebuttal-Aware Writing）

提交之前，想象审稿人最可能的三条批评，并确保你的正文已经提前回答了它们。
写作越好，反驳（rebuttal）压力就越小。

