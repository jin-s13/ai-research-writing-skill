# 引用与清单参考文档

本参考文档用于：参考文献（bibliography）、引用核验（citation verification）、会议投稿清单（conference checklist）、可复现性（reproducibility）、以及构建就绪（build readiness）。

当你需要查找并添加新的引用时，先加载 `citation-workflow.zh-CN.md`。
（中文版对应为 `citation-workflow.zh-CN.md`。本文件是最终审计层（final audit layer）。）

## 引用规则（Citation Rules）

- 永远不要凭记忆生成 BibTeX。
- 优先使用一手来源：arXiv、DOI/Crossref、Semantic Scholar、官方出版社页面，或官方软件文档。
- 把每条引用的来源记录在 `citation_verification.md`。
- 如果一条引用无法核验，用可见的占位符（例如 `PLACEHOLDER_author_year_verify`）并在最终回复中说明。
- 除非被引用的论文确实支撑了该主张，否则不要引用它。
- 对并行工作（concurrent work），除非方法与指标可以明确比较，否则避免强对比式主张。

## 五步引用工作流（Five-Step Citation Workflow）

当你添加新的引用时使用该工作流：

1. **SEARCH**：用 Semantic Scholar、Crossref、arXiv、OpenAlex、出版社页面，或网页搜索找到候选论文。
2. **VERIFY existence**：至少在一个权威来源里确认标题/作者/年份；当元数据冲突时使用两处来源。
3. **RETRIEVE BibTeX**：优先使用 DOI/arXiv/出版社提供的 BibTeX，而不是手工手写。
4. **VALIDATE claim support**：检查被引用的工作是否支撑你句子层面的主张。
5. **RECORD**：加入 BibTeX 条目，并把来源记录到 `citation_verification.md`。

如果任何一步失败：不要默默地把它当作已完成引用。
使用可见占位符，或移除/改写句子。

## 来源优先级（Source Preference）

按优先级：

1. DOI/出版社页面或官方会议论文集（official proceedings）。
2. arXiv 页面（用于预印本）。
3. Semantic Scholar / OpenAlex / Crossref 的元数据。
4. 工具/库的官方软件文档。
5. 只有当你引用的是软件工件时，才用项目仓库；不要把仓库当作“论文主张”的证据来源。

避免为了技术主张引用二手总结，除非你的主张本身就是关于该总结。

## 以“主张”为粒度的引用核验（Claim-Level Citation Audit）

对每个引用句，判断其关系类型：

- `direct`：被引用的工作直接建立该句。
- `background`：被引用的工作激励了该领域，但并未证明该具体主张。
- `contrast`：被引用的工作正在与本文进行对比。
- `software`：该引用支持某个工具/库/数据集。
- `weak`：该引用并不支撑该句，应该改写。

只有 `direct`、`contrast` 和 `software` 才应支撑强主张。

## 核验表（Verification Table）

`citation_verification.md` 应当包含：

| Key | Source checked | Status | Notes |
|---|---|---|---|

Status 取值：

- `verified`
- `software-doc`
- `placeholder`
- `needs-license-check`
- `removed`

如果你是完整论文，建议使用扩展列：

| Key | Source checked | Claim supported | Relation | Status | Notes |
|---|---|---|---|---|---|

## 清单规则（Checklist Rules）

- 清单要匹配目标会议与模板。
- 如果目标会议与模板冲突：写出冲突，并只在冲突确实改变了投稿要求时再提问。
- 清单要诚实填写。`No` + 具体计划是可以的；不带支撑的 `Yes` 很危险。
- 当适用时包含局限（limitations）、更广泛影响（broader impacts）、可复现性（reproducibility）、数据/代码访问（data/code access）、算力（compute）、许可证（licenses）与 LLM 使用说明（LLM usage）。

## 会议清单的主题（Venue Checklist Themes）

大多数 ML 会议会要求（或至少期待）其中一些内容：

- 主张-证据一致性。
- 局限与失败模式。
- 可复现性细节：代码、数据、参数、种子、硬件、运行时间与许可证。
- 实验协议：划分（splits）、基线、指标、统计显著性与算力预算（compute budget）。
- 伦理与更广泛影响（ethics & broader impacts）。
- 人类受试、隐私、安全与防护措施（safeguards）（当适用时）。
- LLM 使用或 AI 辅助披露（当适用时）。
- 新素材：数据集/模型/代码文档、托管（hosting）、维护、许可证与同意（consent）。

对于 NeurIPS 风格清单：每一项都要明确回答，并在可能时引用对应论文章节。

## 构建检查（Build Check）

创建 `build_check.md`，包含：

- 尝试过的构建命令（build command tried）。
- TeX 工具是否可用。
- 错误或警告信息。
- 缺失的引用或参考项。
- 仍待完成的行动项（remaining action items）。

推荐完整构建：

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

使用真实的主 `.tex` 文件名。

## 提交前检查（Pre-Commit Check）

在提交或推送之前：

- `git status --short`
- `git diff --cached --stat`
- 检查生成的图片/PDF 大小。
- 确认没有未解决的 TODO，除非你有意记录为文档。
- 核验 `.tex` 里引用的 citation key 是否在 `.bib` 中存在。

推荐命令：

```bash
python scripts/check_citations.py main.tex references.bib
python scripts/check_todos.py main.tex checklist.tex references.bib figures
python scripts/parse_build_log.py main.log
```

在论文仓库里使用真实路径。

