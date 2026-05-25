# Paper Writing Suite

[English](README.md)

**Paper Writing Suite** 是一个面向 AI 研究论文写作与投稿的 agent skill，用于把研究代码、实验记录、文献调研和会议模板转化为有证据支撑的论文草稿与投稿材料。

它适用于 ML、AI、CV、NLP 及相关研究项目。核心理念是：

> Treat paper writing as a claim-evidence-engineering workflow, not prose generation.

也就是说，论文写作不只是生成流畅文字，而是围绕“主张-证据”组织研究材料：每个重要 claim 都应能追溯到代码、实验结果、笔记或已核验引用。

## 安装

假设你已经把本仓库 clone 到本地。可以把它复制或软链接到对应 agent 的 skills 目录。

### Cursor

全局安装：

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/paper-writing-skills ~/.cursor/skills/paper-writing-suite
```

项目级安装：

```bash
mkdir -p .cursor/skills
ln -s /path/to/paper-writing-skills .cursor/skills/paper-writing-suite
```

### Codex

```bash
mkdir -p "$CODEX_HOME/skills"
ln -s /path/to/paper-writing-skills "$CODEX_HOME/skills/paper-writing-suite"
```

### Claude Code

全局安装：

```bash
mkdir -p "$HOME/.claude/skills"
ln -s /path/to/paper-writing-skills "$HOME/.claude/skills/paper-writing-suite"
```

项目级安装：

```bash
mkdir -p .claude/skills
ln -s /path/to/paper-writing-skills .claude/skills/paper-writing-suite
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
ln -s /path/to/paper-writing-skills "$HOME/.gemini/skills/paper-writing-suite"
```

## 使用示例

```text
Use paper-writing-suite to inspect this repo and create the initial paper_story.md and claim_evidence_map.md.
```

```text
Use paper-writing-suite to revise the Related Work. Build a literature inventory and positioning analysis before drafting.
```

内置脚本只依赖 Python 标准库。

## 覆盖能力

- 梳理 paper story 和贡献定位
- 建立 claim-evidence map
- 撰写或修订 Abstract、Introduction、Related Work、Method、Experiments、Limitations 和 Conclusion
- 建立文献库并核验引用
- 规划 figures/tables，并为数值结果保留确定性来源
- 进行 reviewer-style self-review 和拒稿风险诊断
- 完成 venue checklist、LaTeX build check 和投稿打包

## 仓库结构

```text
paper-writing-suite/
├── SKILL.md                  # agent-facing 入口
├── references/               # workflow、写作、引用、图表、venue、review 指南
├── scripts/                  # 轻量检查和格式辅助脚本
├── templates/                # LaTeX 模板和来源说明
└── README.zh-CN.md           # 中文说明
```

关键 reference：

- `references/README.md`：任务到 reference 的路由。
- `references/workflow.md`：完整论文状态机。
- `references/artifacts.md`：持久化产物契约。
- `references/literature-review.md`：本地文献库和论文定位工作流。
- `references/citation-workflow.md`：引用检索、核验和 BibTeX 工作流。
- `references/figure-workflow.md`：图表规划和后端选择。

## 脚本

```bash
python3 scripts/extract_claims.py main.tex > claim_evidence_map.md
python3 scripts/check_citations.py main.tex references.bib
python3 scripts/check_todos.py main.tex checklist.tex references.bib figures
python3 scripts/parse_build_log.py main.log
python3 scripts/camera_ready_check.py main.tex
```

更多说明见 `scripts/README.md`。

## 注意事项

- 内置模板只是 convenience copies，正式投稿前必须核对官方 venue instructions。
- 不要提交私有 PDF、专有实验日志、API keys 或 reviewer-confidential material。

## 致谢

本项目参考并借鉴了相关开源 skill 项目的思想与组织方式，包括：

- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## License

本项目采用 MIT License。
