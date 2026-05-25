# 引用工作流参考文档

当你需要查找、添加或修复引用（citations）时使用本参考文档。
它继承自 `ml-paper-writing` 的“高可靠性（high-reliability）”工作流：不要凭记忆生成 BibTeX；必须核验元数据与主张支撑。

## 不可谈判的规则（Non-Negotiable Rule）

- 不要编造引用（invent citations）。
即使你的参考文献写得很流畅，但只要是假的，就会构成学术诚信问题。
如果某条引用无法被核验，就把它标记为占位符（placeholder），或直接移除对应主张。

## 五步可验证的引用工作流（Five-Step Verified Citation Workflow）

```text
1. SEARCH   -> 从权威学术来源中查找候选项
2. VERIFY  -> 在可靠元数据中确认标题/作者/年份/DOI/arXiv
3. RETRIEVE -> 从 DOI、arXiv、出版社或官方元数据获取 BibTeX
4. VALIDATE -> 检查被引用的工作是否支撑句级主张
5. RECORD  -> 增加 .bib 条目，并把核验过程记录在 citation_verification.md
```

## 来源选择（Source Selection）

| 需求（Need） | 首选来源（Preferred source） |
|---|---|
| ML/AI 论文检索 | Semantic Scholar、OpenAlex、arXiv |
| DOI 元数据 | Crossref、DOI 内容协商（content negotiation） |
| 预印本元数据 | arXiv API 或 arXiv 页面 |
| 出版商版本 | 官方会议论文集或出版社页面 |
| 软件/库引用 | 官方文档、发布页（release page）、仓库引用元数据 |
| 数据集引用 | 数据集卡片（dataset card）、官方数据集页面、论文，或许可证页面 |

Google Scholar 没有官方公开 API。避免依赖抓取（scraping）它的工作流。

## 查询策略（Query Strategy）

按这个顺序搜索：

1. 已知且准确的标题（Exact known title）。
2. 方法名 + 任务/领域（Method name + task/domain）。
3. 基线名 + 基准/任务（Baseline name + benchmark/task）。
4. 当标题不确定时，用作者名 + 关键词（Author name + keyword）。
5. 现有 `.bib` key 与代码库里的引用（citations）。

当搜索失败会影响论文叙事时，记录失败原因。

## 元数据核验（Metadata Verification）

满足以下条件时，才算“该引用已被核验（verified）”：

- 标题、第一作者、年份，以及会议/预印本来源保持一致；
- 如果适用，存在 DOI 或 arXiv ID；
- BibTeX 已从权威来源获取或从权威来源推导而来；
- 该引用确实支撑它所绑定的主张。

当元数据冲突或该工作较为冷门时，使用两处来源（two sources）。

## BibTeX key 约定（BibTeX Key Convention）

使用稳定、可读的 key：

```text
firstauthor_year_shorttitle
```

示例：

```text
vaswani_2017_attention
kirillov_2023_segment
```

key 保持全小写（lowercase）、ASCII，并且在论文里使用后就保持稳定（stable）。

## 主张核验（Claim Validation）

对每一条引用句，按支持关系分类：

- `direct`：论文直接支撑该主张。
- `background`：论文只是用来激励该领域。
- `contrast`：该论文正在与本文进行对比。
- `software`：该引用记录了某个工具/库/数据集。
- `weak`：该引用并不支撑该主张。

强主张需要 `direct`、`contrast` 或 `software` 支持，具体取决于句子的类型。

## `citation_verification.md` 模板（Template）

```markdown
| Key | Source checked | Claim supported | Relation | Status | Notes |
|---|---|---|---|---|---|
| author_2026_short | DOI / arXiv / publisher URL | Sentence or claim | direct | verified | ... |
```

Status 取值：

- `verified`
- `software-doc`
- `placeholder`
- `needs-license-check`
- `removed`

## 占位符策略（Placeholder Policy）

只有在草稿需要保留“意图（intent）”时才使用可见占位符：

```latex
\cite{PLACEHOLDER_author_year_verify}
```

然后把占位符写入 `citation_verification.md`，并告知用户。
在最终稿里不要留下隐藏的 placeholder 引用。

## 引用修复流程（Citation Repair Procedure）

当某个引用 key 缺失或看起来可疑时：

1. 在 `.bib`、`.tex`、笔记与下载的 PDF 中搜索该 key。
2. 如果可用网络工具，搜索标题或附近的语句（online/API）。
3. 替换为已核验的“原始来源（primary source）”。
4. 如果没有来源能支撑该句，修改该句。
5. 运行 `scripts/check_citations.py`。

## 常见失败模式（Common Failure Modes）

- 真作者 + 编造标题。
- arXiv 与会议论文集的年份写错了。
- 把“综述/Survey”当成某个特定技术主张的证据来源，实际应引用原始论文。
- 用软件仓库元数据当作科学结果的证据。
- 当任务定义不可比时，把并行工作当作基线引用。

