# 风格预设参考文档

当你需要制作论文图（figures）或统一论文的视觉语言时，可使用本参考文档。它会吸收 `academic-plotting` 中有用的风格预设，同时保留该套件的一条规则：用于图的数据必须是确定性的（exact data must be deterministic）。

## 通用图形规则（Universal Figure Rules）

- 优先选择矢量输出：PDF/SVG/TikZ。
- 栅格图像使用 300 DPI 或更高。
- 使用色盲友好调色板，并且不要只依赖颜色来表达含义。
- 确保所有文字在最终论文尺寸下依然清晰可读；不要出现小于 7 pt 的字号。
- 避免 3D 效果、装饰性渐变、剪贴画、水印，以及“假 UI 外框（fake UI chrome）”。
- 确保同一篇论文中不同图表的风格一致。

## 会议/期刊的图尺寸（Venue Figure Sizes）

| 会议/期刊 | 单栏/主宽度 | 全宽 | 备注 |
|---|---:|---:|---|
| NeurIPS / ICLR 单栏风格 | 5.5 in | 5.5 in | 主文档通常为单栏。 |
| ICML 双栏风格 | 3.25 in | 6.75 in | 全宽图使用 `figure*`。 |
| ACL / EMNLP 双栏风格 | 3.3 in | 6.8 in | 全宽图使用 `figure*`。 |
| AAAI 双栏风格 | 3.3 in | 7.0 in | 保持标注紧凑。 |

一定要核对实际模板（Always check the actual template）。

## 数据绘图预设（Data Plot Preset）

推荐的 matplotlib 默认设置：

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.18,
    "grid.linewidth": 0.6,
})
```

## 调色板（Palettes）

### Okabe-Ito

当你关心对比准确性时使用：

```python
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]
```

### Ocean Dusk

用于更精致的 ML/系统图表：

```python
OCEAN_DUSK = {
    "teal": "#264653",
    "cyan": "#2A9D8F",
    "gold": "#E9C46A",
    "orange": "#F4A261",
    "coral": "#E76F51",
    "gray": "#8C8C8C",
}
OURS = "#E76F51"
BASELINE = "#B0BEC5"
BEST_BASELINE = "#264653"
```

## 图表/示意图风格（Diagram Styles）

### 经典学术（Classic Academic）

用于需要精确系统图的最佳默认选项。

- 白色背景。
- 浅色分段（section bands）。
- 细灰色边框。
- 数据流用实线箭头。
- 失败/重试用红色虚线箭头。
- 尽量少用图标。

### 现代极简（Modern Minimal）

用于清爽的方法概览（method overviews）。

- 布局稀疏。
- 每一组只使用一种强调色。
- 不使用装饰性图标。
- 留出足够大空白。
- 灰色细箭头。

### 草图/白板（Sketch / Whiteboard）

当你需要“可记忆”的概览图、且精确文字受限时使用。

- 暖色偏白背景（off-white）。
- 碳黑描边（charcoal outlines）。
- 柔和的淡填充。
- 手绘线条质感。
- 仅当标签仍可读时才使用。

### 插图式技术（Illustrated Technical）

用于偏解释性、文档风格的示意图。

- 小而一致的线条图标。
- 柔和的分组区域。
- 弯曲箭头。
- 保持文字简短。

## 箭头约定（Arrow Conventions）

| 语义关系 | 样式 |
|---|---|
| data flow（数据流） | 实线箭头，按来源组上色 |
| control flow（控制流） | 灰色实线箭头 |
| feedback/reflection（反馈/反思） | 虚线弯曲箭头 |
| error/failure（错误/失败） | 红色虚线箭头 |
| optional path（可选路径） | 灰色点线箭头 |
| equivalence/comparison（等价/对比） | 双向箭头或方括号标注 |

在所有方法图里使用同一套约定。

