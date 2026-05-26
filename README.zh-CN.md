# Paper Writing Suite

[English](README.md)

**把研究仓库变成可投稿的论文——有证据链，不靠幻觉。**

Paper Writing Suite 是一个面向 **ML / AI / CV / NLP** 的 agent skill：把你的代码、实验日志、笔记和会议模板交给 coding agent，它会帮你产出**可审计、有证据支撑**的 LaTeX 草稿与投稿材料，而不是“读起来很顺、但经不起追问”的 prose。

> **论文写作是 claim–evidence 工程，不是散文生成。**  
> 每个重要主张都应能追溯到代码、实验结果、笔记或已核验引用。

---

## 为什么用这个 skill

| 常见 AI 写论文方式 | Paper Writing Suite |
|---|---|
| 凭记忆写流畅段落 | 主张与仓库证据一一对应 |
| 引用猜造或编造 | 从 arXiv / DOI / Semantic Scholar 拉 BibTeX |
| 只出 figure 计划、不出图 | Overview / 方法图默认生成；数值图用确定性脚本 |
| 停在提纲 | 落地 `paper_story.md`、`claim_evidence_map.md`、`references.bib`、图文件 |
| 泛泛写作建议 | Venue checklist、审稿人视角自检、编译与打包门禁 |

**模板与 checklist 覆盖：** NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV、ACL、AAAI、COLM 等。正式投稿前务必核对[各会议官方说明](references/venue-templates.md)。

---

## 快速开始

**1. 安装**（软链到 agent 的 skills 目录）：

```bash
git clone https://gitlab.tetras.ai/jinsheng/paper-writing-suite.git
ln -s "$(pwd)/paper-writing-suite" ~/.cursor/skills/paper-writing-suite   # Cursor 全局
```

更多 agent 路径见下方 [安装](#安装)。

**2. 在论文仓库里对 agent 说：**

```text
Use paper-writing-suite to inspect this repo and create paper_story.md and claim_evidence_map.md.
```

**3. 按章节迭代**，例如：

```text
Use paper-writing-suite to revise Related Work: build a literature inventory and positioning analysis before drafting.
```

```text
Use paper-writing-suite to plan Figure 1 (method overview), generate the figure asset, and wire it into main.tex.
```

内置脚本仅依赖 **Python 3 标准库**，无需额外安装。

---

## 你能得到什么

从选题叙事到 camera-ready 的完整链路：

| 阶段 | 典型产出 |
|---|---|
| **叙事** | 论点、缺口、贡献、应回避的 claim |
| **证据** | 与代码 / 日志 / 表格绑定的 `claim_evidence_map.md` |
| **写作** | Abstract、Introduction、Related Work、Method、Experiments、Limitations、Conclusion |
| **文献** | 本地语料、定位分析、核验后的 `references.bib` |
| **图表** | 计划 + 文件：**生成图**作 overview / 方法示意；**确定性绘图**承载数值结果 |
| **审稿** | 审稿人视角风险、拒稿点诊断、作者自检 |
| **投稿** | Venue checklist、LaTeX 编译检查、TODO / 引用审计、打包 |

### 工作模式

Agent 按任务只加载需要的 reference，避免“一口气读完整个 `references/`”：

| 模式 | 适用场景 |
|---|---|
| Full-paper | 仓库 + 实验 + 模板 → 草稿或投稿包 |
| Story | 厘清 thesis、gap、贡献边界 |
| Section | 单节修订（加载对应写作指南） |
| Figure | 规划并**实际产出**示意图与结果图 |
| Citation | 检索、核验、修复 BibTeX |
| Reviewer | 投稿前风险扫描 |
| Submission | Checklist、build log、camera-ready |
| Automation | 调用 `scripts/` 做批量检查 |

细则见 [`SKILL.md`](SKILL.md) 与 [`references/README.md`](references/README.md)。

### 内置质量门禁

Skill 要求 agent 不能跳过的检查点：

- **证据** — 数值来自数据 / 日志 / 脚本，而非图像模型  
- **叙事** — 贡献未明确前不写全文草稿  
- **文献** — Related Work 前先完成定位与语料  
- **引用** — 未核验 BibTeX 必须标为 placeholder  
- **图表** — 概念图默认**图像生成**进稿；TikZ/SVG 仅作可选参考  
- **审稿** — 高风险 objection 未处理前不算完成  
- **编译** — 尝试编译或记录阻塞原因  

---

## 安装

克隆本仓库后，复制或软链到对应 agent 的 skills 目录。

| Agent | 全局路径 |
|---|---|
| **Cursor** | `~/.cursor/skills/paper-writing-suite` |
| **Codex** | `$CODEX_HOME/skills/paper-writing-suite` |
| **Claude Code** | `$HOME/.claude/skills/paper-writing-suite` |
| **Gemini** | `$HOME/.gemini/skills/paper-writing-suite` |

### Cursor

全局：

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/paper-writing-suite ~/.cursor/skills/paper-writing-suite
```

项目级：

```bash
mkdir -p .cursor/skills
ln -s /path/to/paper-writing-suite .cursor/skills/paper-writing-suite
```

### Codex

```bash
mkdir -p "$CODEX_HOME/skills"
ln -s /path/to/paper-writing-suite "$CODEX_HOME/skills/paper-writing-suite"
```

### Claude Code

全局：

```bash
mkdir -p "$HOME/.claude/skills"
ln -s /path/to/paper-writing-suite "$HOME/.claude/skills/paper-writing-suite"
```

项目级：将路径改为 `.claude/skills/` 即可。

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
ln -s /path/to/paper-writing-suite "$HOME/.gemini/skills/paper-writing-suite"
```

---

## 仓库结构

```text
paper-writing-suite/
├── SKILL.md              # Agent 入口：模式、门禁、证据策略
├── references/           # 工作流、写作、引用、图表、venue、审稿
│   └── assets/           # 结果图版式参考（figures4papers 风格）
├── scripts/              # Claim、引用、TODO、编译日志、camera-ready 检查
├── templates/            # NeurIPS / ICML / CVPR / ACL / … LaTeX 模板
└── README.md
```

**深入阅读推荐：**

| 文件 | 作用 |
|---|---|
| [`references/workflow.md`](references/workflow.md) | 全文工作流状态机 |
| [`references/artifacts.md`](references/artifacts.md) | 论文仓库里应落盘的产物契约 |
| [`references/figure-workflow.md`](references/figure-workflow.md) | 示意图 vs 结果图；生成图默认策略 |
| [`references/citation-workflow.md`](references/citation-workflow.md) | 检索、核验、BibTeX |
| [`templates/README.md`](templates/README.md) | 模板列表与编译说明 |

---

## 辅助脚本

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
```

详见 [`scripts/README.md`](scripts/README.md)。

---

## 使用注意

- 内置模板仅为便利副本，**正式投稿前必须核对官方 venue 要求**。  
- 勿将私有 PDF、专有实验日志、API key 或审稿保密材料提交进仓库。

---

## 致谢

本项目参考并借鉴了以下开源 skill 项目的思路与组织方式：

- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)
- [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)

## License

MIT License。
