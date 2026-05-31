# AI Research Writing Skill

[English](README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: stdlib only](https://img.shields.io/badge/Python-stdlib%20only-blue.svg)](scripts/README.md)
[![Entrypoint](https://img.shields.io/badge/Entrypoint-SKILL.md-purple.svg)](SKILL.md)
[![LaTeX templates](https://img.shields.io/badge/Templates-NeurIPS%20%7C%20ICML%20%7C%20ICLR%20%7C%20CVPR%20%7C%20ACL-orange.svg)](templates/README.md)

把一个 ML/AI 研究仓库，整理成**有证据、有图表、能编译、能继续投稿打磨的论文草稿**。

你把代码、实验日志、研究笔记和会议模板交给 coding agent；这个 skill 会约束 agent 不只是“写得像论文”，而是产出一套可检查的论文材料：论文主线、claim-evidence map、引用核验、图表、审稿式意见、拒稿风险和 LaTeX 编译记录。

> **写论文不是生成漂亮段落，而是把每个关键论断和证据对齐。**  
> 重要 claim 应该能追溯到代码、实验结果、研究笔记或已核验文献。

![AI Research Writing Skill teaser](examples/paper-about-ai-research-writing-skill/paper/figures/teaser_imagegen.png)

---

## 端到端 Demo

```text
使用 AI Research Writing Skill，给这个仓库本身写一篇完整的系统论文。
把 ai-research-writing-skill 当作研究对象。
检查 SKILL.md、references/、scripts/、templates/、examples/ 和 README。
生成 paper_story.md、claim_evidence_map.md、文献定位、已核验引用、ICML 风格图表，并在 examples/paper-about-ai-research-writing-skill/paper/ 下生成可编译的 ICML LaTeX 论文。
不要编造性能数字，只使用仓库中可以检查的事实作为证据。
```

这个 example 已经包含完整输出。想快速判断生成质量，可以直接看 PDF：

- **生成的 ICML 风格论文：** [`paper/main.pdf`](examples/paper-about-ai-research-writing-skill/paper/main.pdf)
- `paper/main.tex`：完整 LaTeX 论文草稿。
- `paper/main.pdf`：已编译 PDF。
- `paper_story.md`：论文主线、gap、贡献和不能乱说的 claim。
- `claim_evidence_map.md`：每个主要 claim 对应的证据状态。
- `literature/positioning.md` 和 `citation_verification.md`：相关项目定位与引用核验。
- `paper/figures/` 和 `paper/tables/`：ICML 风格图表资产。
- `build_check.md`：编译命令、结果和剩余风险。

![AI Research Writing Skill method overview](examples/paper-about-ai-research-writing-skill/paper/figures/overview_imagegen.png)

## 适合哪些使用场景

你不需要等论文快写完才用它。不同阶段都可以把它当成一个“科研写作搭档”。

| 场景 | 你现在有什么 | 可以让 agent 做什么 |
|---|---|---|
| **只有一个想法** | 选题、灵感、可能的方法 | 梳理论文主线、研究缺口、贡献边界、需要补的证据和下一步实验计划。 |
| **想从 repo 写成完整论文** | 代码、方案设计、笔记、实验日志、中间结果、会议模板 | 生成论文主线、证据表、文献定位、BibTeX、图、表、LaTeX 草稿和编译记录。 |
| **已有初稿，想找问题** | 完整或部分论文草稿 | 扮演严格审稿人，写 reviewer-style comments，指出拒稿风险，并把问题转成可执行修改项。 |
| **已有稿件，准备 revise** | 论文、审稿意见、已知弱点或某个待改章节 | 按章节修订，保留有证据支撑的 claim，弱化不可靠表述，修复引用，改进图表。 |
| **需要图表** | 实验结果、日志、CSV、方法说明或粗略图示想法 | 规划图表，生成 overview/method 图，制作确定性结果表，写 caption，并接入 LaTeX。 |
| **投稿前自检** | 接近完成的论文包 | 检查引用、占位符、编译、venue checklist、审稿风险、打包和 Overleaf/Git 交接。 |

可以直接复制的 prompt：

```text
我现在只有一个粗略想法。请使用 AI Research Writing Skill 帮我梳理论文主线：明确研究 gap、可以声称和不能声称的 claim，并制定证据、实验、图表和写作计划。
```

```text
我有代码、方法设计、笔记和一些实验日志/结果。请使用 AI Research Writing Skill 端到端生成完整论文包：paper_story.md、claim_evidence_map.md、文献定位、核验 BibTeX、图表、LaTeX 草稿和 build_check.md。
```

```text
我已经有论文初稿。请使用 AI Research Writing Skill 扮演严格的 ICML 审稿人，写详细 review comments，指出拒稿风险，并把高风险问题转成具体修改建议。
```

```text
我已经有论文稿件，想做 revise。请使用 AI Research Writing Skill 按章节改进论文，保留有证据支撑的 claim，弱化不可靠 claim，修复引用，改进图表，并更新 LaTeX 包。
```

## 为什么需要这个 skill

| 常见 AI 写论文方式 | 这个 skill 更强调 |
|---|---|
| 凭记忆写出流畅段落 | 先把 claim 和仓库证据对齐 |
| 引用靠猜，BibTeX 靠编 | 从 arXiv、DOI、Semantic Scholar 等来源核验引用 |
| 只给 figure 想法，不落文件 | 生成 overview/method 图；数值图表必须来自数据或脚本 |
| 停在提纲和建议 | 落地 `paper_story.md`、`claim_evidence_map.md`、`references.bib` 和图表文件 |
| 泛泛而谈“可以改进” | 给出审稿式意见、拒稿风险、venue checklist、编译与打包检查 |

**模板和 checklist 覆盖：** NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV、ACL、AAAI、COLM 等。正式投稿前，请一定以[会议官方说明](references/venue-templates.md)为准。

## 使用前后对比

| 使用前 | 使用后 |
|---|---|
| 笔记、日志、草稿散落各处 | 有 `paper_story.md` 和清晰的任务边界 |
| claim 听起来合理，但证据在哪里不清楚 | `claim_evidence_map.md` 记录每个 claim 的证据状态 |
| 凭记忆补引用 | 引用从权威元数据获取或核验 |
| 只有 figure 想法 | 生成概念图，数值图表由确定性脚本或表格承载 |
| “看起来写完了” | 还有审稿风险、引用、编译和投稿前检查 |

## 产出什么

这个 skill 覆盖从选题叙事到投稿前整理的完整链路：

| 阶段 | 典型产物 |
|---|---|
| **论文主线** | thesis、gap、贡献、不能乱说的 claim |
| **证据** | 和代码、日志、表格绑定的 `claim_evidence_map.md` |
| **正文** | Abstract、Introduction、Related Work、Method、Experiments、Limitations、Conclusion |
| **文献** | 本地文献清单、定位分析、核验后的 `references.bib` |
| **图表** | overview/method 生成图；结果图表由数据、日志或脚本生成 |
| **审稿** | reviewer-style comments、拒稿风险、作者自检、修改计划 |
| **投稿** | venue checklist、LaTeX 编译检查、引用审计、打包记录 |

### 内置质量门禁

这个 skill 会要求 agent 在关键节点停下来检查，而不是一路写到底：

- **证据门禁**：数值必须来自数据、日志或脚本，不能来自图像模型。  
- **主线门禁**：贡献和 claim 边界没定清楚之前，不直接写全文。  
- **文献门禁**：Related Work 之前先做文献定位。  
- **引用门禁**：未核验的 BibTeX 必须显式标出来。  
- **图表门禁**：概念图可以用图像生成；数值结果必须用确定性方式生成。  
- **审稿门禁**：高风险 objection 没处理前，不轻易说“完成”。  
- **编译门禁**：要么成功编译，要么记录阻塞原因。  

---

## 安装

**最简单的理解：**根目录 [`SKILL.md`](SKILL.md) 是唯一规范入口。  
`references/`、`scripts/`、`templates/` 和 `examples/` 都是它按需调用的辅助材料。

### 让 Agent 自动安装

你可以直接对自己的 agent 说：

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
遵循 SKILL.md，只加载当前任务需要的 references。
```

---

## 仓库结构

```text
ai-research-writing-skill/
├── docs/                 # 发布与增长 playbook
├── examples/             # 端到端 demo paper
├── SKILL.md              # 唯一规范 agent 入口
├── references/           # 工作流、写作、引用、图表、venue、审稿
│   └── assets/           # 科研图表示例与版式参考
├── scripts/              # claim、引用、占位符、编译日志和投稿前检查
├── templates/            # NeurIPS / ICML / CVPR / ACL / ... LaTeX 模板
└── README.md
```

**建议先看这些文件：**

| 文件 | 用途 |
|---|---|
| [`references/workflow.md`](references/workflow.md) | 完整论文工作流 |
| [`references/artifacts.md`](references/artifacts.md) | 论文仓库里应该落盘哪些产物 |
| [`references/figure-workflow.md`](references/figure-workflow.md) | 如何区分概念图、方法图和数值结果图 |
| [`references/citation-workflow.md`](references/citation-workflow.md) | 如何检索、核验和修复 BibTeX |
| [`templates/README.md`](templates/README.md) | 模板列表和编译说明 |
| [`examples/paper-about-ai-research-writing-skill/`](examples/paper-about-ai-research-writing-skill/) | 用本项目给自己写论文的端到端示例 |
| [`docs/LAUNCH_PLAYBOOK.zh-CN.md`](docs/LAUNCH_PLAYBOOK.zh-CN.md) | 开源发布和推广清单 |

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

更多说明见 [`scripts/README.md`](scripts/README.md)。

---

## 使用注意

- 仓库里的会议模板只是方便起步，**正式投稿前一定要核对官方 author instructions**。  
- 不要把私有 PDF、未公开实验日志、API key 或审稿保密材料提交进仓库。  
- 生成图可以帮助解释方法，但不能作为数值结果或实验结论的来源。

---

## 致谢

本项目参考了下面这些优秀的科研写作与绘图项目。我们不是要替代它们，而是把相关思路收束到一个更具体的场景：**让 agent 在真实 ML/AI 研究仓库里，生成有证据链、可编译、可继续投稿打磨的论文包**。

| 项目 | 擅长什么 | 本项目的不同点 |
|---|---|---|
| [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 面向 ML/CV/NLP 的论文写作 skill package。 | 在写作指南之外，增加 repo inventory、claim-evidence map、引用核验、图表资产、编译检查和投稿打包。 |
| [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | 通用科研写作助手，覆盖毕业论文、章节写作、文献综述和 LaTeX 输出。 | 更聚焦 AI 会议论文，从代码、日志、实验结果和 venue template 出发。 |
| [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | 综合 AI research and engineering skills library。 | 只做一个深方向：已有 ML/AI 研究仓库的论文写作执行与投稿前整理。 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | Nature/CNS 风格写作、润色、审稿回复、数据可用性和高影响力图表 workflow。 | 目标 venue 是 NeurIPS、ICML、ICLR、CVPR、ACL 等 ML/AI 会议。 |
| [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 面向顶会和期刊的高质量 Python 科研绘图脚本与示例。 | 把 figure workflow 接入整篇论文链路：图要绑定 claim、证据、caption、LaTeX 引用和投稿检查。 |

## License

MIT License
