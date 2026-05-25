# 系统会议指南：OSDI、NSDI、ASPLOS、SOSP

本参考文档提供顶级系统会议的全面信息，包括截止日期、格式要求、轨道说明与投稿策略。

---

## 会议概览

| 会议 | 全称 | 页数限制 | 模板 | 轨道 |
|------------|-----------|------------|----------|--------|
| **OSDI 2026** | 第 20 届 USENIX 操作系统设计与实现研讨会 | 12 页（camera-ready +2） | USENIX `usenix-2020-09.sty` | Research + Operational Systems |
| **NSDI 2027** | 第 24 届 USENIX 网络系统设计与实现研讨会 | 12 页 | USENIX `usenix-2020-09.sty` | Research / Frontiers / Operational |
| **ASPLOS 2027** | ACM 编程语言与操作系统体系结构支持国际会议 | 12 页（ACM） | ACM SIGPLAN `acmart.cls` | 单轨，双评审周期 |
| **SOSP 2026** | 第 32 届 ACM 操作系统原理研讨会 | 12 页 | ACM SIGPLAN `acmart.cls` | 单轨 |

> **OSDI 2026**：新增「Operational Systems」轨道。每位作者最多 8 篇投稿。鼓励合适篇幅（勿为凑满 12 页而注水）。目标录用率 ≥20%。无作者回复期；以「conditional accept」替代 major revision。
>
> **NSDI 2027**：两个截止日期（春/秋）。新增「Frontiers Track」面向雄心勃勃、前瞻性的想法。所有论文经 Introduction 预筛。被拒论文可能获得一次性修改机会。
>
> **ASPLOS 2027**：两个周期（4 月/9 月）。新增快速评审轮（仅审前 2 页）。评估对体系结构/PL/OS 核心领域的贡献。每周期每位作者最多 4 篇。
>
> **SOSP 2026**：ACM SIGPLAN 格式。可选 Artifact Evaluation。双盲审稿。鼓励突破性研究方向。

---

## 截止日期与关键日期

### OSDI 2026（美国华盛顿州西雅图 | 2026 年 7 月 13–15 日）

| 里程碑 | 日期 |
|-----------|------|
| 摘要注册 | 2025 年 12 月 4 日，美东 5:59 PM |
| 全文投稿 | 2025 年 12 月 11 日，美东 5:59 PM |
| 通知 | 2026 年 3 月 26 日 |
| Camera-ready | 2026 年 6 月 9 日 |

### NSDI 2027（美国罗德岛州普罗维登斯 | 2027 年 5 月 11–13 日）

**春季截止：**

| 里程碑 | 日期 |
|-----------|------|
| 标题与摘要 | 2026 年 4 月 16 日，美东 11:59 PM |
| 全文 | 2026 年 4 月 23 日，美东 11:59 PM |
| 通知 | 2026 年 7 月 23 日 |
| Camera-ready | 2026 年 10 月 20 日 |

**秋季截止：**

| 里程碑 | 日期 |
|-----------|------|
| 标题与摘要 | 2026 年 9 月 10 日，美东 11:59 PM |
| 全文 | 2026 年 9 月 17 日，美东 11:59 PM |
| 通知 | 2026 年 12 月 8 日 |
| Camera-ready | 2027 年 3 月 4 日 |

### ASPLOS 2027

**4 月周期：**

| 里程碑 | 日期 |
|-----------|------|
| 全文投稿 | 2026 年 4 月 15 日（AoE） |
| 作者回复 | 2026 年 7 月 6–9 日 |
| 通知 | 2026 年 7 月 27 日 |

**9 月周期：**

| 里程碑 | 日期 |
|-----------|------|
| 全文投稿 | 2026 年 9 月 9 日（AoE） |
| 作者回复 | 2026 年 12 月 1–4 日 |
| 通知 | 2026 年 12 月 21 日 |

### SOSP 2026（2026 年 9 月 30 日）

| 里程碑 | 日期 |
|-----------|------|
| 摘要注册 | 2026 年 3 月 26 日（AoE） |
| 全文投稿 | 2026 年 4 月 1 日（AoE） |
| 通知 | 2026 年 7 月 3 日 |
| Camera-ready | 2026 年 8 月 28 日 |
| 研讨会 | 2026 年 9 月 29 日 |
| 会议 | 2026 年 9 月 30 日 |

---

## 轨道说明

### OSDI 2026 轨道

**Research Track**：面向操作系统设计、实现、分析、评估与部署的广泛兴趣。主题包括：
- 操作系统及其与硬件/软件的交互，以及作为其他系统基石的角色
- 虚拟化，包括虚拟机监视器、hypervisor、OS 级虚拟化
- 文件与存储系统、分布式系统、云计算
- 机器学习/AI 系统、安全与隐私、嵌入式/实时系统

**Operational Systems Track**（新增）：
- 描述已部署、在运系统及其宝贵经验的论文
- 标题须以「(Operational Systems)」结尾
- 评判侧重部署洞见而非新颖性

### NSDI 2027 轨道

**Research Track**：网络系统设计与实现的原创研究。

**Frontiers Track**（新增）：
- 面向网络系统中雄心勃勃、前瞻性的想法
- 评估可不够完整，但须呈现有说服力的愿景

**Operational Track**：大规模部署的系统及运营洞见。

### ASPLOS 2027 评审流程

**Rapid Review Round**（新增）：
- 审稿人**仅**阅读前 2 页以决定是否进入全文评审
- 前 2 页须自洽：问题、方法、关键结果、贡献
- 未通过快速评审的论文将收到简要反馈并被拒

**Full Review Round**：
- 标准双盲全文评审
- 作者回复期
- 可提供 Major revision（非仅接收/拒绝）

### SOSP 2026 特点

- **Artifact Evaluation**（可选但鼓励）：提交制品以支持可复现性
- **Author Response**：500 词限制，不允许新实验

---

## 格式要求

### USENIX 格式（OSDI、NSDI）

```latex
% USENIX format setup
\documentclass[letterpaper,twocolumn,10pt]{article}
\usepackage{usenix-2020-09}

% Key specifications:
% - Paper size: US Letter (8.5" x 11")
% - Font: Times Roman, 10pt on 12pt leading
% - Text block: 7" x 9"
% - Two columns, 0.33" column separation
% - Page limit: 12 pages (excluding references)
```

### ACM SIGPLAN 格式（ASPLOS、SOSP）

```latex
% ACM SIGPLAN format setup
\documentclass[sigplan,10pt]{acmart}

% For submission (hide copyright block):
\setcopyright{none}
\settopmatter{printfolios=true, printccs=false, printacmref=false}
\renewcommand\footnotetextcopyrightpermission[1]{}

% Key specifications:
% - Paper size: US Letter
% - Font: 10pt
% - Text block: 178mm x 229mm
% - Two columns
% - Page limit: 12 pages (excluding references)
```

---

## 投稿规则

### OSDI 2026

- **每位作者最多投稿**：8 篇
- **无作者回复期**
- **Conditional accept** 替代 major revision
- **匿名化**：系统名称须与 arXiv/报告不同
- **篇幅**：鼓励按需缩短（勿为凑满 12 页而注水）
- **AI 政策**：允许生成式 AI 工具但须披露；AI 不得列为作者

### NSDI 2027

- **Introduction 预筛**：所有论文先根据 Introduction 质量评估
- **One-shot revision**：被拒论文可能获得修改机会
- **双截止**：春季（2026 年 4 月）+ 秋季（2026 年 9 月）
- **轨道选择**：投稿时须选择 Research、Frontiers 或 Operational

### ASPLOS 2027

- **每周期每位作者最多**：4 篇
- **快速评审**：初期仅审前 2 页
- **双周期**：4 月 + 9 月
- **重投说明**：若曾投 ASPLOS 须提供
- **须推进**：体系结构、编程语言或操作系统研究

### SOSP 2026

- **Artifact Evaluation**：可选但推荐
- **作者回复**：500 词限制，无新实验
- **匿名系统名**：须与公开版本不同
- **双盲**：作者不可识别

---

## 格式转换：ML 会议 → 系统会议

将 ML 会议论文转为系统会议时，变更不止换模板：

| 方面 | ML 会议 | 系统会议 | 行动 |
|-------|----------|---------------|--------|
| **页数限制** | 7–9 页 | 12 页 | 补充系统设计细节 |
| **评估** | 基准、消融 | 端到端 + 微基准 | 增加系统级评估 |
| **贡献 framing** | 算法新颖性 | 系统设计 + 实现 | 重构为系统贡献 |
| **实现** | 常居次要 | 核心贡献 | 详述架构与优化 |
| **部署** | 少见 | 高度重视（尤其 OSDI/NSDI） | 补充部署经验 |

### 具体转换路径

| 从 → 到 | 关键调整 |
|-----------|------------------|
| ML → OSDI | USENIX 模板；系统视角重构；补充设计/实现；强调部署 |
| ML → NSDI | USENIX 格式；强调网络系统；选择轨道 |
| ML → ASPLOS | ACM SIGPLAN；前 2 页自洽（快速评审）；面向 arch/PL/OS |
| ML → SOSP | ACM SIGPLAN；强调 OS 原理；系统设计/评估 |
| OSDI ↔ SOSP | USENIX ↔ ACM SIGPLAN；页数相近 |
| OSDI ↔ NSDI | 同为 USENIX；调整范围（通用 vs 网络） |

---

## 系统论文结构

典型系统论文结构（与 ML 论文不同）：

```text
1. Introduction          - 问题、方法、关键结果（对 NSDI 预筛 / ASPLOS 快速评审至关重要）
2. Background/Motivation - 系统背景、现有方案为何不足
3. Design                - 系统架构、关键设计决策
4. Implementation        - 实现细节、优化、工程挑战
5. Evaluation            - 端到端性能 + 微基准 + 可扩展性
6. Discussion            - 局限性、部署经验（可选，SOSP 重视）
7. Related Work          - 按方法组织，非按时间
8. Conclusion            - 贡献与影响总结
```

**与 ML 论文的主要差异**：
- **Design** 取代 Methods：侧重架构与权衡
- **Implementation** 是核心贡献，非附庸
- **Evaluation** 含宏观（端到端）与微观基准
- **Discussion** 较常见（尤其 SOSP）

---

## 官方 CFP 链接

- **OSDI 2026**: <https://www.usenix.org/conference/osdi26/call-for-papers>
- **NSDI 2027**: <https://www.usenix.org/conference/nsdi27/call-for-papers>
- **ASPLOS 2027**: <https://www.asplos-conference.org/asplos2026/call-for-papers-asplos27/>
- **SOSP 2026**: <https://sigops.org/s/conferences/sosp/2026/cfp.html>
- **USENIX LaTeX Template**: <https://www.usenix.org/conferences/author-resources/paper-templates>
- **ACM SIGPLAN Template**: <https://www.acm.org/publications/proceedings-template>
