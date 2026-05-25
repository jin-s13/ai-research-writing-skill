# ML/AI 与系统会议 LaTeX 模板

本目录收录主要机器学习、人工智能与系统会议的官方 LaTeX 模板。

## 将 LaTeX 编译为 PDF

### 方式一：VS Code + LaTeX Workshop（推荐）

**环境准备：**
1. 安装 [TeX Live](https://www.tug.org/texlive/)（建议完整版）
   - macOS：`brew install --cask mactex`
   - Ubuntu：`sudo apt install texlive-full`
   - Windows：从 [tug.org/texlive](https://www.tug.org/texlive/) 下载

2. 安装 VS Code 扩展：**LaTeX Workshop**（作者 James Yu）
   - 打开 VS Code → 扩展（Cmd/Ctrl+Shift+X）→ 搜索 “LaTeX Workshop” → 安装

**使用：**
- 在 VS Code 中打开任意 `.tex` 文件
- 保存（Cmd/Ctrl+S）→ 自动编译为 PDF
- 点击绿色运行按钮，或使用 `Cmd/Ctrl+Alt+B` 手动编译
- 查看 PDF：点击 “View LaTeX PDF” 图标，或 `Cmd/Ctrl+Alt+V`
- 并排预览：`Cmd/Ctrl+Alt+V` 后将标签页拖至侧边

**设置**（添加到 VS Code 的 `settings.json`）：
```json
{
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex → bibtex → pdflatex × 2",
      "tools": ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
    }
  ]
}
```

### 方式二：命令行

```bash
# 基本编译
pdflatex main.tex

# 含参考文献（完整流程）
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# 使用 latexmk（自动处理依赖）
latexmk -pdf main.tex

# 持续编译（监视文件变更）
latexmk -pdf -pvc main.tex
```

### 方式三：Overleaf（在线）

1. 访问 [overleaf.com](https://www.overleaf.com)
2. New Project → Upload Project → 将模板文件夹打包为 ZIP 上传
3. 在线编辑并实时预览 PDF
4. 无需本地安装

### 方式四：其他 IDE

| IDE | 扩展/插件 | 说明 |
|-----|------------------|-------|
| **Cursor** | LaTeX Workshop | 与 VS Code 相同 |
| **Sublime Text** | LaTeXTools | 常用、维护活跃 |
| **Vim/Neovim** | VimTeX | 功能强、键盘驱动 |
| **Emacs** | AUCTeX | 完整的 LaTeX 环境 |
| **TeXstudio** | 内置 | 专用 LaTeX IDE |
| **Texmaker** | 内置 | 跨平台 LaTeX 编辑器 |

### 编译故障排查

**“File not found” 错误：**
```bash
# 确保在模板目录下执行
cd templates/icml2026
pdflatex example_paper.tex
```

**参考文献未出现：**
```bash
# 首次 pdflatex 后运行 bibtex
pdflatex main.tex
bibtex main        # 根据 main.aux 查找引用
pdflatex main.tex  # 纳入参考文献
pdflatex main.tex  # 解析交叉引用
```

**缺少宏包：**
```bash
# TeX Live 包管理器
tlmgr install <package-name>

# 或安装完整发行版以避免此类问题
```

## 可用模板

### ML/AI 会议

| 会议 | 目录 | 年份 | 来源 |
|------------|-----------|------|--------|
| ICML | `icml2026/` | 2026 | [Official ICML](https://icml.cc/Conferences/2026/AuthorInstructions) |
| ICLR | `iclr2026/` | 2026 | [Official GitHub](https://github.com/ICLR/Master-Template) |
| NeurIPS | `neurips2025/` | 2025 | 社区模板 |
| ACL | `acl/` | 2025+ | [Official ACL](https://github.com/acl-org/acl-style-files) |
| AAAI | `aaai2026/` | 2026 | [AAAI Author Kit](https://aaai.org/authorkit26/) |
| COLM | `colm2025/` | 2025 | [Official COLM](https://github.com/COLM-org/Template) |

### 系统会议

| 会议 | 目录 | 年份 | 模板类型 | 来源 |
|------------|-----------|------|---------------|--------|
| OSDI | `osdi2026/` | 2026 | USENIX | [OSDI '26 CFP](https://www.usenix.org/conference/osdi26/call-for-papers) |
| NSDI | `nsdi2027/` | 2027 | USENIX | [NSDI '27 CFP](https://www.usenix.org/conference/nsdi27/call-for-papers) |
| ASPLOS | `asplos2027/` | 2027 | ACM SIGPLAN | [ASPLOS '27 CFP](https://www.asplos-conference.org/asplos2026/call-for-papers-asplos27/) |
| SOSP | `sosp2026/` | 2026 | ACM SIGPLAN | [SOSP '26 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html) |

## 用法

### ICML 2026

```latex
\documentclass{article}
\usepackage{icml2026}  % For submission
% \usepackage[accepted]{icml2026}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

关键文件：
- `icml2026.sty` - 样式文件
- `icml2026.bst` - 参考文献样式
- `example_paper.tex` - 示例文档

### ICLR 2026

```latex
\documentclass{article}
\usepackage[submission]{iclr2026_conference}  % For submission
% \usepackage[final]{iclr2026_conference}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

关键文件：
- `iclr2026_conference.sty` - 样式文件
- `iclr2026_conference.bst` - 参考文献样式
- `iclr2026_conference.tex` - 示例文档

### ACL 系列（ACL、EMNLP、NAACL）

```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}  % For review
% \usepackage{acl}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

关键文件：
- `acl.sty` - 样式文件
- `acl_natbib.bst` - 参考文献样式
- `acl_latex.tex` - 示例文档

### AAAI 2026

```latex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai2026}  % For submission
% \usepackage{aaai2026}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

关键文件：
- `aaai2026.sty` - 样式文件
- `aaai2026.bst` - 参考文献样式

### COLM 2025

```latex
\documentclass{article}
\usepackage[submission]{colm2025_conference}  % For submission
% \usepackage[final]{colm2025_conference}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

关键文件：
- `colm2025_conference.sty` - 样式文件
- `colm2025_conference.bst` - 参考文献样式

### OSDI 2026 / NSDI 2027（USENIX 格式）

OSDI 与 NSDI 均使用 USENIX LaTeX 样式。格式要求：正文最多 12 页（不含参考文献）、双栏、10pt 字号、12pt 行距、Times Roman 字体。

```latex
\documentclass[letterpaper,twocolumn,10pt]{article}
\usepackage{usenix-2020-09}  % USENIX style file

\begin{document}
\title{Your Paper Title}

\author{Paper \#XXX}  % Anonymized for submission

\maketitle

\begin{abstract}
Your abstract here.
\end{abstract}

% Your paper content

{\footnotesize \bibliographystyle{acm}
\bibliography{references}}

\end{document}
```

关键文件：
- `usenix-2020-09.sty` - USENIX 样式文件
- `main.tex` - 示例文档

**OSDI 2026 特别说明：**
- 投稿：≤12 页；终稿：≤14 页
- 两个 track：Research 与 Operational Systems
- Operational Systems track：标题须以 “(Operational Systems)” 结尾
- 每位作者最多 8 篇投稿

**NSDI 2027 特别说明：**
- 与 OSDI 相同的 USENIX 格式，≤12 页
- 三个 track：Research、Frontiers、Operational Systems
- 基于 Introduction 的预筛选
- 春季与秋季两个 deadline

### ASPLOS 2027（ACM SIGPLAN 格式）

ASPLOS 使用 ACM `acmart` 文档类并启用 `sigplan` 选项。正文最多 12 页（不含参考文献）、双栏、10pt。

```latex
\documentclass[sigplan,10pt]{acmart}

\renewcommand\footnotetextcopyrightpermission[1]{}
\settopmatter{printfolios=true}

\begin{document}
\title{Your Paper Title}

\author{Paper \#XXX}  % Anonymized for submission
\affiliation{}

\begin{abstract}
Your abstract here.
\end{abstract}

\maketitle
\pagestyle{plain}

% Your paper content

\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
```

关键文件：
- `acmart.cls` - ACM 文档类（从 [ACM](https://www.acm.org/publications/proceedings-template) 下载）
- `ACM-Reference-Format.bst` - 参考文献样式
- `main.tex` - 示例文档

**ASPLOS 2027 特别说明：**
- 快速评审轮：审稿人仅阅读前 2 页
- **前 2 页须自成一体、可独立理解**
- 两个周期：四月与九月
- 每位作者每周期最多 4 篇投稿
- 提供 Major Revision 决定

### SOSP 2026（ACM SIGPLAN 格式）

SOSP 与 ASPLOS 使用相同的 ACM SIGPLAN 格式。正文最多 12 页，支持 A4 或 US letter，正文块 178×229mm。

```latex
\documentclass[sigplan,10pt]{acmart}

\renewcommand\footnotetextcopyrightpermission[1]{}
\settopmatter{printfolios=true}

\begin{document}
\title{Your Paper Title}

\author{Paper \#XXX}  % Anonymized
\affiliation{}

\begin{abstract}
Your abstract here.
\end{abstract}

\maketitle
\pagestyle{plain}

% Your paper content

\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
```

**SOSP 2026 特别说明：**
- 可选 Artifact Evaluation
- 作者回复期
- 允许补充材料（审稿人不必读）
- 须对系统名称匿名

## 页数限制汇总

### ML/AI 会议

| 会议 | 投稿 | 终稿 | 说明 |
|------------|-----------|--------------|-------|
| ICML 2026 | 8 pages | 9 pages | +unlimited refs/appendix |
| ICLR 2026 | 9 pages | 10 pages | +unlimited refs/appendix |
| NeurIPS 2025 | 9 pages | 9 pages | +checklist outside limit |
| ACL 2025 | 8 pages (long) | varies | +unlimited refs/appendix |
| AAAI 2026 | 7 pages | 8 pages | +unlimited refs/appendix |
| COLM 2025 | 9 pages | 10 pages | +unlimited refs/appendix |

### 系统会议

| 会议 | 投稿 | 终稿 | 格式 | 说明 |
|------------|-----------|--------------|--------|-------|
| OSDI 2026 | 12 pages | 14 pages | USENIX (8.5×11", 10pt, two-col) | +unlimited refs; encourages concise papers  |
| NSDI 2027 | 12 pages | varies | USENIX (same as OSDI) | +unlimited refs/appendix |
| ASPLOS 2027 | 12 pages | varies | ACM SIGPLAN (10pt, two-col) | +unlimited refs |
| SOSP 2026 | 12 pages | varies | ACM SIGPLAN (10pt, two-col, 7×9" block) | +unlimited refs; supplementary allowed |

## 常见问题

### 编译错误

1. **缺少宏包**：安装完整 TeX 发行版（TeX Live Full 或 MikTeX）
2. **参考文献错误**：使用提供的 `.bst` 文件，配合 `\bibliographystyle{}`
3. **字体警告**：安装 `cm-super` 或使用 `\usepackage{lmodern}`

### 匿名化

投稿版本须确保：
- `\author{}` 中无作者姓名
- 无致谢（Acknowledgments）章节
- 无基金编号
- 使用匿名仓库链接
- 自引以第三人称表述

### 常用 LaTeX 宏包

```latex
% Recommended packages (check compatibility with venue style)
\usepackage{amsmath,amsthm,amssymb}  % Math
\usepackage{graphicx}                 % Figures
\usepackage{booktabs}                 % Tables
\usepackage{hyperref}                 % Links
\usepackage{algorithm,algorithmic}    % Algorithms
\usepackage{natbib}                   % Citations
```

## 更新模板

模板每年更新。每次投稿前请核对官方来源：

**ML/AI：**
- ICML: https://icml.cc/
- ICLR: https://iclr.cc/
- NeurIPS: https://neurips.cc/
- ACL: https://github.com/acl-org/acl-style-files
- AAAI: https://aaai.org/
- COLM: https://colmweb.org/

**Systems**
- OSDI: https://www.usenix.org/conference/osdi26/call-for-papers
- NSDI: https://www.usenix.org/conference/nsdi27/call-for-papers
- ASPLOS: https://www.asplos-conference.org/asplos2026/call-for-papers-asplos27/
- SOSP: https://sigops.org/s/conferences/sosp/2026/cfp.html
- USENIX Templates: https://www.usenix.org/conferences/author-resources/paper-templates
- ACM Templates: https://www.acm.org/publications/proceedings-template
