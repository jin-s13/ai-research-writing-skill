# 审稿前自查参考文档

在进行大幅修改（major revisions）以及提交之前，先使用本参考文档。
目标是：在审稿人指出之前，先找到可能导致拒稿的风险。

## 五维审稿（Five-Dimension Review）

对每个维度打分为：`pass`、`needs revision` 或 `needs evidence`。

| 维度 | 审稿人会问什么 | 常见失败 |
|---|---|---|
| Contribution（贡献） | 有什么新东西？为什么重要？ | 论文读起来像实现报告（implementation report）。 |
| Writing clarity（写作清晰度） | 读完引言后，审稿人能否复述论文？ | 叙事是模块清单。 |
| Experimental strength（实验强度） | 实验是否支撑主要主张？ | 主要主张依赖部分数据或“挑选过”的数字（cherry-picked）。 |
| Evaluation completeness（评估完整性） | 基线、指标、划分（splits）是否公平？ | 缺少消融、设定不清楚或基线较弱。 |
| Method soundness（方法可靠性） | 设计选择是否有依据且可复现？ | 方法依赖未记录的提示词（prompts）、启发式（heuristics）或隐藏的手工步骤。 |

需要校准“面向会议的审稿期望与评分”时，使用 `references/reviewer-guidelines.zh-CN.md`。

## 接受信号（Acceptance Signals）

当满足以下条件，论文就会更接近“审稿可接受（reviewer-ready）”：

- 贡献类型明确：任务（task）、方法（method）、系统（system）、基准（benchmark）、数据集（dataset）、分析（analysis）或发现（finding）。
- 主结果由公平的基线与合适的指标支撑。
- 消融覆盖关键设计选择。
- 第一页让新颖性与重要性清晰可见。
- 局限诚实，并且不与核心主张相矛盾。

## 拒稿风险审计（Rejection-Risk Audit）

创建 `submission_readiness.md`，包含：

1. **论文主张（Paper thesis）**。
2. **审稿人最可能的五个反对点（Top five reviewer objections）**。
3. **针对每个反对点的证据（Evidence that addresses each objection）**。
4. **仍然存在的缺口（Remaining gaps）**。
5. **计划修复（Planned fix）**：编辑、增加实验、加入局限，或移除主张。
6. **严重程度（Severity）**：high / medium / low。

对于严重等级（high）且仍未解决的问题，除非用户明确接受风险，否则应阻止你发出“最终提交回应（final submission response）”。

## 反向/对抗式问题（Adversarial Questions）

以一个怀疑的审稿人角度提问：

- 任务究竟是什么？它的定义是否比以往工作更清楚？
- 你宣称的新颖性属于：方法、系统、基准、数据集、工作流，还是评估协议？
- 审稿人会不会说：这只是提示词工程（prompt engineering）？如果是，那是什么让它不仅是“提示词”？
  - 具体来说，是执行（execution）、验证（verification）、表征（representation）、还是评估（evaluation）上的贡献？
- 摘要中最强的主张是否由最强的实验支撑？
- 是否承认了负结果或混合结果？
- 在相同输入/输出假设下，基线是否可比？
- 评估指标是否与论文声称“在乎”的能力一致？
- 你是否挑选了少数例子（cherry-picked），还是展示了系统性的行为？
- 有没有把引用当成“装饰”，而不是当成证据？
- 局限是否显而易见但未写明？

## 主张审计（Claim Audit）

对每条 Abstract 与 Introduction 的主张：

```text
Claim:
Evidence:
Citation or result:
Risk:
Revision:
Status: keep / weaken / remove / needs experiment
```

规则：

- 强主张需要直接证据。
- 广泛能力主张需要边界（task boundaries）。
- “First / general / unified / end-to-end / robust / state-of-the-art” 类表达需要额外审查。
- 如果某个术语可能被误解，就在第一次出现附近给出定义。

## 实验审计（Experiment Audit）

对每个实验：

- 它回答了什么研究问题？
- 它支撑了论文的哪个主张？
- 基线是否公平且有明确命名？
- 指标是否给出方向（direction）？
- 是否需要方差（variance）、种子（seeds）或重复运行（repeats）？
- 是否分析了失败案例（failure cases）？
- 审稿人是否会要求你补充一个缺失的消融？
- caption 是否足够让读者独立理解？

## 写作审计（Writing Audit）

对每个分节：

- 开头句是否说明该节的角色（role）？
- 每个段落是否只传达一个消息（one message）？
- 段落之间的转折/过渡是否基于逻辑，而非时间顺序（chronology）？
- 方法名称是否前后一致？
- 在动机之前，论文是否避免把读者淹没在实现细节里？
- 方法细节变得难以追踪之前，是否在正文里先引入 Figure 1？

## 审稿可用的修改计划（Reviewer-Ready Revision Plan）

把风险转成行动：

| Risk | Fix type | Concrete action | Owner/status |
|---|---|---|---|
| Unsupported claim（无支撑主张） | Edit（编辑） | Weaken claim in Abstract and Introduction. | |
| Missing evidence（证据缺失） | Experiment（实验） | Add ablation on ... | |
| Confusing method（方法令人困惑） | Writing/Figure（写作/图表） | Add overview diagram and method invariant. | |
| Weak citation（引用较弱） | Citation（引用） | Replace with verified primary source. | |
| Scope gap（范围缺口） | Limitation（局限） | Add limitation paragraph. | |

## 最终自查陈述（Final Self-Review Statement）

定稿前写：

```text
The paper is currently strongest on ...
The highest remaining reviewer risk is ...
The main evidence supporting the central claim is ...
Claims intentionally weakened or removed:
Submission-blocking issues:
```

