# Paper Writing Suite

**Paper Writing Suite** 是一个端到端的 Codex 论文写作 skill，用于把研究代码仓库、实验记录、开发笔记和会议模板，转化为结构化、证据支撑明确的论文初稿。

它面向 ML、AI、CAD、机器人、系统等研究项目。它的目标不是“帮你润色几段话”，而是把论文写作当成一条完整的研究工程流程：

```text
代码仓库 / 研究笔记 / 实验结果
-> paper story
-> claim-evidence map
-> LaTeX 初稿
-> 图表设计
-> 引用核验
-> 会议 checklist
-> 编译检查
-> Overleaf / Git 提交
```

核心理念：

> Treat paper writing as a claim-evidence-engineering workflow, not prose generation.

也就是说，论文写作不是单纯生成流畅文字，而是围绕“主张-证据”进行工程化组织。每一个重要 claim 都应该能追溯到代码、实验结果、研究记录或已核验文献。如果证据不足，就应该削弱、标记或删除这个 claim。

## 为什么需要这个 Skill

真实论文写作的问题，往往不在单个环节，而在多个工具之间的断层：

- 写作助手可以生成流畅 prose，但容易脱离真实实验。
- 文献调研可以找到很多 paper，但不一定能形成清晰 paper story。
- 画图工具可以生成漂亮图片，但图不一定支撑论文主张。
- LaTeX 模板可以编译，但 submission 可能仍然缺少 citation verification、limitations、checklist、reproducibility notes。

Paper Writing Suite 的目标，就是把这些零散环节连接成一个可执行、可审计、可持续迭代的论文生产流程。

## 和已有 Skills 的关系

Paper Writing Suite 是从三个互补 skill 中整合和重构出来的：

| 原始 skill | 优势 | 单独使用时的问题 | Paper Writing Suite 如何整合 |
|---|---|---|---|
| `ml-paper-writing` | 顶会论文流程意识强：repo mining、paper story、citation discipline、checklist awareness | 很适合作为总控，但中间产物和执行门禁不够稳定 | 成为顶层投稿工作流：项目读取、story、引用核验、checklist、build、Git/Overleaf packaging |
| `research-paper-writing` | section-level 写作质量强：Abstract/Introduction 结构、段落角色、reverse outline、claim-evidence alignment | 非常适合改段落，但不是完整 LaTeX/repo/submission pipeline | 成为 section-quality 层：claim-evidence map、段落角色、reviewer-facing revision |
| `academic-plotting` | 图表设计意识强：figure role、entities、relationships、layout、数值图、架构图 | 后端可能过于绑定特定工具；生成式图片容易把文字或数字画错 | 成为 figure-quality 层：数值图用确定性脚本，系统图保留可编辑 fallback，生成图只做 polish |

因此，Paper Writing Suite 不是把三个 skill 简单拼起来，而是把它们重新组织成一套统一的 paper-production state machine。

## 核心优势

### 1. 端到端论文工程能力

Paper Writing Suite 覆盖从研究材料到投稿文件的完整路径：

- 读取 repo、docs、notes、results
- 梳理 paper story
- 建立 claim-evidence map
- 起草和修改论文各 section
- 组织 related work
- 设计 figures 和 tables
- 核验 citations
- 填写会议 checklist
- 执行 build check
- 准备 Git / Overleaf 提交

### 2. Claim-Evidence 约束

这个 skill 强制把重要主张和证据绑定起来，尤其是 Abstract 和 Introduction 中的主张。

它可以减少几类常见问题：

- claim 超过实验支持范围
- 只报好看的结果，隐藏负面指标
- 引用文献但文献其实不支持对应表述
- 文字很流畅，但 reviewer 看不到证据

### 3. 稳定的中间产物

对于完整论文生成任务，Paper Writing Suite 会鼓励产生稳定的中间文件：

```text
paper_story.md
claim_evidence_map.md
references.bib
citation_verification.md
figures/figure_plan.md
build_check.md
```

这些文件让论文写作过程可追踪、可恢复，也方便多人协作。

### 4. 面向会议投稿的工作流

Paper Writing Suite 会关注目标会议和模板要求，例如：

- NeurIPS / ICML / ICLR 风格 checklist
- 匿名投稿模式
- 页数限制
- reproducibility
- compute reporting
- broader impacts
- limitations
- data/code/license audit

如果用户要求和当前模板不一致，skill 会提醒并记录原因。

### 5. 更安全的图表生成

Paper Writing Suite 把图表按风险分层：

- **精确数值图**：必须使用确定性脚本生成。
- **架构图 / workflow 图**：优先保留 TikZ/SVG 等可编辑 fallback。
- **生成式视觉图**：可以用于 polish，但必须有 prompt/source 文件和 fallback。
- **文字密集型生成图**：必须人工检查，避免文字变形或数字错误。

这避免了生成式图片“好看但不可靠”的常见问题。

### 6. 默认进行引用核验

这个 skill 明确禁止凭记忆写 BibTeX。

推荐引用来源包括：

- arXiv BibTeX
- DOI / Crossref
- Semantic Scholar
- publisher official page
- official software documentation

每条引用都应该记录在 `citation_verification.md` 中。

## Skill 结构

```text
paper-writing-suite/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── abstract-introduction.md
│   ├── citation-checklist.md
│   ├── citation-workflow.md
│   ├── example-bank.md
│   ├── figure-spec.md
│   ├── figure-workflow.md
│   ├── paper-story.md
│   ├── reviewer-self-review.md
│   ├── reviewer-guidelines.md
│   ├── section-writing.md
│   ├── style-presets.md
│   ├── submission-packaging.md
│   ├── venue-templates.md
│   └── venue-profiles.md
└── scripts/
    ├── camera_ready_check.py
    ├── check_citations.py
    ├── check_todos.py
    ├── extract_claims.py
    ├── make_latex_table.py
    └── parse_build_log.py
```

## 各个 Reference 的作用

### `references/paper-story.md`

用于梳理论文主线：

- thesis
- gap
- technical challenge
- method insight
- contributions
- evidence
- claims to make
- claims to avoid
- reviewer risks

### `references/section-writing.md`

用于指导各 section 的写作和修改：

- Abstract
- Introduction
- Related Work
- Method
- Experiments
- Limitations
- Conclusion

它强调段落角色、reverse outline 和 claim-evidence alignment。

### `references/abstract-introduction.md`

用于 Abstract / Introduction 的高风险写作：abstract 模板、backward-first introduction logic、technical challenge pattern、pipeline pattern 和 reverse outline。

### `references/figure-workflow.md`

用于图表设计：

- figure role
- message
- entities
- relationships
- layout
- backend
- fallback

它还规定了什么时候使用确定性绘图，什么时候可以使用生成式图片。

### `references/figure-spec.md`

用于定义每张图必须具备的 role / message / entities / relationships / layout / backend / source / fallback schema。

### `references/style-presets.md`

用于数据图风格、会议图尺寸、配色、diagram style 和 arrow convention。

### `references/citation-checklist.md`

用于：

- citation verification
- checklist
- build check
- pre-commit check

### `references/citation-workflow.md`

用于程序化 citation workflow：search、verify、retrieve BibTeX、validate claim support、record verification。

### `references/venue-profiles.md`

用于记录 NeurIPS、ICML、ICLR、ACL/NLP、systems，以及 CAD/robotics/graphics-adjacent 论文的投稿预期。

### `references/venue-templates.md`

用于 limitations、reproducibility、compute、ethics、LLM usage、checklist 和 camera-ready 文本模板。

### `references/reviewer-guidelines.md`

用于整理 reviewer 对 soundness、clarity、significance、originality、reproducibility 和不同 venue 的评审关注点。

### `references/reviewer-self-review.md`

用于做 adversarial reviewer audit，覆盖 contribution、writing clarity、experimental strength、evaluation completeness 和 method soundness。

### `references/submission-packaging.md`

用于 build check、static check、artifact hygiene、Overleaf/Git workflow 和 camera-ready 检查。

### `scripts/check_citations.py`

用于检查 LaTeX 中使用的 citation key 是否存在于 BibTeX 文件中。

示例：

```bash
python scripts/check_citations.py paper.tex references.bib
```

### `scripts/check_todos.py`

用于提交前检查未解决的 TODO、PLACEHOLDER、CITATION NEEDED 等标记。

示例：

```bash
python scripts/check_todos.py paper.tex checklist.tex references.bib figures
```

### 自动化脚本

```bash
python scripts/extract_claims.py main.tex > claim_evidence_map.md
python scripts/make_latex_table.py results.csv --caption "Main results." --label tab:main --precision 3
python scripts/parse_build_log.py main.log
python scripts/camera_ready_check.py main.tex
```

## 使用示例

可以这样要求 Codex：

```text
Use paper-writing-suite to turn this repo and experiment folder into a NeurIPS paper draft.
```

或者：

```text
Use paper-writing-suite to revise the Abstract and Introduction. Make sure every claim is supported by the experiments.
```

或者：

```text
Use paper-writing-suite to design Figure 1 and the main experiment figure. Use deterministic plotting for numbers and keep editable fallbacks for diagrams.
```

## 推荐工作流

1. 检查项目结构、README、docs、results、notes。
2. 创建 `paper_story.md`。
3. 创建或更新 claim-evidence map。
4. 起草 Abstract 和 Introduction。
5. 起草 Related Work 和 Method。
6. 设计 Figure 1 和主要实验图。
7. 起草 Experiments、Limitations 和 Conclusion。
8. 核验 citations。
9. 完成 checklist 和 build check。
10. 提交到 Overleaf 或论文仓库。

## 设计原则

- **Evidence first**：先有证据，再写主张。
- **No hallucinated citations**：每条 BibTeX 都必须核验。
- **Figures are arguments**：每张图都应该支撑一个论文主张。
- **Generated images need fallbacks**：生成图可以 polish，但可编辑图和确定性数值图才是 source of truth。
- **Checklists are not paperwork**：checklist 会暴露 reproducibility、ethics、data、compute 等缺口。
- **A good draft is auditable**：合作者应该能追踪 claim、数字、引用和图表的来源。

## 当前状态

Paper Writing Suite 适合用作 Codex 风格 agent 的论文写作助手，尤其适合从一个仍在开发中的研究 repo 出发，生成论文初稿和投稿工程。

它已经经过以下验证：

- skill structure validation
- LaTeX citation-key checking
- 一个 NeurIPS 风格论文项目上的端到端测试，包括 paper story、section drafting、figure planning、citation verification、checklist completion 和 Overleaf Git submission

## License

开源前请添加你希望使用的 license。
