# 引用管理与幻觉防范

本参考文档提供通过程序化方式管理引用、防止 AI 生成引用幻觉，以及维护整洁参考文献库的完整工作流。

---

## 目录

- [为何引用核验至关重要](#为何引用核验至关重要)
- [引用 API 概览](#引用-api-概览)
- [经核验的引用工作流](#经核验的引用工作流)
- [Python 实现](#python-实现)
- [BibTeX 管理](#bibtex-管理)
- [常见引用格式](#常见引用格式)
- [故障排除](#故障排除)

---

## 为何引用核验至关重要

### 幻觉问题

研究已记录 AI 生成引用中的显著问题：
- AI 生成引用的**错误率约 40%**（Enago Academy 研究）
- NeurIPS 2025 发现**逾 100 条幻觉引用**溜过审稿
- 常见错误包括：
  - 虚构论文标题但使用真实作者名
  - 错误的发表场所或年份
  - 元数据看似合理但不存在的论文
  - 错误的 DOI 或 arXiv ID

### 后果

- 部分会议直接拒稿（desk rejection）
- 审稿人信任受损
- 发表后可能被撤稿
- 浪费时间追查不存在的来源

### 解决方案

**切勿凭记忆生成引用——务必通过程序化方式核验。**

---

## 引用 API 概览

### 主要 API

| API | 覆盖范围 | 速率限制 | 最适用场景 |
|-----|----------|-------------|----------|
| **Semantic Scholar** | 2.14 亿篇论文 | 1 RPS（免费 key） | ML/AI 论文、引用图谱 |
| **CrossRef** | 1.4 亿+ DOI | 带 mailto 的 polite pool | DOI 查询、BibTeX 获取 |
| **arXiv** | 预印本 | 3 秒间隔 | ML 预印本、PDF 访问 |
| **OpenAlex** | 2.4 亿+ 作品 | 10 万/天，10 RPS | MAG 的开源替代 |

### API 选择指南

```
需要 ML 论文检索？ → Semantic Scholar
有 DOI、需要 BibTeX？ → CrossRef 内容协商
查找预印本？ → arXiv API
需要开放数据、批量访问？ → OpenAlex
```

### 无官方 Google Scholar API

Google Scholar 没有官方 API。爬取违反服务条款。仅当 Semantic Scholar 覆盖不足时，可考虑 SerpApi（$75–275/月）。

---

## 经核验的引用工作流

### 五步流程

```
1. 检索 → 用具体关键词查询 Semantic Scholar
     ↓
2. 核验 → 在 2+ 个来源中确认论文存在
     ↓
3. 获取 → 通过 DOI 内容协商获取 BibTeX
     ↓
4. 校验 → 确认所引用 claim 出现在原文中
     ↓
5. 添加 → 将经核验条目加入 .bib 文件
```

### 步骤 1：检索

对 ML/AI 论文使用 Semantic Scholar：

```python
from semanticscholar import SemanticScholar

sch = SemanticScholar()
results = sch.search_paper("transformer attention mechanism", limit=10)

for paper in results:
    print(f"Title: {paper.title}")
    print(f"Year: {paper.year}")
    print(f"DOI: {paper.externalIds.get('DOI', 'N/A')}")
    print(f"arXiv: {paper.externalIds.get('ArXiv', 'N/A')}")
    print(f"Citation count: {paper.citationCount}")
    print("---")
```

### 步骤 2：核验存在性

至少在两个来源中确认论文存在：

```python
import requests

def verify_paper(doi=None, arxiv_id=None, title=None):
    """Verify paper exists in multiple sources."""
    sources_found = []

    # Check Semantic Scholar
    sch = SemanticScholar()
    if doi:
        paper = sch.get_paper(f"DOI:{doi}")
        if paper:
            sources_found.append("Semantic Scholar")

    # Check CrossRef (via DOI)
    if doi:
        resp = requests.get(f"https://api.crossref.org/works/{doi}")
        if resp.status_code == 200:
            sources_found.append("CrossRef")

    # Check arXiv
    if arxiv_id:
        resp = requests.get(
            f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        )
        if "<entry>" in resp.text:
            sources_found.append("arXiv")

    return len(sources_found) >= 2, sources_found
```

### 步骤 3：获取 BibTeX

使用 DOI 内容协商以保证准确性：

```python
import requests

def doi_to_bibtex(doi: str) -> str:
    """Get verified BibTeX from DOI via CrossRef content negotiation."""
    response = requests.get(
        f"https://doi.org/{doi}",
        headers={"Accept": "application/x-bibtex"},
        allow_redirects=True
    )
    response.raise_for_status()
    return response.text

# Example: "Attention Is All You Need"
bibtex = doi_to_bibtex("10.48550/arXiv.1706.03762")
print(bibtex)
```

### 步骤 4：校验 claim

在因特定 claim 引用论文前，确认该 claim 存在：

```python
def get_paper_abstract(doi):
    """Get abstract to verify claims."""
    sch = SemanticScholar()
    paper = sch.get_paper(f"DOI:{doi}")
    return paper.abstract if paper else None

# Verify claim appears in abstract
abstract = get_paper_abstract("10.48550/arXiv.1706.03762")
claim = "attention mechanism"
if claim.lower() in abstract.lower():
    print("Claim appears in paper")
```

### 步骤 5：加入参考文献库

将经核验条目以统一 key 格式加入 .bib 文件：

```python
def generate_citation_key(bibtex: str) -> str:
    """Generate consistent citation key: author_year_firstword."""
    import re

    # Extract author
    author_match = re.search(r'author\s*=\s*\{([^}]+)\}', bibtex, re.I)
    if author_match:
        first_author = author_match.group(1).split(',')[0].split()[-1]
    else:
        first_author = "unknown"

    # Extract year
    year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', bibtex, re.I)
    year = year_match.group(1) if year_match else "0000"

    # Extract title first word
    title_match = re.search(r'title\s*=\s*\{([^}]+)\}', bibtex, re.I)
    if title_match:
        first_word = title_match.group(1).split()[0].lower()
        first_word = re.sub(r'[^a-z]', '', first_word)
    else:
        first_word = "paper"

    return f"{first_author.lower()}_{year}_{first_word}"
```

---

## Python 实现

### 完整 Citation Manager 类

```python
"""
Citation Manager - Verified citation workflow for ML papers.
"""

import requests
import time
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass

try:
    from semanticscholar import SemanticScholar
except ImportError:
    print("Install: pip install semanticscholar")
    SemanticScholar = None

@dataclass
class Paper:
    title: str
    authors: List[str]
    year: int
    doi: Optional[str]
    arxiv_id: Optional[str]
    venue: Optional[str]
    citation_count: int
    abstract: Optional[str]

class CitationManager:
    """Manage citations with verification."""

    def __init__(self, api_key: Optional[str] = None):
        self.sch = SemanticScholar(api_key=api_key) if SemanticScholar else None
        self.verified_papers: Dict[str, Paper] = {}

    def search(self, query: str, limit: int = 10) -> List[Paper]:
        """Search for papers using Semantic Scholar."""
        if not self.sch:
            raise RuntimeError("Semantic Scholar not available")

        results = self.sch.search_paper(query, limit=limit)
        papers = []

        for r in results:
            paper = Paper(
                title=r.title,
                authors=[a.name for a in (r.authors or [])],
                year=r.year or 0,
                doi=r.externalIds.get('DOI') if r.externalIds else None,
                arxiv_id=r.externalIds.get('ArXiv') if r.externalIds else None,
                venue=r.venue,
                citation_count=r.citationCount or 0,
                abstract=r.abstract
            )
            papers.append(paper)

        return papers

    def verify(self, paper: Paper) -> Tuple[bool, List[str]]:
        """Verify paper exists in multiple sources."""
        sources = []

        # Already found in Semantic Scholar via search
        sources.append("Semantic Scholar")

        # Check CrossRef if DOI available
        if paper.doi:
            try:
                resp = requests.get(
                    f"https://api.crossref.org/works/{paper.doi}",
                    timeout=10
                )
                if resp.status_code == 200:
                    sources.append("CrossRef")
            except:
                pass

        # Check arXiv if ID available
        if paper.arxiv_id:
            try:
                resp = requests.get(
                    f"http://export.arxiv.org/api/query?id_list={paper.arxiv_id}",
                    timeout=10
                )
                if "<entry>" in resp.text and "<title>" in resp.text:
                    sources.append("arXiv")
            except:
                pass

        return len(sources) >= 2, sources

    def get_bibtex(self, paper: Paper) -> Optional[str]:
        """Get BibTeX for verified paper."""
        if paper.doi:
            try:
                resp = requests.get(
                    f"https://doi.org/{paper.doi}",
                    headers={"Accept": "application/x-bibtex"},
                    timeout=10,
                    allow_redirects=True
                )
                if resp.status_code == 200:
                    return resp.text
            except:
                pass

        # Fallback: generate from paper data
        return self._generate_bibtex(paper)

    def _generate_bibtex(self, paper: Paper) -> str:
        """Generate BibTeX from paper metadata."""
        # Generate citation key
        first_author = paper.authors[0].split()[-1] if paper.authors else "unknown"
        first_word = paper.title.split()[0].lower().replace(',', '').replace(':', '')
        key = f"{first_author.lower()}_{paper.year}_{first_word}"

        # Format authors
        authors = " and ".join(paper.authors) if paper.authors else "Unknown"

        bibtex = f"""@article{{{key},
  title = {{{paper.title}}},
  author = {{{authors}}},
  year = {{{paper.year}}},
  {'doi = {' + paper.doi + '},' if paper.doi else ''}
  {'eprint = {' + paper.arxiv_id + '},' if paper.arxiv_id else ''}
  {'journal = {' + paper.venue + '},' if paper.venue else ''}
}}"""
        return bibtex

    def cite(self, query: str) -> Optional[str]:
        """Full workflow: search, verify, return BibTeX."""
        # Search
        papers = self.search(query, limit=5)
        if not papers:
            return None

        # Take top result
        paper = papers[0]

        # Verify
        verified, sources = self.verify(paper)
        if not verified:
            print(f"Warning: Could only verify in {sources}")

        # Get BibTeX
        bibtex = self.get_bibtex(paper)

        # Cache
        if bibtex:
            self.verified_papers[paper.title] = paper

        return bibtex


# Usage example
if __name__ == "__main__":
    cm = CitationManager()

    # Search and cite
    bibtex = cm.cite("attention is all you need transformer")
    if bibtex:
        print(bibtex)
```

### 快捷函数

```python
def quick_cite(query: str) -> str:
    """One-liner citation."""
    cm = CitationManager()
    return cm.cite(query)

def batch_cite(queries: List[str], output_file: str = "references.bib"):
    """Cite multiple papers and save to file."""
    cm = CitationManager()
    bibtex_entries = []

    for query in queries:
        print(f"Processing: {query}")
        bibtex = cm.cite(query)
        if bibtex:
            bibtex_entries.append(bibtex)
        time.sleep(1)  # Rate limiting

    with open(output_file, 'w') as f:
        f.write("\n\n".join(bibtex_entries))

    print(f"Saved {len(bibtex_entries)} citations to {output_file}")
```

---

## BibTeX 管理

### BibTeX 与 BibLaTeX

| 特性 | BibTeX | BibLaTeX |
|---------|--------|----------|
| Unicode 支持 | 有限 | 完整 |
| 条目类型 | 标准 | 扩展（@online、@dataset） |
| 可定制性 | 有限 | 高度灵活 |
| 后端 | bibtex | Biber（推荐） |

**建议**：新论文使用 BibLaTeX + Biber。

### LaTeX 设置

```latex
% In preamble
\usepackage[
    backend=biber,
    style=numeric,
    sorting=none
]{biblatex}
\addbibresource{references.bib}

% In document
\cite{vaswani_2017_attention}

% At end
\printbibliography
```

### 引用命令

```latex
\cite{key}      % Numeric: [1]
\citep{key}     % Parenthetical: (Author, 2020)
\citet{key}     % Textual: Author (2020)
\citeauthor{key} % Just author name
\citeyear{key}  % Just year
```

### 统一的引用 key

使用格式：`author_year_firstword`

```
vaswani_2017_attention
devlin_2019_bert
brown_2020_language
```

---

## 常见引用格式

### 会议论文

```bibtex
@inproceedings{vaswani_2017_attention,
  title = {Attention Is All You Need},
  author = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and
            Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and
            Kaiser, Lukasz and Polosukhin, Illia},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {30},
  year = {2017},
  publisher = {Curran Associates, Inc.}
}
```

### 期刊文章

```bibtex
@article{hochreiter_1997_long,
  title = {Long Short-Term Memory},
  author = {Hochreiter, Sepp and Schmidhuber, J{\"u}rgen},
  journal = {Neural Computation},
  volume = {9},
  number = {8},
  pages = {1735--1780},
  year = {1997},
  publisher = {MIT Press}
}
```

### arXiv 预印本

```bibtex
@misc{brown_2020_language,
  title = {Language Models are Few-Shot Learners},
  author = {Brown, Tom and Mann, Benjamin and Ryder, Nick and others},
  year = {2020},
  eprint = {2005.14165},
  archiveprefix = {arXiv},
  primaryclass = {cs.CL}
}
```

---

## 故障排除

### 常见问题

**问题：Semantic Scholar 无结果**
- 尝试更具体的关键词
- 检查作者姓名拼写
- 对精确短语使用引号

**问题：DOI 无法解析为 BibTeX**
- DOI 可能已注册但未关联 CrossRef
- 若有 arXiv ID 可改试 arXiv
- 根据元数据手动生成 BibTeX

**问题：速率限制错误**
- 请求间加延迟（1–3 秒）
- 如有 API key 请使用
- 缓存结果避免重复查询

**问题：BibTeX 编码问题**
- 使用正确 LaTeX 转义：`{\"u}` 表示 ü
- 确保文件为 UTF-8 编码
- 使用 BibLaTeX + Biber 以更好支持 Unicode

### 核验清单

添加引用前：

- [ ] 论文在至少 2 个来源中找到
- [ ] DOI 或 arXiv ID 已核验
- [ ] BibTeX 已获取（非凭记忆生成）
- [ ] 条目类型正确（@inproceedings 与 @article）
- [ ] 作者姓名完整且格式正确
- [ ] 年份与发表场所已核验
- [ ] 引用 key 遵循统一格式

---

## 其他资源

**API：**
- Semantic Scholar: https://api.semanticscholar.org/api-docs/
- CrossRef: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- arXiv: https://info.arxiv.org/help/api/basics.html
- OpenAlex: https://docs.openalex.org/

**Python 库：**
- `semanticscholar`: https://pypi.org/project/semanticscholar/
- `arxiv`: https://pypi.org/project/arxiv/
- `habanero` (CrossRef): https://github.com/sckott/habanero

**核验工具：**
- Citely: https://citely.ai/citation-checker
- ReciteWorks: https://reciteworks.com/
