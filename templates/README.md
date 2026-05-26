# LaTeX Templates for ML/AI, CV, and NLP Conferences

This directory contains LaTeX templates for major machine learning, AI, computer vision, and NLP conferences.

Before using or redistributing bundled templates, check `SOURCES.md` and the official venue author instructions. Local templates are convenience copies, not a substitute for current venue requirements.

## Compiling LaTeX to PDF

### Option 1: VS Code with LaTeX Workshop (Recommended)

**Setup:**
1. Install [TeX Live](https://www.tug.org/texlive/) (full distribution recommended)
   - macOS: `brew install --cask mactex`
   - Ubuntu: `sudo apt install texlive-full`
   - Windows: Download from [tug.org/texlive](https://www.tug.org/texlive/)

2. Install VS Code extension: **LaTeX Workshop** by James Yu
   - Open VS Code → Extensions (Cmd/Ctrl+Shift+X) → Search "LaTeX Workshop" → Install

**Usage:**
- Open any `.tex` file in VS Code
- Save the file (Cmd/Ctrl+S) → Auto-compiles to PDF
- Click the green play button or use `Cmd/Ctrl+Alt+B` to build
- View PDF: Click "View LaTeX PDF" icon or `Cmd/Ctrl+Alt+V`
- Side-by-side view: `Cmd/Ctrl+Alt+V` then drag tab

**Settings** (add to VS Code `settings.json`):
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

### Option 2: Command Line

```bash
# Basic compilation
pdflatex main.tex

# With bibliography (full workflow)
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Using latexmk (handles dependencies automatically)
latexmk -pdf main.tex

# Continuous compilation (watches for changes)
latexmk -pdf -pvc main.tex
```

### Option 3: Overleaf (Online)

1. Go to [overleaf.com](https://www.overleaf.com)
2. New Project → Upload Project → Upload the template folder as ZIP
3. Edit online with real-time PDF preview
4. No local installation needed

### Option 4: Other IDEs

| IDE | Extension/Plugin | Notes |
|-----|------------------|-------|
| **Cursor** | LaTeX Workshop | Same as VS Code |
| **Sublime Text** | LaTeXTools | Popular, well-maintained |
| **Vim/Neovim** | VimTeX | Powerful, keyboard-driven |
| **Emacs** | AUCTeX | Comprehensive LaTeX environment |
| **TeXstudio** | Built-in | Dedicated LaTeX IDE |
| **Texmaker** | Built-in | Cross-platform LaTeX editor |

### Troubleshooting Compilation

**"File not found" errors:**
```bash
# Ensure you're in the template directory
cd templates/icml2026
pdflatex example_paper.tex
```

**Bibliography not appearing:**
```bash
# Run bibtex after first pdflatex
pdflatex main.tex
bibtex main        # Uses main.aux to find citations
pdflatex main.tex  # Incorporates bibliography
pdflatex main.tex  # Resolves references
```

**Missing packages:**
```bash
# TeX Live package manager
tlmgr install <package-name>

# Or install full distribution to avoid this
```

## Available Templates and Official Rules

The table below combines bundled template locations with official source/rule pages. Page limits change by year and track; always verify the linked official instructions before active submission.

| Venue | Directory | Official source / rules | Submission limit | Camera-ready / final notes |
|---|---|---|---|---|
| ICML 2026 | `icml2026/` | [ICML Author Instructions](https://icml.cc/Conferences/2026/AuthorInstructions) | 8 main-body pages; unlimited references/appendices | Final version allows 1 extra main-body page; camera-ready PDF limit is 20MB |
| ICLR 2026 | `iclr2026/` | [ICLR Author Guide](https://iclr.cc/Conferences/2026/AuthorGuide), [ICLR template](https://github.com/ICLR/Master-Template) | 9 main-text pages; citations can be additional | Rebuttal/camera-ready main-text limit increases to 10 pages |
| NeurIPS 2025 | `neurips2025/` | [NeurIPS Call for Papers](https://nips.cc/Conferences/2025/CallForPapers), [formatting instructions](https://arxiv.org/html/2506.15953v1) | 9 content pages including figures/tables; references, checklist, and optional appendices excluded | Accepted papers receive 1 extra content page for camera-ready |
| ACL 2025+ | `acl/` | [ACL style files](https://github.com/acl-org/acl-style-files), [ACLPUB formatting](https://acl-org.github.io/ACLPUB/formatting.html) | Long papers: 8 content pages plus unlimited references; short papers: 4 content pages plus unlimited references | Final long papers get 1 extra content page; final short papers get 1 extra content page |
| AAAI 2026 | `aaai2026/` | [AAAI-26 Submission Instructions](https://aaai.org/conference/aaai/aaai-26/submission-instructions/), [AAAI Press camera-ready info](https://proceedings.aaai.org/info) | Main technical track: 7 content pages plus references/reproducibility checklist | Camera-ready limits vary by track; main track allows 7 content pages plus limited ack/ethics/references pages |
| COLM 2025 | `colm2025/` | [COLM 2025 CFP](https://colmweb.org/2025/cfp.html), [COLM template](https://github.com/COLM-org/Template) | 9 main-text pages; citations/appendices additional | Accepted papers may add 1 extra page for camera-ready |
| CVPR 2026 | `cvpr2026/` | [CVPR Author Guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines) | 8 pages including figures/tables; cited references excluded | Rebuttal is a 1-page PDF; verify final camera-ready instructions |
| ICCV 2025 | `iccv2025/` | [ICCV Author Guidelines](https://iccv.thecvf.com/Conferences/2025/AuthorGuidelines), [submission checklist](https://iccv.thecvf.com/Conferences/2025/SubmissionCheckList) | 8 pages including figures/tables; cited references excluded | Rebuttal is a 1-page PDF; verify final camera-ready instructions |
| ECCV 2026 | `eccv2026/` | [ECCV Submission Policies](https://eccv.ecva.net/Conferences/2026/SubmissionPolicies) | 14 pages including figures/tables in LNCS style; cited references excluded | Use the ECCV 2026 LNCS template; template/font/margin changes may cause desk rejection |


## Usage

### ICML 2026

```latex
\documentclass{article}
\usepackage{icml2026}  % For submission
% \usepackage[accepted]{icml2026}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

Key files:
- `icml2026.sty` - Style file
- `icml2026.bst` - Bibliography style
- `example_paper.tex` - Example document

### ICLR 2026

```latex
\documentclass{article}
\usepackage[submission]{iclr2026_conference}  % For submission
% \usepackage[final]{iclr2026_conference}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

Key files:
- `iclr2026_conference.sty` - Style file
- `iclr2026_conference.bst` - Bibliography style
- `iclr2026_conference.tex` - Example document

### ACL Venues (ACL, EMNLP, NAACL)

```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}  % For review
% \usepackage{acl}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

Key files:
- `acl.sty` - Style file
- `acl_natbib.bst` - Bibliography style
- `acl_latex.tex` - Example document

### AAAI 2026

```latex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai2026}  % For submission
% \usepackage{aaai2026}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

Key files:
- `aaai2026.sty` - Style file
- `aaai2026.bst` - Bibliography style

### COLM 2025

```latex
\documentclass{article}
\usepackage[submission]{colm2025_conference}  % For submission
% \usepackage[final]{colm2025_conference}  % For camera-ready

\begin{document}
% Your paper content
\end{document}
```

Key files:
- `colm2025_conference.sty` - Style file
- `colm2025_conference.bst` - Bibliography style

## Common Issues

### Compilation Errors

1. **Missing packages**: Install full TeX distribution (TeX Live Full or MikTeX)
2. **Bibliography errors**: Use the provided `.bst` file with `\bibliographystyle{}`
3. **Font warnings**: Install `cm-super` or use `\usepackage{lmodern}`

### Anonymization

For submission, ensure:
- No author names in `\author{}`
- No acknowledgments section
- No grant numbers
- Use anonymous repositories
- Cite own work in third person

### Common LaTeX Packages

```latex
% Recommended packages (check compatibility with venue style)
\usepackage{amsmath,amsthm,amssymb}  % Math
\usepackage{graphicx}                 % Figures
\usepackage{booktabs}                 % Tables
\usepackage{hyperref}                 % Links
\usepackage{algorithm,algorithmic}    % Algorithms
\usepackage{natbib}                   % Citations
```

## Updating Templates

Templates are updated annually. Before each submission, verify the official source/rule links in the table above and update `SOURCES.md` if a bundled template changes.
