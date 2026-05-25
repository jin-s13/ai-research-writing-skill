# 审稿人指南与评估标准

本参考文档说明主要 ML/AI 与系统会议审稿人如何评估论文，帮助作者预判并回应审稿关切。

## 目录

- [通用评估维度](#通用评估维度)
- [NeurIPS 审稿人指南](#neurips-审稿人指南)
- [ICML 审稿人指南](#icml-审稿人指南)
- [ICLR 审稿人指南](#iclr-审稿人指南)
- [ACL 审稿人指南](#acl-审稿人指南)
- [系统会议审稿人指南](#系统会议审稿人指南)
- [何谓高质量审稿](#何谓高质量审稿)
- [常见审稿关切](#常见审稿关切)
- [如何回应审稿意见](#如何回应审稿意见)

## 通用评估维度

所有主要 ML 会议从四个核心维度评估论文：

### 1. Quality（技术可靠性）

**审稿人会问：**
- claim 是否有理论分析或实验结果充分支撑？
- 证明是否正确？实验是否控制得当？
- 基线是否合适且公平对比？
- 方法论是否可靠？

**如何确保高质量：**
- 提供完整证明（正文或附录含证明 sketch）
- 使用合适基线（非稻草人）
- 报告方差/误差条及计算方法
- 记录超参选择过程

### 2. Clarity（写作与组织）

**审稿人会问：**
- 论文是否清晰、组织良好？
- 领域专家能否复现结果？
- 记号是否一致？术语是否定义？
- 论文是否自洽？

**如何确保清晰：**
- 全文术语一致
- 记号首次使用时定义
- 含可复现细节（附录可接受）
- 投稿前请非作者阅读

### 3. Significance（影响与重要性）

**审稿人会问：**
- 结果对社区是否有影响？
- 他人是否会在此基础上继续工作？
- 是否解决重要问题？
- 实际影响潜力如何？

**如何体现重要性：**
- 清楚说明问题重要性
- 与更广泛研究主题相连
- 讨论潜在应用
- 与现有方法有意义地对比

### 4. Originality（新颖性与贡献）

**审稿人会问：**
- 是否提供新洞见？
- 与先前工作有何不同？
- 贡献是否非平凡？

**NeurIPS 指南要点：**
> "Originality does not necessarily require introducing an entirely new method. Papers that provide novel insights from evaluating existing approaches or shed light on why methods succeed can also be highly original."

## NeurIPS 审稿人指南

### 打分体系（1–6 分）

| 分数 | 标签 | 说明 |
|-------|-------|-------------|
| **6** | Strong Accept | 开创性、近乎无瑕疵；居前 2–3% |
| **5** | Accept | 技术扎实、影响大；有益于社区 |
| **4** | Borderline Accept | 扎实但评估有限；倾向接收 |
| **3** | Borderline Reject | 扎实但弱点多于优点；倾向拒稿 |
| **2** | Reject | 技术缺陷或评估薄弱 |
| **1** | Strong Reject | 已知结果或伦理问题未解决 |

### 审稿人须知

审稿人被明确要求：

1. **按论文现状评估** — 非「若修改后会如何」
2. **提供建设性反馈** — 3–5 条可执行要点
3. **不因诚实承认局限而扣分** — 鼓励承认弱点
4. **评估可复现性** — 工作能否被验证？
5. **考虑伦理影响** — 潜在滥用或伤害

### 审稿人应避免

- 肤浅、缺乏依据的审稿
- 要求不合理的大量额外实验
- 因作者诚实承认局限而惩罚
- 因未引用审稿人自己的工作而拒稿

### 时间线（NeurIPS 2025）

- Bidding：5 月 17–21 日
- 审稿期：5 月 29 日 – 7 月 2 日
- 作者 rebuttal：7 月 24–30 日
- 讨论期：7 月 31 日 – 8 月 13 日
- 最终通知：9 月 18 日

## ICML 审稿人指南

### 审稿结构

ICML 审稿人提供：

1. **Summary** — 贡献简述
2. **Strengths** — 优点
3. **Weaknesses** — 待改进处
4. **Questions** — 需作者澄清
5. **Limitations** — 对所述局限的评估
6. **Ethics** — 伦理关切
7. **Overall Score** — 总体推荐

### 打分指南

ICML 使用类似 1–6 分并校准：
- 录用论文前 25%：5–6 分
- 典型录用：4–5 分
- 边界：3–4 分
- 明确拒稿：1–2 分

### 关键评估点

1. **可复现性** — 细节是否足够？
2. **实验严谨性** — 多种子、合适基线？
3. **写作质量** — 清晰、有条理？
4. **新颖性** — 贡献是否非平凡？

## ICLR 审稿人指南

### OpenReview 流程

ICLR 使用 OpenReview：
- 录用决定后公开审稿意见
- 作者回复对审稿人可见
- 审稿人与 AC 讨论

### 打分

ICLR 审稿包含：
- **Soundness**：1–4
- **Presentation**：1–4
- **Contribution**：1–4
- **Overall**：1–10
- **Confidence**：1–5

### ICLR 特有考量

1. **LLM 披露** — 审稿人评估 LLM 使用是否恰当披露
2. **可复现性** — 强调代码可得性
3. **Reciprocal Reviewing** — 作者须担任审稿人

## ACL 审稿人指南

### ACL 特有标准

ACL 增加 NLP 特定评估：

1. **语言学可靠性** — 语言学 claim 是否准确？
2. **资源文档** — 数据集/模型是否妥善记录？
3. **多语言考量** — 若适用，是否涵盖语言多样性？

### Limitations 节

ACL 强制要求 Limitations 节。审稿人检查：
- 局限是否诚实、全面？
- 局限是否削弱核心 claim？
- 是否讨论潜在负面影响？

### 伦理审稿

ACL 有专门伦理审稿流程，针对：
- 双重用途关切
- 数据隐私
- 偏见与公平

## 系统会议审稿人指南

系统会议（OSDI、NSDI、ASPLOS、SOSP）与 ML/AI 会议的评估方式不同。跨 venue 投稿时理解这些差异至关重要。

### 系统会议核心评估标准

| 标准 | 审稿人关注 | |
|-----------|------------------------|-----------|
| **Novelty** | 新系统设计，而非仅增量改进 | |
| **Significance** | 解决重要实际问题 | |
| **System Design** | 架构可靠、设计决策清晰 | |
| **Implementation** | 可运行原型，非仅仿真 | |
| **Evaluation** | 真实负载、端到端性能 | |
| **Clarity** | 写作清晰、可复现 | |

### OSDI 2026 审稿视角

**审稿人评估：**
- 主题与计算机系统相关性
- 对未来系统研究与实践的影响潜力
- 对相当比例 OSDI 参会者的兴趣
- PC 重叠少的论文录用概率较低

**Research Track 标准：**
- 新颖性、重要性、清晰度、相关性、正确性
- 系统中量化或有洞见的经验

**Operational Systems Track 标准：**
- 有意义规模的真实部署
- 加深对既有问题理解的教训
- 推翻或强化既有假设
- **不要求**新颖研究想法

**2026 新变化：**
- 无作者回复期
- Conditional accept 替代 revise-and-resubmit
- 目标录用率 ≥20%
- 鼓励对注水论文降分

### NSDI 2027 审稿视角

**预筛（仅 Introduction）**

预筛阶段审稿人检查三项：
1. **Scope**：主题属于 NSDI 范围
2. **Accessibility**：PC 成员可理解
3. **Track alignment**：符合轨道标准

**分轨道评审**

| Track | 关键标准 | |
|-------|---------------|----------|
| Research | 新颖想法 + 有说服力的评估证据 | + |
| Frontiers | 大胆非增量想法（不要求完整评估） | |
| Operational | 部署背景、规模、对社区的教训 | |

**One-shot revision**
- 被拒论文可能收到需修改问题清单
- 作者可在下一截止日提交修订
- 尽可能由相同审稿人审修订稿

### ASPLOS 2027 审稿视角

**Rapid Review Round**
- 审稿人**仅**读前 2 页
- 评估：是否推进 Architecture、PL 或 OS 研究？
- 多数投稿可能无法通过此阶段
- 类似 Nature/Science 早期筛选

**Full Review 标准**
- 推进 ASPLOS 核心学科（非仅使用它们）
- 系统设计与实现质量
- 可提供 Major Revision 决定

### SOSP 2026 审稿视角

**核心评估**
- 新颖性、重要性、兴趣、清晰度、相关性、正确性
- 鼓励重要新方向的突破性工作
- 新问题与成熟领域评估标准不同

**Author Response**
- 限于：纠正事实错误 + 回应审稿人问题
- **不得**加入新实验或额外工作
- 建议控制在 500 词以内

**Artifact Evaluation：**
- 可选但鼓励
- 协作流程：评估期间作者可修复问题
- 录用通知后数日内注册

### ML 与系统：审稿差异对照

| 方面 | ML/AI 会议 | 系统会议 | |
|--------|-------------|---------------|----------|
| **页数限制** | 7–9 页 | 12 页 | |
| **评估重点** | 基准、消融、指标 | 端到端系统性能、真实负载 | |
| **实现** | 代码常可选 | 期望可运行系统 | |
| **新颖性** | 新方法/洞见 | 新系统设计/方法 | |
| **可复现性** | Checklist 驱动 | Artifact evaluation（可选） | |
| **模板** | Venue 专用 `.sty` | USENIX `.sty` 或 ACM `acmart.cls` | |
| **评审流程** | 单截止 | 常为双截止 | |

## 系统会议常见关切

| 关切 | 如何预先化解 | |
|---------|-----------------|----------|
| "只是 ML 论文，不是系统" | 强调系统设计、架构决策、部署挑战 | |
| "评估只有微基准" | 含真实负载的端到端评估 | |
| "没有可工作原型" | 构建并评估真实系统，非仅仿真 | |
| "部署不现实" | 展示实际适用性，讨论实际约束 | |
| "与系统社区无关" | 用系统术语 framing，引用系统论文 | |
| "ASPLOS：未推进 arch/PL/OS" | 明确说明如何推进核心学科 | |

### 遵循 Daniel Dennett 的规则

优秀审稿人遵循：

1. **公平重述立场** — 表明理解论文
2. **列出同意之处** — 承认做得好的地方
3. **列出你学到什么** — 认可贡献
4. **然后再批评** — 在建立理解之后

### 审稿结构最佳实践

**强审稿结构：**
```
Summary (1 paragraph):
- What the paper does
- Main contribution claimed

Strengths (3-5 bullets):
- Specific positive aspects
- Why these matter

Weaknesses (3-5 bullets):
- Specific concerns
- Why these matter
- Suggestions for addressing

Questions (2-4 items):
- Clarifications needed
- Things that would change assessment

Minor Issues (optional):
- Typos, unclear sentences
- Formatting issues

Overall Assessment:
- Clear recommendation with reasoning
```

## 常见审稿关切

### 技术关切

| 关切 | 如何预先化解 |
|---------|-----------------|
| "Baselines too weak" | 使用 SOTA 基线，引用近期工作 |
| "Missing ablations" | 含系统消融研究 |
| "No error bars" | 报告 std dev/error，多次运行 |
| "Hyperparameters not tuned" | 记录调参过程与搜索范围 |
| "Claims not supported" | 确保每条 claim 有证据 |

### 新颖性关切

| 关切 | 如何预先化解 |
|---------|-----------------|
| "Incremental contribution" | 清楚说明相对先前工作的新意 |
| "Similar to [paper X]" | 在 Related Work 中明确对比 X |
| "Straightforward extension" | 突出非显而易见之处 |

### 清晰度关切

| 关切 | 如何预先化解 |
|---------|-----------------|
| "Hard to follow" | 清晰结构、路标句 |
| "Notation inconsistent" | 检查全部记号，可做记号表 |
| "Missing details" | 含可复现附录 |
| "Figures unclear" | 自洽 caption、合适尺寸 |

### 重要性关切

| 关切 | 如何预先化解 |
|---------|-----------------|
| "Limited impact" | 讨论更广泛含义 |
| "Narrow evaluation" | 多基准评估 |
| "Only works in restricted setting" | 承认范围，说明为何仍有价值 |

## 如何回应审稿意见

### Rebuttal 最佳实践

**应做：**
- 感谢审稿人时间
- 逐条回应关切
- 提供证据（可能时补充新实验）
- 简洁——审稿人很忙
- 承认合理批评

**勿做：**
- 防御或 dismiss
- 承诺做不到的事
- 回避难批评
- 写过长的 rebuttal
- 争论主观判断

### Rebuttal 模板

```markdown
We thank the reviewers for their thoughtful feedback.

## Reviewer 1

**R1-Q1: [Quoted concern]**
[Direct response with evidence]

**R1-Q2: [Quoted concern]**
[Direct response with evidence]

## Reviewer 2

...

## Summary of Changes
If accepted, we will:
1. [Specific change]
2. [Specific change]
3. [Specific change]
```

### 何时接受批评

部分反馈应直接接受：
- 有效技术错误
- 漏引重要相关工作
- 表述不清
- 缺实验细节

优雅承认：「审稿人指出…我们将修订为…」

### 何时礼貌反驳

可在以下情况尊重地不同意：
- 审稿人误解论文
- 要求实验超出范围
- 批评事实错误

建设性 framing：「我们理解这一观点。然而，[解释]…」

## 投稿前模拟审稿

投稿前自问：

**Quality：**
- [ ] 若看到这类结果我会相信吗？
- [ ] 所有 claim 是否有证据？
- [ ] 基线是否公平且较新？

**Clarity：**
- [ ] 他人能否仅凭论文复现？
- [ ] 对本子领域外专家是否清晰？
- [ ] 所有术语与记号是否定义？

**Significance：**
- [ ] 社区为何应关心？
- [ ] 他人能用这项工作做什么？
- [ ] 问题是否重要？

**Originality：**
- [ ] 此处具体新在哪里？
- [ ] 与最接近的相关工作有何不同？
- [ ] 贡献是否非平凡？
