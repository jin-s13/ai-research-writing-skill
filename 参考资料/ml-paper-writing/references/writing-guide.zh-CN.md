# ML 论文写作理念与最佳实践

本参考文档汇编 Neel Nanda、Andrej Karpathy、Sebastian Farquhar、Zachary Lipton、Jacob Steinhardt 等 prominent ML 研究者的写作建议。

---

## 目录

- [叙事原则](#叙事原则)
- [时间分配](#时间分配)
- [摘要写作公式](#摘要写作公式)
- [引言结构](#引言结构)
- [句子级清晰度](#句子级清晰度)
- [用词与精确性](#用词与精确性)
- [数学写作](#数学写作)
- [图表设计](#图表设计)
- [常见错误](#常见错误)

---

## 叙事原则

### Neel Nanda

「论文是一篇简短、严谨、基于证据的技术故事，读者关心其 takeaway。」

叙事建立在三根支柱上，须在引言结束时一目了然：

**「What」**：在一贯主题下 1–3 条具体、新颖的 claim。含糊的「我们研究 X」会立刻失败——审稿人需要精确、可证伪的 claim。

**「Why」**：严谨的经验证据令人信服地支持这些 claim，包括诚实调参的强基线，以及能区分竞争假设而非仅展示「还行结果」的实验。

**「So What」**：读者为何应关心，将贡献与社区公认的重要问题相连。

### Andrej Karpathy

「论文不是随手汇报的实验集合。论文推销的是此前不明显或不存在的一个东西。全文围绕这一核心贡献以手术刀般的精度组织。」

无论新架构、理论结果还是对既有方法的理解——NeurIPS 明确指出「原创性不一定要求全新方法」。

**实践含义**：若无法用一句话陈述贡献，你还没有一篇论文。实验、相关工作、讨论的存在仅为支撑该核心 claim。

---

## 时间分配

### Neel Nanda

在以下四块上大致投入**相等时间**：
1. 摘要
2. 引言
3. 图表
4. 其余全部合计

这不是夸张——多数审稿人在进入方法前已形成初步判断。读者按可预测顺序阅读：**标题 → 摘要 → 引言 → 图表 → 也许其余部分。**

### 审稿人阅读模式

对审稿人行为的研究显示：
- 摘要 100% 会被读
- 引言 90%+ 审稿人会 skim
- 多数审稿人在方法前先看图
- 全文方法仅在被吸引后才会细读

**含义**：把论文价值前置。勿把贡献埋在后面。

---

## 摘要写作公式

### Sebastian Farquhar 的 5 句公式

1. **你做到了什么**：「We introduce...」「We prove...」「We demonstrate...」
2. **为何困难且重要**
3. **你怎么做**（含专业关键词以利检索）
4. **你有什么证据**
5. **你最突出的数字/结果**

### 示例（好摘要）

```
We prove that gradient descent on overparameterized neural networks
converges to global minima at a linear rate. [What]
This resolves a fundamental question about why deep learning works
despite non-convex optimization landscapes. [Why hard/important]
Our proof relies on showing that the Neural Tangent Kernel remains
approximately constant during training, reducing the problem to
kernel regression. [How with keywords]
We validate our theory on CIFAR-10 and ImageNet, showing that
predicted convergence rates match experiments within 5%. [Evidence]
This is the first polynomial-time convergence guarantee for
networks with practical depth and width. [Remarkable result]
```

### 应避免

Zachary Lipton：「若第一句可接到任何 ML 论文上，删掉它。」

**删除这类开头**：
- "Large language models have achieved remarkable success..."
- "Deep learning has revolutionized..."
- "In recent years, neural networks have..."

**改从你的具体贡献开始。**

---

## 引言结构

### 要求

- **最多 1–1.5 页**（双栏格式）
- **方法应在第 2–3 页开始**
- 须含 **2–4 条贡献 bullet**（双栏下每条最多 1–2 行）

### 结构模板

```markdown
1. Opening Hook (2-3 sentences)
   - State the problem your paper addresses
   - Why it matters RIGHT NOW

2. Background/Challenge (1 paragraph)
   - What makes this problem hard?
   - What have others tried? Why is it insufficient?

3. Your Approach (1 paragraph)
   - What do you do differently?
   - Key insight that enables your contribution

4. Contribution Bullets (2-4 items)
   - Be specific and falsifiable
   - Each bullet: 1-2 lines maximum

5. Results Preview (2-3 sentences)
   - Most impressive numbers
   - Scope of evaluation

6. Paper Organization (optional, 1-2 sentences)
   - "Section 2 presents... Section 3 describes..."
```

### 贡献 bullet：好 vs 坏

**好：**
- We prove that X converges in O(n log n) time under assumption Y
- We introduce Z, a 3-layer architecture that reduces memory by 40%
- We demonstrate that A outperforms B by 15% on benchmark C

**坏：**
- We study the problem of X (not a contribution)
- We provide extensive experiments (too vague)
- We make several contributions to the field (says nothing)

---

## 句子级清晰度

### Gopen & Swan：《The Science of Scientific Writing》

这篇 1990 年经典论文指出：**读者对信息在散文中出现位置有结构预期**。违背这些预期会迫使读者把认知花在结构上而非内容上。

> "If the reader is to grasp what the writer means, the writer must understand what the reader needs."

#### 读者预期的 7 原则

**原则 1：主语-动词邻近**

语法主语与动词应靠近。中间插入内容会被读作次要打断。

**弱**：「The model, which was trained on 100M tokens and fine-tuned on domain-specific data using LoRA with rank 16, achieves state-of-the-art results」

**强**：「The model achieves state-of-the-art results after training on 100M tokens and fine-tuning with LoRA (rank 16)」

**原则 2：强调位置（把最好的留到最后）**

读者自然强调**句末**。把最重要信息放在那里。

**弱**：「Accuracy improves by 15% when using attention」
**强**：「When using attention, accuracy improves by **15%**」

**原则 3：主题位置（先交代背景）**

句首建立视角。把「这是谁的故事」放在前面——读者预期句子讲的是先出现的主体。

**弱**：「A novel attention mechanism that computes alignment scores is introduced」
**强**：「To address the alignment problem, we introduce a novel attention mechanism」

**原则 4：旧信息先于新信息**

把熟悉信息（旧）放在主题位置以向后衔接；把新信息放在强调位置。

**弱**：「Sparse attention was introduced by Child et al. The quadratic complexity of standard attention motivates this work.」
**强**：「Standard attention has quadratic complexity. To address this, Child et al. introduced sparse attention.」

**原则 5：一个单元一个功能**

每个话语单元（句、段、节）只服务一个功能。有两点就拆成两个单元。

**原则 6：动词承载动作**

把句子的动作放在动词里，而非名词化。

**弱**：「We performed an analysis of the results」（名词化）
**强**：「We analyzed the results」（动词承载动作）

**原则 7：新信息之前有上下文**

在要求读者接受新内容前先提供上下文。适用于句、段、节各层级。

**弱**：「Equation 3 shows that convergence is guaranteed when the learning rate satisfies...」
**强**：「For convergence to be guaranteed, the learning rate must satisfy the condition in Equation 3...」

#### 摘要表

| 原则 | 规则 | 记忆口诀 |
|-----------|------|----------|
| Subject-Verb Proximity | Keep subject and verb close | "Don't interrupt yourself" |
| Stress Position | Emphasis at sentence end | "Save the best for last" |
| Topic Position | Context at sentence start | "First things first" |
| Old Before New | Familiar → unfamiliar | "Build on known ground" |
| One Unit, One Function | Each paragraph = one point | "One idea per container" |
| Action in Verb | Use verbs, not nominalizations | "Verbs do, nouns sit" |
| Context Before New | Explain before presenting | "Set the stage first" |

---

---

## 微观写作技巧

### Ethan Perez (Anthropic)

这些微观技巧在句、词层面提升清晰度。

#### 代词管理

**尽量少用代词**（"this," "it," "these," "that"）。必要时作形容词并带名词：

**弱**：「This shows that the model converges.」
**强**：「This result shows that the model converges.」

**弱**：「It improves performance.」
**强**：「This modification improves performance.」

#### 动词位置

**把动词尽量靠前**，便于解析：

**弱**：「The gradient, after being computed and normalized, updates the weights.」
**强**：「The gradient updates the weights after being computed and normalized.」

#### 所有格展开

为清晰可展开所有格结构：

**原文**：「X's Y」→ **展开**：「The Y of X」

**前**：「The model's accuracy on the test set」
**后**：「The accuracy of the model on the test set」

并非总更好，但句子别扭时可试展开。

#### 应删除的词

在几乎所有情况下删除这些 filler：
- "actually"
- "a bit"
- "fortunately" / "unfortunately"
- "very" / "really"
- "quite"
- "basically"
- "essentially"
- 多余的连接词（非必要时少用 "however," "moreover," "furthermore"）

#### 造句规则

1. **一句一意** — 若一句难以表达，就拆成两句
2. **避免重复音** — 同句避免发音相近的词
3. **每句都有信息** — 删除仅复述的句子
4. **始终主动语态** — 指明主体（「We find...」而非「It is found...」）
5. **展开缩写** — 正式写作中「don't」→「do not」

#### 段落结构

- **首句**：清楚陈述要点
- **中间句**：用证据支撑
- **末句**：强化或过渡

勿把关键信息埋在段中。

---

## 用词与精确性

### Zachary Lipton

**删除 hedging**，除非确有不确定性：
- 除非必要删除 "may" 和 "can"
- 「provides *very* tight approximation」显得不自信
- 「provides tight approximation」更自信

**避免空洞强化词**：
- 删除：very, extremely, highly, significantly（除非指统计显著性）
- 这些词常显不自信而非有力

### Jacob Steinhardt

**精确优于简短**：用具体词替换模糊词。

| 模糊 | 具体 |
|-------|----------|
| performance | accuracy, latency, throughput |
| improves | increases accuracy by X%, reduces latency by Y |
| large | 1B parameters, 100M tokens |
| fast | 3x faster, 50ms latency |
| good results | 92% accuracy, 0.85 F1 |

**术语一致**：同一概念用不同词会造成混乱。

**选定一种并坚持**：
- "model" vs "network" vs "architecture"
- "training" vs "learning" vs "optimization"
- "sample" vs "example" vs "instance"

### 词汇信号

**避免暗示增量工作的词**：
- 勿用："combine," "modify," "expand," "extend"
- 改用："develop," "propose," "introduce"

**原因**：「We combine X and Y」像把两个现成想法拼在一起；「We develop a method that leverages X for Y」更像真实贡献。

---

## 数学写作

### Ethan Perez

**展开所有格**以提升清晰度：
- 弱：「X's Y」
- 强：「The Y of X」

示例：「the model's accuracy」→「the accuracy of the model」

### 一般原则

1. **定理前正式列出所有假设**
2. **证明旁给出直观解释**
3. **全文记号一致**
4. **符号首次出现时定义**

### 记号约定

```latex
% Scalars: lowercase italic
$x$, $y$, $\alpha$, $\beta$

% Vectors: lowercase bold
$\mathbf{x}$, $\mathbf{v}$

% Matrices: uppercase bold
$\mathbf{W}$, $\mathbf{X}$

% Sets: uppercase calligraphic
$\mathcal{X}$, $\mathcal{D}$

% Functions: roman for named functions
$\mathrm{softmax}$, $\mathrm{ReLU}$
```

---

## 图表设计

### Neel Nanda

图表应能独立讲述连贯故事，即使读者先跳过正文。许多读者**确实**会先跳过正文看图。

### 设计原则

1. **Figure 1 至关重要**：摘要后常被首先细看的图
2. **自洽 caption**：不读正文也应理解图
3. **图内勿放标题**：caption 承担此功能（ICML/NeurIPS 规则）
4. **矢量图**：曲线用 PDF/EPS，仅照片用 PNG（600 DPI）

### 可访问性

约 8% 男性有色觉缺陷，图须对他们可用。

**做法**：
- 色盲友好调色板：Okabe-Ito 或 Paul Tol
- 避免红绿组合
- 验证灰度可读
- 除颜色外还用线型（实线、虚线、点线）

### 工具

```python
# SciencePlots: Publication-ready styles
import matplotlib.pyplot as plt
plt.style.use(['science', 'ieee'])

# Or for Nature-style
plt.style.use(['science', 'nature'])
```

---

## 常见错误

### 结构错误

| 错误 | 对策 |
|---------|----------|
| 引言过长（>1.5 页） | 背景移入 Related Work |
| 方法被埋没（第 3 页后才开始） | 前置贡献、压缩引言 |
| 缺少贡献 bullet | 添加 2–4 条具体、可证伪 claim |
| 实验未写明支撑的 claim | 每项实验前说明检验什么 |

### 写作错误

| 错误 | 对策 |
|---------|----------|
| 摘要开头泛泛 | 从具体贡献开始 |
| 术语不一致 | 每概念一词 |
| 被动语态过多 | 主动：「We show」而非「It is shown」 |
| 处处 hedging | 除非真不确定，否则自信表述 |

### 图表错误

| 错误 | 对策 |
|---------|----------|
| 曲线用位图 | 用矢量（PDF/EPS） |
| 红绿配色 | 色盲友好调色板 |
| 图内标题 | 标题放 caption |
| caption 依赖正文 | 使 caption 自洽 |

### 引用错误

| 错误 | 对策 |
|---------|----------|
| Related Work 逐篇罗列 | 按方法组织 |
| 漏引重要文献 | 审稿人可能即作者——慷慨引用 |
| AI 生成引用 | 始终经 API 核验 |
| 引用格式不一致 | BibLaTeX + 统一 key |

---

## 投稿前清单

投稿前确认：

**叙事**：
- [ ] 能用一句话陈述贡献
- [ ] 引言中 What/Why/So What 清晰
- [ ] 每项实验支撑具体 claim

**结构**：
- [ ] 摘要遵循 5 句公式
- [ ] 引言 ≤1.5 页
- [ ] 方法在第 2–3 页开始
- [ ] 含 2–4 条贡献 bullet
- [ ] 有 Limitations 节

**写作**：
- [ ] 全文术语一致
- [ ] 无泛泛开头句
- [ ] 除非必要已删除 hedging
- [ ] 所有图有自洽 caption

**技术**：
- [ ] 所有引用经 API 核验
- [ ] 含误差条及计算方法说明
- [ ] 算力资源已记录
- [ ] 已说明代码/数据可得性
