# 图表工作流参考文档

当你要为论文规划、生成或修改图表（figures）时使用本参考文档。

在开始规划图之前先加载 `figure-spec.zh-CN.md`，当你需要确定视觉风格或会议尺寸时加载 `style-presets.zh-CN.md`。
（如果你当前使用的是英文版本，这两处对应英文为 `figure-spec.md` 与 `style-presets.md`。）

## 必要的图表规划（Required Figure Plan）

在你开始生成图表之前，先创建 `figures/figure_plan.md`。
对每一张图，需要指定：

- **角色（Role）**：overview、method detail、result summary、ablation、teaser、failure analysis。
- **信息（Message）**：这张图应该传达的“单一主张”（the single claim the figure should communicate）。
- **实体（Entities）**：模块、输入、输出、指标或数据集。
- **关系（Relationships）**：箭头、分组、反馈回路、对比。
- **布局（Layout）**：水平流水线、两行流程、分组柱状图、热力图、网格等。
- **后端（Backend）**：确定性绘图、TikZ/SVG、图像生成，或混合（hybrid）。
- **fallback**：如果生成资源不存在，论文如何成功编译（how the paper compiles if generated assets are absent）。

对于更大的项目，使用 `figure-spec.zh-CN.md` 里的 schema，并把 spec 存在 `figures/figure_specs.yaml` 或 `figures/figure_specs.md`。

## 后端选择（Backend Selection）

- 对数值结果使用确定性绘图（deterministic plotting）。优先选择 matplotlib/seaborn 或直接生成 SVG/PDF。不要使用图像生成（image generation）用于精确数字。
- 当你需要把 CSV 精确转换为 LaTeX 表格、且表格数值必须可审计时，使用 `scripts/make_latex_table.py`。
- 当你需要精确文字与箭头时，用 TikZ/SVG 做图。
- 只有在图用于更精致的概览/预告（teaser）且文字精度不关键，或者存在 fallback 时，才使用图像生成。
- 对于带标签的生成图，提交前先检查图像。如果文字变形，就改用 TikZ/SVG。

## 图表类型（Figure Types）

按图表要支撑的主张类型选择：

| 主张类型 | 推荐图表 | 备注 |
|---|---|---|
| 系统/工作流贡献 | 流水线图或架构图 | 展示工件、控制流、反馈与确定性/LLM 边界。 |
| 主量化对比 | 表格或分组柱状图 | 当很多“精确数字”必须存在时表格通常更好。 |
| 随时间/迭代的进展 | 折线图（line plot） | 若有不确定性运行，则加入置信区间。 |
| 消融 | 分组柱状图或小倍数（small multiples） | 突出被移除的组件以及其后果。 |
| 难度分解 |分层表格、热力图或分面柱状图 | 在 caption 或周边文字中保持 level 定义清晰。 |
| 失败分析 | 定性案例网格 + 简短标注 | 只使用能体现“论文层级观点”的示例。 |

避免装饰性图表。图表应通过让主张更易理解或更易验证来“赚取空间”。

## 数据绘图标准（Data Plot Standards）

针对数值图：

- 源数据必须来自脚本、CSV/JSON、notebook 导出的表格，或有文档说明的结果文件。
- 绘图脚本应当能从源数据重新生成精确资源。
- 矢量输出优先用 PDF/SVG；当场地方/工具链只接受栅格时才用 PNG。
- 栅格图至少使用 300 DPI。
- 对比使用色盲友好调色板。Okabe-Ito 是一个安全默认：
  `#E69F00`, `#56B4E9`, `#009E73`, `#F0E442`, `#0072B2`, `#D55E00`, `#CC79A7`。
- 在所有图里一致突出“提出的方法”。
- 不要使用 3D 柱状图、用饼图进行 ML 对比、过度网格线、或未解释的双轴（dual axes）。
- 在坐标轴标签或 caption 里体现指标方向（metric direction）。

推荐的 matplotlib 默认设置：

```python
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "legend.fontsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
})
```

简单对比用单栏宽度；只有当密度要求时才使用全宽图。

## 示意图（diagram）提示词模板（Diagram Prompt Template）

对“图像生成的示意图”，需要包含：

1. 会议与图的目的。
2. 使用精确调色板的视觉风格。
3. 画布宽高比（canvas aspect ratio）。
4. 布局分区（layout regions）。
5. 精确标签（exact labels）。
6. 箭头与反馈路径。
7. 约束：不出现 logo、不出现水印、不使用不支持的术语、不生成过小文字。

### 示例提示词结构（Diagram Prompt Structure）

对生成的概览示意图，使用下面六段式提示：

1. **Framing**：会议、分节、读者应获得的 takeaway，以及语气（tone）。
2. **Visual style**：干净学术、草图、现代极简或技术插图（technical illustration）。
3. **Color palette**：精确 hex 码（hex codes）与一致语义含义。
4. **Layout**：分区、面板（panels）、组件、间距、阅读顺序。
5. **Connections**：每一条箭头、反馈回路、虚线失败路径（dashed failure path）、以及标签。
6. **Constraints**：不出现编造的标签（hallucinated labels）、不出现过小文字、不出现 logo、不出现假数字、不做不支持的主张。

生成示意图在“尽量减少文字”时效果更好。
如果精确标签非常关键，就做一个 TikZ/SVG 版本。

## LaTeX fallback 模式（LaTeX Fallback Pattern）

对生成图表使用如下模式：

```latex
\IfFileExists{figures/name_generated.png}{%
  \includegraphics[width=\linewidth]{figures/name_generated.png}
}{%
  \input{figures/name_tikz}
}
```

对于结果绘图（result plots），优先用 PDF：

```latex
\IfFileExists{figures/result.pdf}{%
  \includegraphics[width=\linewidth]{figures/result.pdf}
}{%
  \includegraphics[width=\linewidth]{figures/result.png}
}
```

## 提交前图质量检查（Figure Quality Checklist）

- 图是否只传达一个明确消息（one message）？
- 文字在最终论文尺寸下是否可读？
- 精确数字是否由代码生成，而不是图像模型生成？
- 当需要比较时颜色是否色盲友好？
- 是否有源文件或提示词以便重新生成？
- caption 是否自包含（self-contained）？
- 论文正文是否提到该图并解释其 takeaway？

## caption 写作模式（Caption Pattern）

caption 应当像一个小型论证（miniature argument）：

1. 定义显示了什么。
2. 写清指标方向或视觉编码（visual encoding）。
3. 给出 takeaway。
4. 只有在解释需要时才写 caveats。

示例模式：

```text
Figure X: Overview of METHOD. The workflow converts ... into ... by separating ...
Dashed arrows indicate reflection or retry paths. This separation lets ... while preserving ...
```

## 提交前 QA（QA Before Submission）

- 在最终图的纸面宽度下查看图。
- 当颜色用于比较编码时，用灰度检查可读性。
- 确认每个标签都与论文术语一致。
- 确认每个数字都与源数据一致。
- 确认图文件没有不必要地过大。
- 确认每张图在正文中都被引用（在出现前后）。

