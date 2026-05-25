---
name: ml-paper-writing
description: 为 NeurIPS、ICML、ICLR、ACL、AAAI、COLM、OSDI、NSDI、ASPLOS、SOSP 撰写可投稿的 ML/AI/系统论文。适用于从研究仓库起草论文、组织论证、核验引用或准备 camera-ready 投稿。含 LaTeX 模板、审稿人指南与引用核验工作流。
version: 1.1.0
author: Orchestra Research
license: MIT
tags: [Academic Writing, NeurIPS, ICML, ICLR, ACL, AAAI, COLM, OSDI, NSDI, ASPLOS, SOSP, LaTeX, Paper Writing, Citations, Research, Systems]
dependencies: [semanticscholar, arxiv, habanero, requests]
---

# 顶级 AI 与系统会议 ML 论文写作

面向 **NeurIPS、ICML、ICLR、ACL、AAAI、COLM**（ML/AI venue）与 **OSDI、NSDI、ASPLOS、SOSP**（系统 venue）的可投稿论文写作专家级指南。本 skill 融合顶尖研究者（Nanda、Farquhar、Karpathy、Lipton、Steinhardt）的写作理念与实用工具：LaTeX 模板、引用核验 API 与会议 checklist。

## 核心理念：协作式写作

**论文写作是协作过程，但 Claude 应主动交付草稿。**

典型工作流从含代码、结果与实验产物的研究仓库开始。Claude 的角色是：

1. **理解项目** — 探索仓库、结果与现有文档
2. **在把握贡献时交付完整初稿**
3. **检索文献** — 用网络搜索与 API 找相关引用
4. **在科学家反馈下迭代精炼**
5. **仅在关键决策 genuinely 不确定时询问澄清**

**关键原则**：主动。若仓库与结果清晰，交付完整初稿。勿在每个章节都等反馈——科学家很忙。先给出可反应的具体文稿，再根据其回复迭代。

---

## ⚠️ 关键：切勿幻觉引用

**这是 AI 辅助学术写作最重要的规则。**

### 问题
AI 生成引用的**错误率约 40%**。幻觉参考文献——不存在的论文、错误作者、错误年份、伪造 DOI——是严重学术不端，可导致 desk rejection 或撤稿。

### 规则
**切勿凭记忆生成 BibTeX。务必程序化获取。**

| 行动 | ✅ 正确 | ❌ 错误 |
|--------|-----------|----------|
| 添加引用 | 搜索 API → 核验 → 获取 BibTeX | 凭记忆写 BibTeX |
| 不确定某篇论文 | 标为 `[CITATION NEEDED]` | 猜测引用 |
| 找不到确切论文 | 注明："placeholder - verify" | 编造听起来相似的论文 |

### 无法核验引用时

若无法程序化核验引用，必须：

```latex
% EXPLICIT PLACEHOLDER - requires human verification
\cite{PLACEHOLDER_author2024_verify_this}  % TODO: Verify this citation exists
```

**务必告知科学家**：「我已将 [X] 条引用标为待核验占位符，无法确认这些论文存在。」

### 推荐：安装 Exa MCP 用于论文检索

最佳论文检索体验可安装 **Exa MCP**，提供实时学术搜索：

**Claude Code:**
```bash
claude mcp add exa -- npx -y mcp-remote "https://mcp.exa.ai/mcp"
```

**Cursor / VS Code**（加入 MCP 设置）：
```json
{
  "mcpServers": {
    "exa": {
      "type": "http",
      "url": "https://mcp.exa.ai/mcp"
    }
  }
}
```

Exa MCP 支持例如：
- "Find papers on RLHF for language models published after 2023"
- "Search for transformer architecture papers by Vaswani"
- "Get recent work on sparse autoencoders for interpretability"

然后用 Semantic Scholar API 核验结果，并通过 DOI 获取 BibTeX。

---

## 工作流 0：从研究仓库起步

开始写论文时，先理解项目：

```
Project Understanding:
- [ ] Step 1: Explore the repository structure
- [ ] Step 2: Read README, existing docs, and key results
- [ ] Step 3: Identify the main contribution with the scientist
- [ ] Step 4: Find papers already cited in the codebase
- [ ] Step 5: Search for additional relevant literature
- [ ] Step 6: Outline the paper structure together
- [ ] Step 7: Draft sections iteratively with feedback
```

**步骤 1：探索仓库**

```bash
# Understand project structure
ls -la
find . -name "*.py" | head -20
find . -name "*.md" -o -name "*.txt" | xargs grep -l -i "result\|conclusion\|finding"
```

关注：
- `README.md` — 项目概览与主张
- `results/`、`outputs/`、`experiments/` — 关键发现
- `configs/` — 实验设置
- 既有 `.bib` 或引用
- 任何草稿或笔记

**步骤 2：识别既有引用**

检查代码库中已引用的论文：

```bash
# Find existing citations
grep -r "arxiv\|doi\|cite" --include="*.md" --include="*.bib" --include="*.py"
find . -name "*.bib"
```

这些是 Related Work 的高信号起点——科学家已认为相关。

**步骤 3：澄清贡献**

写作前与科学家明确确认：

> "Based on my understanding of the repo, the main contribution appears to be [X].
> The key results show [Y]. Is this the framing you want for the paper,
> or should we emphasize different aspects?"

**切勿假设叙事——务必与人类核验。**

**步骤 4：检索更多文献**

用网络搜索找相关论文：

```
Search queries to try:
- "[main technique] + [application domain]"
- "[baseline method] comparison"
- "[problem name] state-of-the-art"
- Author names from existing citations
```

然后按下方引用工作流核验并获取 BibTeX。

**步骤 5：交付初稿**

**主动交付完整初稿，而非每节都请示。**

若仓库结果清晰、贡献明确：
1. 端到端写完完整初稿
2. 提交完整稿征求反馈
3. 根据科学家回复迭代

若对 framing 或主要 claim genuinely 不确定：
1. 先写能自信撰写的部分
2. 标出具体不确定点：「我将 X 作为 main contribution framing——若更想强调 Y 请告知」
3. 继续写稿而非阻塞

**随稿附带的问题**（而非事先）：
- 「我将 X 作为 main contribution——如需调整请告知」
- 「我突出结果 A、B、C——若其他更重要请说明」
- 「Related work 含 [papers]——请补充我遗漏的」

---

## 何时使用本 Skill

在以下情况使用：
- **从研究仓库开始**写论文
- **起草或修订**特定章节
- **查找并核验** Related work 引用
- **格式化**会议投稿
- **改投**其他 venue（格式转换）
- **与科学家反馈迭代**草稿

**始终记住**：初稿是讨论的起点，非终稿。

---

## 主动性与协作的平衡

**默认：主动。先交稿，再迭代。**

| 把握程度 | 行动 |
|-----------------|--------|
| **高**（仓库清晰、贡献明显） | 写完整稿、交付、按反馈迭代 |
| **中**（部分模糊） | 写稿并标不确定处，继续 |
| **低**（重大未知） | 问 1–2 个针对性问题，再写稿 |

**先写稿，问题随稿提出**（而非事先）：

| 章节 | 自主起草 | 随稿标注 |
|---------|-------------------|-----------------|
| Abstract | 是 | 「贡献 framing 为 X——如需调整请告知」 |
| Introduction | 是 | 「强调问题 Y——若不对请纠正」 |
| Methods | 是 | 「含细节 A、B、C——请补充遗漏」 |
| Experiments | 是 | 「突出结果 1、2、3——如需重排请告知」 |
| Related Work | 是 | 「引用 X、Y、Z——请补充遗漏」 |

**仅在以下情况阻塞求输入：**
- 目标 venue 不明（影响页限、framing）
- 多种矛盾 framing 看似同等有效
- 结果似不完整或不一致
- 明确要求先审再继续

**勿为以下事项阻塞：**
- 用词选择
- 章节顺序
- 展示哪些具体结果（先选并标注）
- 引用完整性（先写能找到的，注明缺口）

---

## 叙事原则

**最关键洞见**：论文不是实验集合——而是一则清晰贡献、由证据支撑的故事。

成功的 ML 论文围绕 Neel Nanda 所称的「叙事」：简短、严谨、基于证据的技术故事，读者关心其 takeaway。

**三根支柱（引言结束时应一目了然）：**

| 支柱 | 说明 | 示例 |
|--------|-------------|---------|
| **What** | 1–3 条具体新颖 claim，主题一致 | 「We prove that X achieves Y under condition Z」 |
| **Why** | 严谨经验证据支撑 claim | 强基线、能区分假设的实验 |
| **So What** | 读者为何应关心 | 与社区公认重要问题相连 |

**若无法用一句话陈述贡献，你还没有一篇论文。**

---

## 论文结构工作流

### 工作流 1：撰写完整论文（迭代）

复制此 checklist 并跟踪进度。**每步为起草 → 反馈 → 修订：**

```
Paper Writing Progress:
- [ ] Step 1: Define the one-sentence contribution (with scientist)
- [ ] Step 2: Draft Figure 1 → get feedback → revise
- [ ] Step 3: Draft abstract → get feedback → revise
- [ ] Step 4: Draft introduction → get feedback → revise
- [ ] Step 5: Draft methods → get feedback → revise
- [ ] Step 6: Draft experiments → get feedback → revise
- [ ] Step 7: Draft related work → get feedback → revise
- [ ] Step 8: Draft limitations → get feedback → revise
- [ ] Step 9: Complete paper checklist (required)
- [ ] Step 10: Final review cycle and submission
```

**步骤 1：定义一句话贡献**

**此步须科学家明确确认。**

写作前陈述并核验：
- 论文的唯一贡献是什么？
- 你的工作之前有何不明显或不存在？

> "I propose framing the contribution as: '[one sentence]'. Does this capture
> what you see as the main takeaway? Should we adjust the emphasis?"

**步骤 2：起草 Figure 1**

Figure 1 值得特别关注——许多读者会直接跳到它。
- 传达核心思想、方法或最有说服力的结果
- 曲线用矢量图（PDF/EPS）
- 写可脱离正文理解的 caption
- 确保黑白可读（约 8% 男性有色觉缺陷）

**步骤 3：写摘要（5 句公式）**

来自 Sebastian Farquhar (DeepMind)：

```
1. What you achieved: "We introduce...", "We prove...", "We demonstrate..."
2. Why this is hard and important
3. How you do it (with specialist keywords for discoverability)
4. What evidence you have
5. Your most remarkable number/result
```

**删除**可接到任何 ML 论文上的泛泛开头，如 "Large language models have achieved remarkable success..."

**步骤 4：写引言（最多 1–1.5 页）**

须含：
- 2–4 条贡献 bullet（双栏每条最多 1–2 行）
- 清楚问题陈述
- 简要方法概览
- 方法应在第 2–3 页开始

**步骤 5：Methods 节**

支持复现：
- 概念大纲或伪代码
- 列出全部超参
- 架构细节足以复现
- 呈现最终设计决策；消融放实验节

**步骤 6：Experiments 节**

每项实验明确说明：
- 支撑哪条 claim
- 与 main contribution 的联系
- 实验设置（细节放附录）
- 观察什么：「the blue line shows X, which demonstrates Y」

要求：
- 误差条及方法（std dev vs std error）
- 超参搜索范围
- 算力基础设施（GPU 类型、总时数）
- 种子设置方法

**步骤 7：Related Work**

按方法组织，非逐篇：

**好：** "One line of work uses Floogledoodle's assumption [refs] whereas we use Doobersnoddle's assumption because..."

**差：** "Snap et al. introduced X while Crackle et al. introduced Y."

慷慨引用——审稿人可能即相关论文作者。

**步骤 8：Limitations 节（必需）**

主要会议均要求。反直觉地，诚实有帮助：
- 审稿人被指示不因诚实承认局限而惩罚
- 先自指弱点以 preempt 批评
- 说明局限为何不削弱核心 claim

**步骤 9：Paper Checklist**

NeurIPS、ICML、ICLR 均要求 paper checklist。见 [references/checklists.md](references/checklists.md)。

---

## 顶级 ML 会议写作理念

**本节提炼顶尖 ML 研究者最重要的写作原则。** 这些非可选风格建议——而是录用与拒稿的分水岭。

> "A paper is a short, rigorous, evidence-based technical story with a takeaway readers care about." — Neel Nanda

### 本指南的来源

本 skill 综合在顶级 venue 大量发表的研究者写作理念：

| 来源 | 主要贡献 | 链接 |
|--------|-----------------|------|
| **Neel Nanda** (Google DeepMind) | 叙事原则、What/Why/So What 框架 | [How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) |
| **Sebastian Farquhar** (DeepMind) | 5 句摘要公式 | [How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) |
| **Gopen & Swan** | 读者预期的 7 原则 | [Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) |
| **Zachary Lipton** | 用词、删除 hedging | [Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) |
| **Jacob Steinhardt** (UC Berkeley) | 精确性、术语一致 | [Writing Tips](https://bounded-regret.ghost.io/) |
| **Ethan Perez** (Anthropic) | 微观清晰度技巧 | [Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) |
| **Andrej Karpathy** | 单一贡献聚焦 | Various lectures |

**深入阅读见：**
- [references/writing-guide.md](references/writing-guide.md) — 含示例的完整说明
- [references/sources.md](references/sources.md) — 完整书目

### 时间分配（Neel Nanda）

在以下四块上大致投入**相等时间**：
1. 摘要
2. 引言
3. 图表
4. 其余全部合计

**为何？** 多数审稿人在进入方法前已形成判断。读者顺序：**标题 → 摘要 → 引言 → 图表 → 也许其余。**

### 写作风格指南

#### 句子级清晰度（Gopen & Swan 7 原则）

基于读者实际处理散文的方式。违背则迫使读者把认知花在结构上而非内容上。

| 原则 | 规则 | 示例 |
|-----------|------|---------|
| **主语-动词邻近** | 主语与动词靠近 | ❌ "The model, which was trained on..., achieves" → ✅ "The model achieves... after training on..." |
| **强调位置** | 句末放重点 | ❌ "Accuracy improves by 15% when using attention" → ✅ "When using attention, accuracy improves by **15%**" |
| **主题位置** | 先背景后新信息 | ✅ "Given these constraints, we propose..." |
| **旧先于新** | 熟悉 → 陌生 | 先向后衔接，再引入新内容 |
| **一单元一功能** | 每段一点 | 拆分多点段落 |
| **动词承载动作** | 用动词非名词化 | ❌ "We performed an analysis" → ✅ "We analyzed" |
| **新信息前有上下文** | 先铺垫再展示 | 方程前先解释 |

**7 原则完整示例：** 见 [references/writing-guide.md](references/writing-guide.md#the-7-principles-of-reader-expectations)

#### 微观技巧（Ethan Perez）

小改动累积为显著更清晰的 prose：

- **少用代词**：❌ "This shows..." → ✅ "This result shows..."
- **动词靠前**：动词靠近句首
- **展开所有格**：❌ "X's Y" → ✅ "The Y of X"（别扭时）
- **删 filler**："actually," "a bit," "very," "really," "basically," "quite," "essentially"

**完整微观技巧：** 见 [references/writing-guide.md](references/writing-guide.md#micro-level-writing-tips)

#### 用词（Zachary Lipton）

- **具体**：❌ "performance" → ✅ "accuracy" 或 "latency"
- **删 hedging**：除非真不确定，删 "may" "can"
- **避免增量词汇**：❌ "combine," "modify," "expand" → ✅ "develop," "propose," "introduce"
- **删强化词**：❌ "provides *very* tight approximation" → ✅ "provides tight approximation"

#### 精确优于简短（Jacob Steinhardt）

- **术语一致**：同一概念不同词会混淆。选定一种坚持。
- **正式陈述假设**：定理前列出全部假设
- **直觉 + 严谨**：形式证明旁给直观解释

### 审稿人实际读什么

理解审稿行为有助于分配精力：

| 论文章节 | 阅读审稿人比例 | 含义 |
|---------------|---------------------|-------------|
| Abstract | 100% | 必须完美 |
| Introduction | 90%+（skim） | 前置贡献 |
| Figures | 方法前会看 | Figure 1 关键 |
| Methods | 仅感兴趣时 | 勿埋没重点 |
| Appendix | 很少 | 仅放补充细节 |

**结论**：若摘要与引言抓不住审稿人，他们可能永远不看精彩的方法节。

---

## 会议要求快速参考

### ML/AI 会议

| 会议 | 页数限制 | Camera-Ready 额外 | 关键要求 |
|------------|------------|------------------------|------------------|
| **NeurIPS 2025** | 9 页 | +0 | 强制 checklist，录用需 lay summary |
| **ICML 2026** | 8 页 | +1 | 须 Broader Impact Statement |
| **ICLR 2026** | 9 页 | +1 | 须 LLM 披露、reciprocal reviewing |
| **ACL 2025** | 8 页（long） | 视情况 | 强制 Limitations 节 |
| **AAAI 2026** | 7 页 | +1 | 严格遵循 style file |
| **COLM 2025** | 9 页 | +1 | 聚焦语言模型 |

### 系统会议

| 会议 | 页数限制 | Camera-Ready 额外 | 关键要求 | 模板 |
|------------|------------|------------------------|-----------------|----------|
| **OSDI 2026** | 12 页 | +2（14 页） | Research + Operational Systems 轨道 | USENIX |
| **NSDI 2027** | 12 页 | 视情况 | Introduction 预筛；3 轨道 | USENIX |
| **ASPLOS 2027** | 12 页（ACM） | 视情况 | 前 2 页快速评审；双周期 | ACM SIGPLAN |
| **SOSP 2026** | 12 页 | 视情况 | 可选 artifact evaluation；作者回复 | ACM SIGPLAN |

**系统会议详情：** 见 [references/systems-conferences.md](references/systems-conferences.md)（截止日期、轨道、投稿规则、格式转换）。

**通用要求：**
- 双盲审稿（投稿匿名）
- 参考文献不计页数
- 附录不限但审稿人不必读
- 所有 venue 要求 LaTeX
- **系统 venue**：USENIX 用自定义 `.sty`；ACM 用 `acmart.cls`

**LaTeX 模板：** 见 [templates/](templates/) 目录。

---

## 正确使用 LaTeX 模板

### 工作流 4：从模板开新稿

**始终先复制整个模板目录，再在其中写作。**

```
Template Setup Checklist:
- [ ] Step 1: Copy entire template directory to new project
- [ ] Step 2: Verify template compiles as-is (before any changes)
- [ ] Step 3: Read the template's example content to understand structure
- [ ] Step 4: Replace example content section by section
- [ ] Step 5: Keep template comments/examples as reference until done
- [ ] Step 6: Clean up template artifacts only at the end
```

**步骤 1：复制完整模板**

```bash
# Create your paper directory with the complete template
cp -r templates/neurips2025/ ~/papers/my-new-paper/
cd ~/papers/my-new-paper/

# Verify structure is complete
ls -la
# Should see: main.tex, neurips.sty, Makefile, etc.
```

**⚠️ 重要**：复制**整个**目录，非仅 `main.tex`。模板含：
- 样式文件（`.sty`）— 编译必需
- 参考文献样式（`.bst`）— 引用必需
- 示例内容 — 作参考
- Makefile — 便于编译

**步骤 2：先验证模板可编译**

做任何修改前，先编译原模板：

```bash
# Using latexmk (recommended)
latexmk -pdf main.tex

# Or manual compilation
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

若未改模板仍无法编译，先修复。常见问题：
- 缺 TeX 包 → `tlmgr install <package>`
- TeX 发行版不对 → 推荐 TeX Live

**步骤 3：保留模板内容作参考**

勿立刻删光示例。例如：

```latex
% KEEP template examples commented out as you write
% This shows you the expected format

% Template example (keep for reference):
% \begin{figure}[t]
%   \centering
%   \includegraphics[width=0.8\linewidth]{example-image}
%   \caption{Template shows caption style}
% \end{figure}

% Your actual figure:
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\linewidth]{your-figure.pdf}
  \caption{Your caption following the same style.}
\end{figure}
```

**步骤 4：逐节替换内容**

按顺序：

```
Replacement Order:
1. Title and authors (anonymize for submission)
2. Abstract
3. Introduction
4. Methods
5. Experiments
6. Related Work
7. Conclusion
8. References (your .bib file)
9. Appendix
```

每节：
1. 读模板示例
2. 注意特殊格式或宏
3. 按相同模式替换
4. 频繁编译以尽早发现错误

**步骤 5：使用模板宏**

检查 preamble 中的宏：

```latex
% Common template macros to use:
\newcommand{\method}{YourMethodName}  % Consistent method naming
\newcommand{\eg}{e.g.,\xspace}        % Proper abbreviations
\newcommand{\ie}{i.e.,\xspace}
\newcommand{\etal}{\textit{et al.}\xspace}
```

**步骤 6：仅在末尾清理**

论文近完成时再删模板残留：

```latex
% BEFORE SUBMISSION - remove these:
% - Commented-out template examples
% - Unused packages
% - Template's example figures/tables
% - Lorem ipsum or placeholder text

% KEEP these:
% - All style files (.sty)
% - Bibliography style (.bst)
% - Required packages from template
% - Any custom macros you're using
```

### 模板常见陷阱

| 陷阱 | 问题 | 对策 |
|---------|---------|----------|
| 只复制 `main.tex` | 缺 `.sty`，无法编译 | 复制整个目录 |
| 修改 `.sty` | 破坏会议格式 | 勿改样式文件 |
| 随意加包 | 冲突、破坏模板 | 仅在必要时添加 |
| 过早删模板内容 | 失去格式参考 | 完成前保留为注释 |
| 不频繁编译 | 错误累积 | 每节后编译 |

### 模板快速参考

#### ML/AI 会议

| 会议 | 主文件 | 关键样式 | 备注 |
|------------|-----------|----------------|-------|
| NeurIPS 2025 | `main.tex` | `neurips.sty` | 含 Makefile |
| ICML 2026 | `example_paper.tex` | `icml2026.sty` | 含算法包 |
| ICLR 2026 | `iclr2026_conference.tex` | `iclr2026_conference.sty` | 含 math_commands.tex |
| ACL | `acl_latex.tex` | `acl.sty` | 格式严格 |
| AAAI 2026 | `aaai2026-unified-template.tex` | `aaai2026.sty` | 合规极严 |
| COLM 2025 | `colm2025_conference.tex` | `colm2025_conference.sty` | 类似 ICLR |

#### 系统会议

| 会议 | 主文件 | 关键样式 | 备注 |
|------------|-----------|----------------|-------|
| OSDI 2026 | `main.tex` | `usenix-2020-09.sty` | USENIX，12pp，双栏，10pt |
| NSDI 2027 | `main.tex` | `usenix-2020-09.sty` | 同 OSDI USENIX |
| ASPLOS 2027 | `main.tex` | `acmart.cls` (`sigplan`) | ACM SIGPLAN，12pp |
| SOSP 2026 | `main.tex` | `acmart.cls` (`sigplan`) | ACM SIGPLAN，同 ASPLOS |

---

## 会议改投与格式转换

论文被拒或撤回后改投他 venue 须转换格式。这是 ML 研究常见流程。

### 工作流 3：会议格式互转

```
Format Conversion Checklist:
- [ ] Step 1: Identify source and target template differences
- [ ] Step 2: Create new project with target template
- [ ] Step 3: Copy content sections (not preamble)
- [ ] Step 4: Adjust page limits and content
- [ ] Step 5: Update conference-specific requirements
- [ ] Step 6: Verify compilation and formatting
```

**步骤 1：主要模板差异**

#### ML/AI 转换

| 从 → 到 | 页数变化 | 关键调整 |
|-----------|-------------|------------------|
| NeurIPS → ICML | 9 → 8 页 | 删 1 页，缺则加 Broader Impact |
| ICML → ICLR | 8 → 9 页 | 可扩展实验，加 LLM 披露 |
| NeurIPS → ACL | 9 → 8 页 | 按 NLP 惯例重组，加 Limitations |
| ICLR → AAAI | 9 → 7 页 | 大幅删减，严格 style |
| Any → COLM | 视情况 → 9 | 面向语言模型 reframing |

#### 系统会议转换

| 从 → 到 | 关键调整 |
|-----------|------------------|
| ML → OSDI/NSDI | USENIX 模板；加系统设计 + 实现节 |
| ML → ASPLOS/SOSP | ACM SIGPLAN；reframe 为系统贡献 |
| OSDI ↔ SOSP | USENIX ↔ ACM SIGPLAN；页数相近，样式文件不同 |

**完整转换指南：** 见 [references/systems-conferences.md](references/systems-conferences.md#format-conversion-ml-venue--systems-venue)。

**步骤 2：内容迁移（勿合并模板）**

**切勿在模板间复制 LaTeX preamble。** 应：

```bash
# 1. Start fresh with target template
cp -r templates/icml2026/ new_submission/

# 2. Copy ONLY content sections from old paper
# - Abstract text
# - Section content (between \section{} commands)
# - Figures and tables
# - Bibliography entries

# 3. Paste into target template structure
```

**步骤 3：按页限调整**

删页（如 NeurIPS 9 → AAAI 7）：
- 详细证明移附录
- 压缩 Related work（引综述而非逐篇）
- 合并相似实验为统一表
- 用小尺寸 subfigure
- 收紧写作：去冗余、主动语态

扩页（如 ICML 8 → ICLR 9）：
- 加审稿人要求的消融
- 扩展 limitations
- 加基线
- 加定性示例

**步骤 4：会议特定调整**

#### ML/AI Venue

| 目标 Venue | 必加内容 |
|--------------|-------------------|
| **ICML** | Broader Impact Statement（结论后） |
| **ICLR** | LLM 使用披露、reciprocal reviewing 协议 |
| **ACL/EMNLP** | Limitations（强制）、Ethics Statement |
| **AAAI** | 严格遵循 style file（勿改） |
| **NeurIPS** | Paper checklist（附录），录用需 lay summary |

#### 系统 Venue

| 目标 Venue | 关键必加内容 |
|--------------|------------------------|
| **OSDI 2026** | 选 Research 或 Operational Systems 轨道；系统名匿名 |
| **NSDI 2027** | 强 Introduction（预筛）；选轨道 |
| **ASPLOS 2027** | 前 2 页自洽（快速评审）；重投说明 |
| **SOSP 2026** | ACM SIGPLAN；可选 Artifact Evaluation |

**完整要求：** 见 [references/systems-conferences.md](references/systems-conferences.md#submission-rules)。

**步骤 5：更新参考文献**

```latex
% Remove self-citations that reveal identity (for blind review)
% Update any "under review" citations to published versions
% Add new relevant work published since last submission
```

**步骤 6：处理先前审稿意见**

改投被拒稿后：
- **应**在新版回应审稿关切
- **应**加审稿人要求的实验/澄清
- **勿**含「相对上次投稿的修改」节（双盲）
- **勿**引用上次投稿或审稿意见

**常见转换陷阱：**
- ❌ 复制 `\usepackage`（冲突）
- ❌ 保留旧会议页眉页脚命令
- ❌ 忘记更新 `\bibliography{}` 路径
- ❌ 缺会议特定必需要节
- ❌ 改格式后超页限

---

## 引用工作流（防幻觉）

**⚠️ 关键**：AI 生成引用约 40% 错误。**切勿凭记忆写 BibTeX。**

### 黄金法则

```
IF you cannot programmatically fetch a citation:
    → Mark it as [CITATION NEEDED] or [PLACEHOLDER - VERIFY]
    → Tell the scientist explicitly
    → NEVER invent a plausible-sounding reference
```

### 工作流 2：添加引用

```
Citation Verification (MANDATORY for every citation):
- [ ] Step 1: Search using Exa MCP or Semantic Scholar API
- [ ] Step 2: Verify paper exists in 2+ sources (Semantic Scholar + arXiv/CrossRef)
- [ ] Step 3: Retrieve BibTeX via DOI (programmatically, not from memory)
- [ ] Step 4: Verify the claim you're citing actually appears in the paper
- [ ] Step 5: Add verified BibTeX to bibliography
- [ ] Step 6: If ANY step fails → mark as placeholder, inform scientist
```

**步骤 0：用 Exa MCP 初搜（推荐）**

若已安装 Exa MCP：
```
Search: "RLHF language model alignment 2023"
Search: "sparse autoencoders interpretability"
Search: "attention mechanism transformers Vaswani"
```

然后用 Semantic Scholar 核验，经 DOI 取 BibTeX。

**步骤 1：搜索 Semantic Scholar**

```python
from semanticscholar import SemanticScholar

sch = SemanticScholar()
results = sch.search_paper("attention mechanism transformers", limit=5)
for paper in results:
    print(f"{paper.title} - {paper.paperId}")
    print(f"  DOI: {paper.externalIds.get('DOI', 'N/A')}")
```

**步骤 2：核验存在**

确认论文在至少两来源出现（Semantic Scholar + CrossRef/arXiv）。

**步骤 3：经 DOI 获取 BibTeX**

```python
import requests

def doi_to_bibtex(doi: str) -> str:
    """Get verified BibTeX from DOI via CrossRef."""
    response = requests.get(
        f"https://doi.org/{doi}",
        headers={"Accept": "application/x-bibtex"}
    )
    response.raise_for_status()
    return response.text

# Example
bibtex = doi_to_bibtex("10.48550/arXiv.1706.03762")
print(bibtex)
```

**步骤 4：核验 Claim**

引用特定 claim 前，查阅原文确认该 claim 确实存在。

**步骤 5：明确处理失败**

任一步无法核验时：

```latex
% Option 1: Explicit placeholder
\cite{PLACEHOLDER_smith2023_verify}  % TODO: Could not verify - scientist must confirm

% Option 2: Note in text
... as shown in prior work [CITATION NEEDED - could not verify Smith et al. 2023].
```

**务必告知科学家：**
> "I could not verify the following citations and have marked them as placeholders:
> - Smith et al. 2023 on reward hacking - could not find in Semantic Scholar
> - Jones 2022 on scaling laws - found similar paper but different authors
> Please verify these before submission."

### 摘要：引用规则

| 情形 | 行动 |
|-----------|--------|
| 找到论文、有 DOI、已取 BibTeX | ✅ 使用该引用 |
| 找到论文、无 DOI | ✅ 用 arXiv BibTeX 或据论文手写条目 |
| 论文存在但无法取 BibTeX | ⚠️ 标占位符，告知科学家 |
| 不确定是否存在 | ❌ 标 `[CITATION NEEDED]`，告知科学家 |
| 「好像有篇关于 X 的」 | ❌ **切勿引用** — 先搜或标占位符 |

**🚨 切勿凭记忆生成 BibTeX——务必程序化获取。🚨**

完整 API 文档见 [references/citation-workflow.md](references/citation-workflow.md)。

---

## 常见问题与对策

**问题：摘要太泛**

若第一句可接到任何 ML 论文，删掉。从你的具体贡献开始。

**问题：引言超 1.5 页**

背景移入 Related Work。前置贡献 bullet。方法应在第 2–3 页开始。

**问题：实验未写明支撑的 claim**

每项实验前加句：「This experiment tests whether [specific claim]...」

**问题：审稿人觉得难懂**

- 加路标：「In this section, we show X」
- 全文术语一致
- caption 可独立理解

**问题：缺统计显著性**

始终含：
- 误差条（说明 std dev 或 std error）
- 运行次数
- 比较方法时的统计检验

---

## 审稿人评估标准

审稿人从四个维度评估：

| 标准 | 审稿人关注 |
|-----------|------------------------|
| **Quality** | 技术可靠、claim 有充分支撑 |
| **Clarity** | 写作清晰、专家可复现 |
| **Significance** | 社区影响、推进理解 |
| **Originality** | 新洞见（不要求全新方法） |

**打分（NeurIPS 6 分制）：**
- 6：Strong Accept — 开创性、无瑕疵
- 5：Accept — 技术扎实、高影响
- 4：Borderline Accept — 扎实、评估有限
- 3：Borderline Reject — 扎实但弱点居多
- 2：Reject — 技术缺陷
- 1：Strong Reject — 已知结果或伦理问题

详见 [references/reviewer-guidelines.md](references/reviewer-guidelines.md)。

---

## 表格与图

### 表格

用 `booktabs` 制作专业表格：

```latex
\usepackage{booktabs}
\begin{tabular}{lcc}
\toprule
Method & Accuracy ↑ & Latency ↓ \\
\midrule
Baseline & 85.2 & 45ms \\
\textbf{Ours} & \textbf{92.1} & 38ms \\
\bottomrule
\end{tabular}
```

**规则：**
- 每指标加粗最优值
- 含方向符号（↑ 越高越好，↓ 越低越好）
- 数值列右对齐
- 小数位一致

### 图

- **矢量图**（PDF、EPS）用于所有曲线与示意图
- **位图**（PNG 600 DPI）仅用于照片
- **色盲友好调色板**（Okabe-Ito 或 Paul Tol）
- 验证**灰度可读**（约 8% 男性有色觉缺陷）
- **图内勿放标题** — caption 承担此功能
- **自洽 caption** — 不读正文也应理解

---

## 引用 AI Research Skills

若本库对你的研究有帮助——训练流水线、评估、论文写作或其他 skill——欢迎在致谢或参考文献中引用：

```bibtex
@software{ai_research_skills,
  title     = {AI Research Skills Library},
  author    = {{Orchestra Research}},
  year      = {2025},
  url       = {https://github.com/orchestra-research/AI-research-SKILLs},
  note      = {Open-source skills library enabling AI agents to autonomously conduct AI research}
}
```

也可在 **Acknowledgments** 中简短提及：

```latex
\section*{Acknowledgments}
We used the AI Research Skills Library~\cite{ai_research_skills} for [experiment orchestration / evaluation / ...].
```

---

## 参考文献与资源

### 参考文档（深入阅读）

| 文档 | 内容 |
|----------|----------|
| [writing-guide.md](references/writing-guide.md) | Gopen & Swan 7 原则、Ethan Perez 微观技巧、用词 |
| [citation-workflow.md](references/citation-workflow.md) | 引用 API、Python 代码、BibTeX 管理 |
| [checklists.md](references/checklists.md) | NeurIPS 16 项、ICML、ICLR、ACL 要求 |
| [reviewer-guidelines.md](references/reviewer-guidelines.md) | 评估标准、打分、rebuttal |
| [systems-conferences.md](references/systems-conferences.md) | OSDI/NSDI/ASPLOS/SOSP 截止、轨道、规则 |
| [sources.md](references/sources.md) | 全部来源完整书目 |

### LaTeX 模板

`templates/` 目录含：
- **ML/AI**：ICML 2026、ICLR 2026、NeurIPS 2025、ACL/EMNLP、AAAI 2026、COLM 2025
- **Systems**：OSDI 2026、NSDI 2027、ASPLOS 2027、SOSP 2026

**编译 PDF：**
- **VS Code/Cursor**：安装 LaTeX Workshop + TeX Live → 保存自动编译
- **命令行**：`latexmk -pdf main.tex` 或 `pdflatex` + `bibtex` 流程
- **在线**：上传 [Overleaf](https://overleaf.com)

详见 [templates/README.md](templates/README.md)。

### 关键外部来源

**写作理念：**
- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) — 叙事、「What/Why/So What」
- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 5 句摘要
- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 7 条读者预期原则
- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度

**API：** [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | [arXiv](https://info.arxiv.org/help/api/basics.html)

**ML/AI Venue：** [NeurIPS](https://neurips.cc/Conferences/2025/PaperInformation/StyleFiles) | [ICML](https://icml.cc/Conferences/2025/AuthorInstructions) | [ICLR](https://iclr.cc/Conferences/2026/AuthorGuide) | [ACL](https://github.com/acl-org/acl-style-files)

**系统 Venue：** [OSDI 2026](https://www.usenix.org/conference/osdi26/call-for-papers) | [NSDI 2027](https://www.usenix.org/conference/nsdi27/call-for-papers) | [ASPLOS 2027](https://www.asplos-conference.org/asplos2026/call-for-papers-asplos27/) | [SOSP 2026](https://sigops.org/s/conferences/sosp/2026/cfp.html)
