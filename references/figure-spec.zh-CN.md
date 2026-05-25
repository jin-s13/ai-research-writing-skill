# 图表规格参考文档

在你制作任何论文图（paper figure）之前，先使用本参考文档。
它吸收了 `academic-plotting` 中关于角色/信息/实体/布局/后端（backend）的工作流，并把评审所需要的关键信息显式化。

## 必要的图表规格（Required Figure Spec）

对每一张图，在生成素材之前都要先创建该规格（spec）：

```yaml
figure_id: fig:overview
filename: figures/fig_overview
role: overview | method-detail | result-summary | ablation | failure-analysis | teaser | appendix
message: "The sentence the figure supports."
entities:
  - name: "Input"
    type: artifact | module | dataset | metric | baseline | output
    description: "What it represents."
relationships:
  - source: "Input"
    target: "Planner"
    relation: data-flow | control-flow | feedback | comparison | failure-path
layout: left-to-right pipeline | horizontal bands | two-row process | grouped bars | line plot | heatmap | table
backend: deterministic-plot | latex-table | tikz | svg | generated-image | hybrid
source: "CSV/log/script/prompt path"
fallback: "TikZ/SVG/PDF/PNG fallback path"
caption_takeaway: "The sentence the caption must communicate."
evidence_status: exact-data | illustrative-only | qualitative-example
```

## 图表角色分类（Figure Role Taxonomy）

| 角色 | 目的 | 典型后端 |
|---|---|---|
| overview | 解释整个方法或系统 | 带 fallback 的 TikZ/SVG/generated-image |
| method-detail | 解释一个模块、约束不变量（invariant）或接口 | TikZ/SVG |
| result-summary | 支撑主量化主张 | 确定性绘图（deterministic plot）或表格 |
| ablation | 展示哪些设计选择真正重要 | 确定性绘图或表格 |
| difficulty breakdown | 用子集/等级解释性能 | 确定性绘图或热力图（heatmap） |
| failure-analysis | 展示系统性失败模式 | 定性网格（qualitative grid）+ 标注 |
| teaser | 让任务与输出直观易懂 | 生成图像或策划示例 |

## 后端规则（Backend Rules）

- `deterministic-plot`：所有数值型图表都必须使用。
- `latex-table`：适用于精确数值、很多指标、或排行榜式对比。
- `tikz`/`svg`：当精确标签与箭头非常关键时使用。
- `generated-image`：仅当图用于“示意/说明（illustrative）”，且文字精度不那么关键时使用。
- `hybrid`：当生成视觉图与确定性标签或 TikZ fallback 配套时可使用。

对于精确数字、坐标轴刻度、指标值或表格，永远不要使用图像生成（image generation）。

## 数据图选择（Data Chart Selection）

| 数据形态 | 图表 |
|---|---|
| steps/time x metric | 折线图（line plot） |
| methods x metrics | 分组柱状图或表格 |
| 很多方法按一个指标排序 | 横向条形图（horizontal bar chart） |
| 矩阵或两两得分（pairwise scores） | 热力图（heatmap） |
| 分布（distribution） | 箱线图/小提琴图/直方图 |
| 两个连续变量 | 散点图（scatter plot） |
| 精确基准报告 | LaTeX 表格 |

不确定时：精确数字用表格，趋势用折线/曲线类图。

## 图表规划检查清单（Figure Plan Checklist）

- 这张图是否只有一个明确信息（one message）？
- 这个信息是否对应论文的一个主张？
- 图中的所有实体是否使用与论文一致的命名（terminology）？
- 布局是否与关系类型（relationship type）匹配？
- 后端风险（backend risk）与图内容是否匹配？
- 是否列出了源文件（source file）？
- 生成图是否有 fallback？
- caption takeaway 是否在最终样式之前就写好？

## Caption 合同（Caption Contract）

标题/说明（caption）不应只是描述视觉元素。
请按以下方式写：

```text
Figure X: [What is shown]. [How to read it]. [Takeaway]. [Caveat if needed].
```

对于量化图：包含指标方向（metric direction）以及数值统计方式（mean/median/std/confidence interval/单次运行）。

