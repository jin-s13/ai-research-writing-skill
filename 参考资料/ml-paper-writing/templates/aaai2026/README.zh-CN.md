# AAAI 2026 统一 LaTeX 模板使用说明

> **📝 重要说明**：本仓库借助 Cursor 在 AAAI 2026 官方模板基础上改进得到。如遇不满足要求或与官方冲突之处，请积极提交 issues。

## 在线查看

**📖 在线阅读与测试模板**：[https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07](https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07)

💡 **提示**：可通过上述链接在 Overleaf 中直接查看、编辑与编译模板，无需本地安装 LaTeX。

---

## 概述

已将 AAAI 2026 的两个版本（匿名投稿版与 camera-ready 版）**完整合并**为统一模板文件 `aaai2026-unified-template.tex`。

该模板包含原始两个模板的**全部内容**（共 886 行，比原始文件更完整），包括：

- 全部排版说明与要求
- 完整示例代码与表格
- 图片处理指南
- 参考文献格式要求
- 所有章节与附录
- 各版本特有的 Acknowledgments 部分

## 主要差异

对比两个原始模板，主要差异如下：

### 1. 宏包加载方式

- **匿名版**：`\usepackage[submission]{aaai2026}`
- **Camera-ready 版**：`\usepackage{aaai2026}`

### 2. 标题

- **匿名版**："AAAI Press Anonymous Submission Instructions for Authors Using LaTeX"
- **Camera-ready 版**："AAAI Press Formatting Instructions for Authors Using LaTeX --- A Guide"

### 3. Links 环境

- **匿名版**：Links 环境被注释，防止泄露作者身份
- **Camera-ready 版**：Links 环境正常显示

### 4. 内容章节

- **匿名版**：含 “Preparing an Anonymous Submission” 专节说明
- **Camera-ready 版**：含完整格式说明与版权信息

## 依赖文件

✅ **已验证并复制到主目录的文件**：

- `aaai2026.sty` — AAAI 2026 样式文件（两版相同）
- `aaai2026.bst` — 参考文献样式（两版相同）
- `aaai2026.bib` — 示例参考文献
- `figure1.pdf`、`figure2.pdf` — 示例图片

上述文件在两版中一致，统一模板可正常编译。

## 如何使用统一模板

### 切换到匿名投稿版

在模板第 11 行**取消注释**：

```latex
\def\aaaianonymous{true}
```

### 切换到 Camera-ready 版

在第 11 行**注释或删除**：

```latex
% \def\aaaianonymous{true}
```

## 一键切换机制

统一模板使用 LaTeX 条件编译：

```latex
% 条件包加载
\ifdefined\aaaianonymous
    \usepackage[submission]{aaai2026}  % 匿名版本
\else
    \usepackage{aaai2026}              % Camera-ready版本
\fi

% 条件标题设置
\ifdefined\aaaianonymous
    \title{AAAI Press Anonymous Submission\\Instructions for Authors Using \LaTeX{}}
\else
    \title{AAAI Press Formatting Instructions \\for Authors Using \LaTeX{} --- A Guide}
\fi

% 条件内容显示
\ifdefined\aaaianonymous
    % 匿名版本特有内容
\else
    % Camera-ready版本特有内容
\fi
```

## 文件清单

主目录包含：

- `aaai2026-unified-template.tex` — 统一主论文模板
- `aaai2026-unified-supp.tex` — 统一补充材料模板
- `aaai2026.sty` — AAAI 2026 LaTeX 样式
- `aaai2026.bst` — 参考文献样式
- `aaai2026.bib` — 示例参考文献
- `figure1.pdf`、`figure2.pdf` — 示例图片
- `README.md` — 英文说明（本文件为中文版）

## 补充材料模板

### 概述

`aaai2026-unified-supp.tex` 专为 AAAI 2026 补充材料设计，与主论文模板使用相同的版本切换机制。

### 主要功能

- **版本切换**：修改一行即可在匿名投稿与 camera-ready 间切换
- **补充内容**：支持额外实验、推导、数据、图表、算法等
- **格式一致**：与主论文模板要求完全一致
- **代码示例**：含算法、代码列表等示例

### 用法

与主论文相同，修改第 11 行：

```latex
% 匿名投稿版本
\def\aaaianonymous{true}

% Camera-ready版本
% \def\aaaianonymous{true}
```

### 补充材料内容建议

- 额外实验结果与消融研究
- 详细数学推导与证明
- 更多图表与可视化
- 算法伪代码与实现细节
- 数据集描述与预处理步骤
- 超参数与实验配置
- 失败案例分析
- 计算复杂度分析

## 使用检查清单

### 📋 投稿前

**版本设置**：

- [ ] 已设置 `\def\aaaianonymous{true}`（匿名投稿）
- [ ] 已注释可能暴露身份的信息
- [ ] 参考文献已匿名化（移除作者姓名）

**内容完整性**：

- [ ] 标题、摘要、关键词已填写
- [ ] 各章节完整
- [ ] 图表编号连续正确
- [ ] 参考文献格式正确
- [ ] 补充材料（如有）已准备

**格式**：

- [ ] 页边距符合要求
- [ ] 字体与字号正确
- [ ] 行距符合标准
- [ ] 图表位置与大小合适
- [ ] 数学公式格式正确

**技术**：

- [ ] LaTeX 编译无错误
- [ ] 参考文献正确生成
- [ ] PDF 输出正常
- [ ] 文件大小在限制内

### 📋 录用后

**版本切换**：

- [ ] 已注释 `\def\aaaianonymous{true}`（camera-ready）
- [ ] 已添加完整作者信息
- [ ] 已添加各单位信息
- [ ] 已恢复被注释内容

**内容更新**：

- [ ] 已按审稿意见修改
- [ ] 已更新图表与实验
- [ ] 补充材料已完善
- [ ] 链接与引用已检查

**终检**：

- [ ] 终稿 PDF 质量检查
- [ ] 文件已备份
- [ ] 符合会议终稿提交要求
- [ ] 补充材料已单独提交（如需要）

### 📋 补充材料

**内容组织**：

- [ ] 与主论文内容对应
- [ ] 章节结构清晰
- [ ] 图表编号不与主文冲突
- [ ] 参考文献格式一致

**技术细节**：

- [ ] 算法伪代码完整清晰
- [ ] 实验设置说明充分
- [ ] 数据预处理步骤明确
- [ ] 超参数配置完整

**格式**：

- [ ] 使用统一 supp 模板
- [ ] 页面设置与主文一致
- [ ] 字体与格式符合要求
- [ ] 文件大小在限制内

## 使用建议

1. **投稿阶段**
   - 取消注释 `\def\aaaianonymous{true}`
   - 确保无暴露身份的信息
   - 检查参考文献是否已匿名化

2. **录用后准备终稿**
   - 注释或删除 `\def\aaaianonymous{true}`
   - 添加完整作者与单位信息
   - 按需取消注释 links 环境

3. **编译测试**
   - 两种模式分别编译，确认均可通过
   - 检查 PDF 是否符合要求
   - 验证参考文献格式

4. **依赖文件**
   - 确保所有依赖与 `.tex` 同目录
   - 移动模板时一并移动依赖文件

## 重要注意事项

⚠️ **关于 Bibliography Style**：

- `aaai2026.sty` 已自动设置 `\bibliographystyle{aaai2026}`
- **不要**在正文中再次添加 `\bibliographystyle{aaai2026}`
- 否则会报 "`Illegal, another \bibstyle command`" 错误
- 仅需使用 `\bibliography{aaai2026}`

## 编译示例

```bash
# 编译LaTeX文档
pdflatex aaai2026-unified-template.tex
bibtex aaai2026-unified-template
pdflatex aaai2026-unified-template.tex
pdflatex aaai2026-unified-template.tex
```

## 常见问题

### 1. "Illegal, another \bibstyle command" 错误

**原因**：重复设置 bibliography style  
**解决**：删除正文中的 `\bibliographystyle{aaai2026}`，由 `aaai2026.sty` 自动处理

### 2. 参考文献格式不正确

**原因**：可能缺少 natbib 或 BibTeX 文件问题  
**解决**：按标准流程编译：pdflatex → bibtex → pdflatex → pdflatex

---

## 版本信息

- **模板版本**：AAAI 2026 Unified（主文 + 补充材料）
- **创建日期**：2024 年 12 月
- **支持格式**：匿名投稿与 Camera-Ready
- **模板类型**：主论文模板与补充材料模板
- **兼容性**：LaTeX 2020+ / TeXLive 2024+

---

🎉 **只需修改一行代码即可在两版间切换，所需依赖文件均已就绪！**
