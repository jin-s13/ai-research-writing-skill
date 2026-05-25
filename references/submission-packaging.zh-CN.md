# 投稿打包参考文档

当你准备为本地构建（local build）、Overleaf、arXiv、camera-ready，或 Git 投稿准备草稿时使用本参考文档。

## 打包原则（Packaging Principle）

投稿打包应当满足：可构建（buildable）、可审计（auditable）、且不包含意外占位符（accidental placeholders）。
如果源代码树中仍存在未解决的引用（unresolved citations）、断裂的图路径（broken figure paths）、陈旧的生成资源（stale generated assets），或隐藏的 TODO，就不要把“看起来很精致的 PDF”当作足够。

## 构建工作流（Build Workflow）

1. 确定主 `.tex` 文件。
2. 确定参考文献文件与参考文献工具：BibTeX、biblatex 或 natbib。
3. 如果有对应会议/模板兼容的构建命令就运行它。
4. 把结果记录在 `build_check.md`。
5. 如果缺少 TeX 工具，记录缺失命令，并在可能的情况下仍跑静态检查（static checks）。

推荐的 BibTeX 构建：

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

如果可用，推荐 latexmk 构建：

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## 静态检查（Static Checks）

视情况运行：

```bash
python scripts/check_citations.py main.tex references.bib
python scripts/check_todos.py main.tex checklist.tex references.bib figures
python scripts/parse_build_log.py main.log
python scripts/camera_ready_check.py main.tex
```

同时检查：

- 缺失的图文件。
- 重复的 BibTeX keys。
- 存在构建日志时，留意 overfull/underfull box 警告。
- 未定义引用与 citation。
- 匿名投稿中的占位作者姓名。
- 匿名投稿中意外出现的致谢（acknowledgments）。

## 工件卫生（Artifact Hygiene）

提交前：

- 保留用于绘图和示意的源文件。
- 对于精确图表，优先选择矢量格式。
- 大型 PNG 只在质量仍可接受时才压缩。
- 删除 `.DS_Store`、临时的 TeX 文件、陈旧 PDF，以及失败的生成尝试，除非你有意归档。
- 不要提交私有数据集、API key、凭据（credentials）、或本地绝对路径。
- 确认生成图表与论文正文文字、caption 对得上。

## Overleaf / Git 工作流

对于与 Overleaf 绑定的仓库：

1. 运行 `git status --short`。
2. 检查修改过的文件与生成资源。
3. 跑 citation/TODO/build 检查。
4. 只暂存（stage）你确实要提交的文件。
5. 用简洁信息提交（commit）。
6. 只有当用户要求你推送（push）或已明确授权时才推送。
7. 确认远端分支，并查看推送结果。

打包时，不要撤销与用户无关的修改。

## 投稿就绪模板（Submission Readiness Template）

创建或更新 `submission_readiness.md`：

```text
Target venue:
Template:
Main tex:
Build status:
Citation check:
TODO/placeholder check:
Checklist status:
Limitations status:
Reproducibility status:
Figure/source status:
Known reviewer risks:
Known packaging risks:
Next actions:
```

## Camera-Ready 的差异（Camera-Ready Differences）

在最终/相机就绪模式下，还要额外检查：

- 作者姓名、单位与致谢（acknowledgments）。
- 许可证以及数据/代码链接。
- 更新 arXiv 或补充材料（supplementary references）。
- 审稿人要求的修改。
- 附录之间的交叉引用。
- 最终页数上限与文件大小上限。

## 最终回复合同（Final Response Contract）

当你报告“打包工作”时，包含：

- 改动了哪些文件。
- 跑了哪些检查，以及结果如何。
- 构建状态。
- 仍然存在的阻塞项（blockers）。
- 如果有提交或推送，附上 commit 或 push hash。

