# AI Research Writing Skill

[English](README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: stdlib only](https://img.shields.io/badge/Python-stdlib%20only-blue.svg)](scripts/README.md)
[![Entrypoint](https://img.shields.io/badge/Entrypoint-SKILL.md-purple.svg)](SKILL.md)
[![LaTeX templates](https://img.shields.io/badge/Templates-NeurIPS%20%7C%20ICML%20%7C%20ICLR%20%7C%20CVPR%20%7C%20ACL-orange.svg)](templates/README.md)

把一个 ML/AI 研究仓库，变成**有证据链、可编译、可投稿的会议论文草稿**。

把代码、实验日志、笔记和会议模板交给 coding agent。这个 skill 会引导它产出可审计的 LaTeX 草稿与投稿材料：论文叙事、claim-evidence map、核验引用、图表、审稿人式评审意见、拒稿风险和 build notes。

> **论文写作是 claim–evidence 工程，不是散文生成。**  
> 每个重要主张都应能追溯到代码、实验结果、笔记或已核验引用。

![AI Research Writing Skill teaser](examples/paper-about-ai-research-writing-skill/paper/figures/teaser_imagegen.png)

---

## 端到端 Demo

```text
使用 AI Research Writing Skill 给这个仓库本身写一篇完整的系统论文。
把 ai-research-writing-skill 当作研究对象。
检查 SKILL.md、references/、scripts/、templates/、examples/ 和 README。
创建 paper_story.md、claim_evidence_map.md、literature positioning、已核验引用、ICML 风格方法图与表格，并在 examples/paper-about-ai-research-writing-skill/paper/ 下生成可编译的 ICML LaTeX 论文。
不要编造性能数字。只使用仓库事实作为证据。
```

这个 example 已经包含预期的最终论文包，所以你可以直接查看端到端输出会长什么样：

- **查看生成的 ICML 风格论文 PDF：** [`paper/main.pdf`](examples/paper-about-ai-research-writing-skill/paper/main.pdf)
- `evidence/repository_inventory.md`：作为证据的仓库事实。
- `paper_story.md` 和 `claim_evidence_map.md`：论文叙事与 claim 边界。
- `literature/positioning.md` 和 `citation_verification.md`：相关项目定位。
- `paper/figures/method_overview.tex` 和 `paper/tables/*.tex`：ICML 风格论文图表资产。
- `paper/main.tex`：关于本项目的完整论文草稿。
- `paper/main.pdf`：已编译论文，方便直接判断生成质量。
- `build_check.md`：编译命令、预期结果和剩余风险。

![AI Research Writing Skill method overview](examples/paper-about-ai-research-writing-skill/paper/figures/overview_imagegen.png)

## 用户使用路径

你可以在研究项目的不同阶段使用这个 skill。先看自己手上有什么，再选择对应的入口。

| 使用路径 | 你手上有什么 | 可以让 agent 做什么 |
|---|---|---|
| **头脑风暴与规划** | 一个选题、粗略想法或可能的方法 | 梳理论文 thesis、研究 gap、贡献边界、需要补的证据，以及下一步实验/写作计划。 |
| **从 repo 到完整论文** | 思路、方案设计、代码、笔记、实验 log、中间结果或会议模板 | 生成 `paper_story.md`、`claim_evidence_map.md`、文献定位、图、表、BibTeX、LaTeX 草稿和 build check。 |
| **初稿审稿式检查** | 已有完整或部分论文初稿 | 扮演严格审稿人，写 reviewer-style comments，扫描拒稿风险，并把主要问题转成具体修改动作。 |
| **论文修订 revise** | 已有稿件、已知弱点、审稿意见或某个待改章节 | 按章节或整篇修订，保留有证据支撑的 claim，弱化不可靠 claim，修复引用，改进图表并更新 LaTeX 包。 |
| **图表生成与接入** | 实验结果、日志、CSV、方法说明或粗略 figure 想法 | 产出 figure/table plan、生成 overview/method 图、确定性结果图/表、caption，并接入 LaTeX。 |
| **投稿前检查** | 接近完成的论文包 | 运行引用、占位符、build、venue checklist、审稿风险、打包和 Overleaf/Git handoff 检查。 |

可直接复制的 prompt：

```text
我现在只有一个粗略想法。请使用 AI Research Writing Skill 帮我做论文头脑风暴：梳理 paper story、研究 gap、可以声称和不能声称的 claim，并制定证据、实验、图表和写作计划。
```

```text
我有代码、笔记、方案设计和一些实验 log / 结果。请使用 AI Research Writing Skill 端到端生成完整论文包：paper_story.md、claim_evidence_map.md、文献定位、核验 BibTeX、图、表、LaTeX 草稿和 build_check.md。
```

```text
我已经有论文初稿。请使用 AI Research Writing Skill 扮演严格的 ICML 审稿人，写详细 reviewer comments，指出拒稿风险，并把高风险问题转成具体修改建议。
```

```text
我已经有论文稿件，想进行 revise。请使用 AI Research Writing Skill 按章节改进论文，保留有证据支撑的 claim，弱化不可靠 claim，修复引用，改进图表，并更新 LaTeX 包。
```

## 为什么用这个 skill

| 常见 AI 写论文方式 | AI Research Writing Skill |
|---|---|
| 凭记忆写流畅段落 | 主张与仓库证据一一对应 |
| 引用猜造或编造 | 从 arXiv / DOI / Semantic Scholar 拉 BibTeX |
| 只出 figure 计划、不出图 | Overview / 方法图默认生成；数值图用确定性脚本 |
| 停在提纲 | 落地 `paper_story.md`、`claim_evidence_map.md`、`references.bib`、图文件 |
| 泛泛写作建议 | 审稿人式 comments、拒稿风险诊断、Venue checklist、编译与打包门禁 |

**模板与 checklist 覆盖：** NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV、ACL、AAAI、COLM 等。正式投稿前务必核对[各会议官方说明](references/venue-templates.md)。

## Before / After

| 使用前 | 使用后 |
|---|---|
| 笔记、日志、草稿散落各处 | `paper_story.md` 和任务包明确边界 |
| claim 听起来合理，但证据不清 | `claim_evidence_map.md` 记录证据状态 |
| 凭记忆补引用 | 从权威元数据获取或核验 BibTeX |
| 只有 figure 想法 | 生成概念图，数值图用确定性脚本 |
| “看起来写完了” | 审稿人式批评、build、TODO、引用和投稿检查 |

## 你能得到什么

从选题叙事到 camera-ready 的完整链路：

| 阶段 | 典型产出 |
|---|---|
| **叙事** | 论点、缺口、贡献、应回避的 claim |
| **证据** | 与代码 / 日志 / 表格绑定的 `claim_evidence_map.md` |
| **写作** | Abstract、Introduction、Related Work、Method、Experiments、Limitations、Conclusion |
| **文献** | 本地语料、定位分析、核验后的 `references.bib` |
| **图表** | 计划 + 文件：**生成图**作 overview / 方法示意；**确定性绘图**承载数值结果 |
| **审稿** | 审稿人式 comments、拒稿风险诊断、作者自检、具体修改计划 |
| **投稿** | Venue checklist、LaTeX 编译检查、TODO / 引用审计、打包 |

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

**最简单的判断：**唯一规范入口是根目录 [`SKILL.md`](SKILL.md)。  
仓库里的其他内容都是 skill 按需加载的辅助材料：`references/`、`scripts/`、`templates/` 和 `examples/`。

### 让 Agent 自动安装

你可以直接让自己的 agent 按平台习惯安装这个仓库：

```text
请把 https://github.com/jin-s13/ai-research-writing-skill 安装成本地 skill。
使用仓库根目录 SKILL.md 作为唯一规范入口。
如果你的平台需要 skills 目录，请把整个仓库复制或软链进去。
```

### 手动安装

```bash
git clone https://github.com/jin-s13/ai-research-writing-skill.git
# 然后把整个仓库复制或软链到你的 agent 本地 skills 目录。
```

也可以不安装，直接打开本仓库后对 agent 说：

```text
请使用本仓库里的 AI Research Writing Skill。
遵循 SKILL.md，并且只加载当前任务需要的 references。
```

---

## 仓库结构

```text
ai-research-writing-skill/
├── docs/                 # 发布与增长 playbook
├── examples/             # 最小 demo paper repo
├── SKILL.md              # 唯一规范 agent 入口
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
| [`examples/paper-about-ai-research-writing-skill/`](examples/paper-about-ai-research-writing-skill/) | 关于本项目自身的端到端论文 demo |
| [`docs/LAUNCH_PLAYBOOK.zh-CN.md`](docs/LAUNCH_PLAYBOOK.zh-CN.md) | 开源增长与发布清单 |

---

## 辅助脚本

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
python3 scripts/research_quality_gate.py /path/to/paper-project
```

详见 [`scripts/README.md`](scripts/README.md)。

---

## 使用注意

- 内置模板仅为便利副本，**正式投稿前必须核对官方 venue 要求**。  
- 勿将私有 PDF、专有实验日志、API key 或审稿保密材料提交进仓库。

---

## 致谢

本项目参考并借鉴了下面这些优秀的科研写作与绘图项目，但并不是要替代它们；我们把这些启发收束到一个更窄、更深的目标：**把一个 ML/AI 研究仓库，转成有证据链、可编译、可投稿的会议论文包**。

| 项目 | 擅长什么 | 本项目的差异 |
|---|---|---|
| [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 面向 ML/CV/NLP 论文写作的紧凑 skill package，把科研写作笔记整理成可复用 agent skill。 | 在写作指南之外，增加完整 repo-to-paper 生产契约：项目 inventory、claim-evidence map、核验 BibTeX、图表资产、build check 和投稿打包。 |
| [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | 通用科研写作助手，覆盖毕业论文、章节写作、文献综述、LaTeX 输出、多平台协作和过程追踪。 | 更专注 AI 会议论文，从代码、日志、实验结果和 venue template 出发，而不是通用 thesis/chapter 写作。 |
| [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | 综合 AI research and engineering skills library，覆盖从 idea 到 paper 的更大研究生命周期。 | 只做一个深垂直：已有 ML/AI 研究仓库的论文写作执行与投稿 readiness。 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | Nature/CNS 风格写作、润色、审稿回复、数据可用性、引用和高影响力期刊图表 workflow。 | 目标 venue 是 ML/AI 会议，如 NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV、ACL、AAAI、COLM。 |
| [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 面向顶会和期刊的高质量 Python 科研绘图脚本与示例。 | 把 figure workflow 接入整篇论文链路：图要绑定 claim、证据、caption、LaTeX 引用和投稿检查。 |

一句话：相关项目提供了写作经验、通用技能生态、Nature 风格发表能力或科研绘图能力；本项目把这些启发整合成一个**面向真实 AI 研究仓库的 claim-evidence-engineering 论文 agent workflow**。

## License

MIT License
