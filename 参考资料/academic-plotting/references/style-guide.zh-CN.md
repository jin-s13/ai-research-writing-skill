# ML 论文图表发表样式指南

主要 ML/AI 会议论文图表样式标准。

## 通用规则

1. **优先矢量格式** — LaTeX 用 PDF；PNG 仅用于 AI 生成示意图
2. **栅格图最低 300 DPI**
3. **色盲安全色板** — 勿仅靠颜色区分；辅以标记、图案或标签
4. **风格一致** — 全文图表共用字体、颜色与样式
5. **自包含** — 不读 caption 也应能理解每张图
6. **无装饰元素** — 无阴影、3D、渐变或剪贴画

## 各 Venue 图幅尺寸

### NeurIPS

| 版式 | 宽度 | 说明 |
|--------|-------|-------|
| 单栏 | 5.5 in | NeurIPS 为单栏 |
| 半宽 | 2.65 in | 栏内并排 |
| 最大高度 | 9 in | 整页 |

模板：`\usepackage[final]{neurips_2025}`

### ICML

| 版式 | 宽度 | 说明 |
|--------|-------|-------|
| 单栏 | 3.25 in | ICML 为双栏 |
| 通栏 | 6.75 in | `\begin{figure*}` |
| 最大高度 | 9.25 in | 整页 |

模板：`\usepackage{icml2026}`

### ICLR

| 版式 | 宽度 | 说明 |
|--------|-------|-------|
| 单栏 | 5.5 in | ICLR 为单栏 |
| 最大高度 | 9 in | 整页 |

模板：`\usepackage{iclr2026_conference}`

### ACL / EMNLP

| 版式 | 宽度 | 说明 |
|--------|-------|-------|
| 单栏 | 3.3 in | ACL 为双栏 |
| 通栏 | 6.8 in | `\begin{figure*}` |

模板：`\usepackage[hyperref]{acl2025}`

### AAAI

| 版式 | 宽度 | 说明 |
|--------|-------|-------|
| 单栏 | 3.3 in | AAAI 为双栏 |
| 通栏 | 7.0 in | `\begin{figure*}` |

## 色板

### 推荐色盲安全色板

下列色板在各种色觉下均可区分：

```python
# "deep" variant — high contrast, good for lines and bars
PALETTE_DEEP = [
    "#4C72B0",  # blue
    "#DD8452",  # orange
    "#55A868",  # green
    "#C44E52",  # red
    "#8172B3",  # purple
    "#937860",  # brown
    "#DA8BC3",  # pink
    "#8C8C8C",  # gray
]
```

### 双色方案（ours vs baseline）

```python
# High contrast pair
OURS = "#C44E52"     # red — stands out
BASELINE = "#8C8C8C" # gray — recedes

# Alternative pair
OURS = "#4C72B0"     # blue
BASELINE = "#DD8452"  # orange
```

### 渐变色方案（热力图 / 连续数据）

| 用途 | Colormap | 代码 |
|----------|----------|------|
| 单变量（0 到 max） | Blues | `cmap="Blues"` |
| 发散（负到正） | RdBu_r | `cmap="RdBu_r"` |
| 感知均匀 | viridis | `cmap="viridis"` |
| 相关矩阵 | coolwarm | `cmap="coolwarm"` |
| 注意力权重 | YlOrRd | `cmap="YlOrRd"` |

### 应避免的颜色

- **纯红 + 纯绿** — 约 8% 男性难以区分
- **彩虹/jet 色图** — 感知不均匀，易误导
- **白底浅黄** — 对比不足
- **霓虹/高饱和色** — 学术论文中显得不专业

## 字体排印

### 与 LaTeX 文档字体匹配

| 会议 | 正文字体 | 图中字体设置 |
|-----------|---------------|-------------------|
| NeurIPS | Times | `font.family: serif`, `font.serif: Times New Roman` |
| ICML | Times | 同 NeurIPS |
| ICLR | Times | 同 NeurIPS |
| ACL | Times | 同 NeurIPS |
| AAAI | Times | 同 NeurIPS |

### 字号指南

| 元素 | 字号 | 理由 |
|---------|------|-----------|
| 坐标轴标签 | 10-11pt | 印刷尺寸下可读 |
| 刻度标签 | 8-9pt | 略小但清晰 |
| 图例文字 | 8-9pt | 紧凑可读 |
| 标题（若有） | 11-12pt | 通常省略（caption 即标题） |
| 标注 | 7-8pt | 最小可读字号 |

**规则**：印刷成品中图中文字不得小于 7pt。

### 数学排版

```python
# For inline math
ax.set_xlabel(r"Number of parameters $N$")

# For display math
ax.set_ylabel(r"Loss $\mathcal{L}(\theta)$")

# Greek letters
ax.set_xlabel(r"Learning rate $\alpha$")

# Subscripts/superscripts
ax.set_ylabel(r"$R^2$ score")
```

## 版式惯例

### 图例位置

优先级：
1. **图内**（左上或右上），空间允许时
2. **图下方**：`bbox_to_anchor=(0.5, -0.15), loc="upper center", ncol=N`
3. **图右侧**：`bbox_to_anchor=(1.05, 1), loc="upper left"`（占额外宽度）

```python
# Clean legend (no frame, no extra spacing)
ax.legend(frameon=False, loc="upper left", handlelength=1.5)

# External legend below
ax.legend(frameon=False, bbox_to_anchor=(0.5, -0.15),
          loc="upper center", ncol=4)
```

### 网格线

```python
# Subtle grid (recommended)
ax.grid(True, alpha=0.3, linestyle="--", linewidth=0.5)

# Major grid only (for log-scale plots)
ax.grid(True, which="major", alpha=0.3, linestyle="--")
ax.grid(True, which="minor", alpha=0.1, linestyle=":")
```

### 坐标轴样式

```python
# Remove top and right spines (clean look)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Reduce tick padding
ax.tick_params(axis="both", which="major", pad=3)
```

### 多面板标签

```python
# Standard (a), (b), (c) labels
for i, ax in enumerate(axes.flat):
    ax.set_title(f"({chr(97 + i)})", loc="left", fontweight="bold", fontsize=11)

# Or as text annotation
ax.text(-0.1, 1.05, "(a)", transform=ax.transAxes,
        fontsize=12, fontweight="bold", va="top")
```

## 示意图样式标准

AI 生成的架构/系统示意图：

### 专业示意图色板

```
Section accents:  Blue #4A90D9, Teal #5BA58B, Amber #D4A252, Slate #7B8794
Failure/error:    Red #D94A4A (dashed lines)
Section fill:     #F7F7F5 (very pale warm gray)
Box borders:      #DDDDDD
Box fill:         #FFFFFF
Primary text:     #333333
Secondary text:   #666666
Background:       #FFFFFF
```

### 示意图版式模式

| 模式 | 适用场景 | 描述 |
|---------|-------------|-------------|
| 水平条带 | 分层架构 | 纵向堆叠分区，框横向排列 |
| 自左向右 | 顺序流水线 | 输入 → 处理 → 输出 |
| 中心辐射 | 中心组件 | 中心节点向外连接 |
| 网格 | 组件矩阵 | 规整排列便于对比 |
| 树形 | 层级决策 | 自上而下分支 |

### 箭头惯例

| 箭头类型 | 样式 | 用途 |
|-----------|-------|-------|
| 数据流 | 实线，与源同色 | 正常信息传递 |
| 控制流 | 实线灰色 | 编排信号 |
| 错误/失败 | 红色虚线 | 失败路径、反驳 |
| 可选 | 灰色点线 | 条件路径 |
| 双向 | 双箭头 | 相互依赖 |

## LaTeX 集成

### 基本插图

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig_name.pdf}
  \caption{Clear description of what the figure shows. Best viewed in color.}
  \label{fig:name}
\end{figure}
```

### 通栏图（双栏 venue）

```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/fig_overview.pdf}
  \caption{System overview showing the three main components.}
  \label{fig:overview}
\end{figure*}
```

### 并排子图

```latex
\begin{figure}[t]
  \centering
  \begin{subfigure}[b]{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{figures/fig_a.pdf}
    \caption{Training loss}
    \label{fig:a}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{figures/fig_b.pdf}
    \caption{Evaluation accuracy}
    \label{fig:b}
  \end{subfigure}
  \caption{Training dynamics. (a) Loss decreases steadily. (b) Accuracy plateaus after 50K steps.}
  \label{fig:training}
\end{figure}
```

### Caption 最佳实践

- **首句**：说明图的内容（可独立理解）
- **要点**：读者应注意到什么
- **颜色说明**：若颜色承载含义，写「Best viewed in color」
- **避免「Figure X shows…」** — 图号已标明

好：「不同模型规模的训练 loss。更大模型收敛更快且最终 loss 更低。」
差：「Figure 3 shows the training loss for different model sizes.」

## 无障碍检查清单

- [ ] 灰度打印可读
- [ ] 印刷成品中文字不小于 7pt
- [ ] 使用色盲安全色板
- [ ] 除颜色外还有线型/标记区分
- [ ] 数据与背景对比度高
- [ ] 坐标轴标签存在且可读
- [ ] 图例清晰、不遮挡数据
