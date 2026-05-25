---
name: academic-plotting
description: 根据研究上下文为 ML 论文生成可发表质量的图表。给定论文章节或描述时，提取系统组件与关系，通过 Gemini 生成架构图；给定实验结果或数据时，自动选择图表类型，用 matplotlib/seaborn 生成数据驱动图。在撰写会议论文任意图表时使用。
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Academic Writing, Visualization, Matplotlib, Seaborn, Plotting, Figures, Diagrams, NeurIPS, ICML, ICLR, LaTeX]
dependencies: [matplotlib>=3.8.0, seaborn>=0.13.0, numpy, google-genai>=1.0.0]
---

# ML 论文学术绘图

为 ML/AI 会议论文生成可发表质量的图表。两条独立工作流：

1. **示意图**（架构、系统设计、工作流、流水线）— 通过 Gemini 的 AI 图像生成
2. **数据图**（折线图、柱状图、散点图、热力图、消融）— matplotlib/seaborn

## 何时使用哪条工作流

| 图表类型 | 工具 | 原因 |
|-------------|------|-----|
| 架构 / 系统示意图 | Gemini（工作流 1） | 含方框、箭头、标签的复杂空间布局 |
| 工作流 / 流水线 / 生命周期 | Gemini（工作流 1） | 多步骤流程与连接关系 |
| 柱状图、折线图、散点图 | matplotlib（工作流 2） | 精确数值、可复现 |
| 热力图、混淆矩阵 | matplotlib/seaborn（工作流 2） | 结构化网格数据 |
| 消融表转图表 | matplotlib（工作流 2） | 分组柱或折线对比 |
| 饼图 / 环形图 | matplotlib（工作流 2） | 比例数据（ML 论文中慎用） |
| 训练曲线 | matplotlib（工作流 2） | 随 step/epoch 的 loss/accuracy |

**经验法则**：图有数值坐标轴 → 用 matplotlib；有方框和箭头 → 用 Gemini。

---

## 步骤 0：上下文分析与提取

用户通常提供下列输入之一，而非现成的规格说明：

| 输入类型 | 示例 | 需提取内容 |
|-----------|---------|-----------------|
| 全文 / 章节草稿 | 「这是我们的方法章节……」 | 系统组件、关系、数据流 |
| 描述段落 | 「我们的系统有三层……」 | 关键实体、层级、连接 |
| 原始结果 / 数据表 | 「MMLU: 85.2, HumanEval: 72.1……」 | 指标、方法、对比结构 |
| CSV / JSON 数据 | 实验日志文件 | 变量、趋势、分组维度 |
| 模糊请求 | 「给 overview 做一张图」 | 阅读周边论文上下文推断内容 |

### 提取工作流

**示意图**（研究上下文 → 架构图）：

1. **阅读提供的上下文** — 论文章节、摘要或描述段落
2. **识别视觉实体** — 主要组件/模块/阶段有哪些？
   - 关注：代表系统部分的专有名词、命名模块、层、阶段
   - 计数：若顶层实体 >8，考虑合并为分区
3. **识别关系** — 组件如何连接？
   - 关注：描述数据流的动词（「发送至」「查询」「流入」）
   - 分类：数据流（实线箭头）、控制流（灰色）、错误路径（红色虚线）
4. **确定版式模式**：
   - 顺序流水线 → 自左向右
   - 分层架构 → 水平条带纵向堆叠
   - 中心辐射 → 中心节点向外连接
   - 层级结构 → 自上而下树形
5. **分配颜色** — 每个逻辑组/层一种强调色
6. **逐字写出标签** — 从论文正文提取确切术语

**数据图**（结果 → 图）：

1. **阅读提供的数据** — 表格、含数字段落、CSV 或 JSON
2. **识别维度**：
   - 比较什么？（方法、模型、配置）→ 分类轴
   - 指标是什么？（accuracy、loss、latency、F1）→ 数值轴
   - 是否有时间/step 维度？→ 折线图
   - 是否多指标？→ 多面板或分组柱
3. **按下列优先级自动选图型**：
   - 有 step/时间轴 → **折线图**
   - N 个方法 × M 个 benchmark → **分组柱状图**
   - 单一排序 → **横向柱状图**（排行榜）
   - 两连续变量相关 → **散点图**
   - 方阵数值 → **热力图**
   - 比例构成 → **堆叠柱**（避免饼图）
4. **确定图幅** — 按数据密度选单栏或通栏
5. **突出「我们的方法」** — 标出论文贡献项并用醒目颜色

### 自动识别示例

**上下文 → 示意图**：「系统有 Planner、Executor、Verifier。Planner 将计划发给 Executor，Executor 将结果返回 Verifier，失败时 Verifier 反馈给 Planner。」
→ 3 个实体、环形布局、虚线反馈箭头 → **工作流 1（Gemini）**

**数据 → 图表**：「GPT-4: MMLU 86.4, HumanEval 67.0。Ours: 88.1, 71.2。Llama-3: 79.3, 62.1。」
→ 3 方法 × 2 benchmark → **工作流 2（分组柱）**，用 coral 高亮「Ours」

---

## 工作流 1：架构与系统示意图（AI 图像生成）

使用 Gemini 3 Pro Image Preview 生成示意图。**先选定视觉风格** — 这是图是否专业、是否千篇一律的最大因素。

### 视觉风格

每篇论文选一种风格（全文图表一致）：

#### 风格 A：「Sketch / 简笔画」（手绘）

温暖、亲切、易记。适合总览图与系统介绍。像设计师精修过的白板草图。

```
VISUAL STYLE — HAND-DRAWN SKETCH:
- Slightly irregular, hand-drawn line quality — lines wobble gently, not perfectly straight
- Rounded, soft shapes with visible pen strokes (like drawn with a thick felt-tip marker)
- Warm off-white background (#FAFAF7), NOT pure white
- Fill colors are soft watercolor-like washes: muted blue (#D6E4F0), soft peach (#F5DEB3),
  light sage (#D4E6D4), pale lavender (#E6DFF0)
- Borders are dark charcoal (#2C2C2C) with 2-3px line weight, slightly uneven
- Arrows are hand-drawn with slight curves, ending in simple open arrowheads (not filled triangles)
- Text uses a rounded sans-serif font (like Comic Neue or Architects Daughter feel)
- Small doodle-style icons inside boxes: a tiny gear ⚙ for processing, a lightbulb 💡 for ideas,
  a magnifying glass 🔍 for search — rendered as simple line drawings, NOT emoji
- Overall feel: a carefully drawn whiteboard diagram, clean but with personality
- NO clip art, NO stock icons, NO photorealistic elements
```

#### 风格 B：「Modern Minimal」（简洁有力）

自信、权威。适合需要精确表达的方法图。

```
VISUAL STYLE — MODERN MINIMAL:
- Ultra-clean geometric shapes with crisp edges
- Bold color blocks as backgrounds for sections — NOT just accent bars, but full section fills
  using desaturated tones: slate blue (#E8EDF2), warm sand (#F5F0E8), cool mint (#E8F2EE)
- Component boxes have ROUNDED CORNERS (12px radius), NO visible border — they float on
  the section background using subtle shadow (1px, 4px blur, rgba(0,0,0,0.06))
- ONE accent color per section used sparingly on key elements: Deep blue (#2563EB),
  Emerald (#059669), Amber (#D97706), Rose (#E11D48)
- Arrows are thin (1.5px), dark gray (#6B7280), with small filled circle at source
  and clean arrowhead at target — NOT thick colored arrows
- Typography: Inter or system sans-serif, title 600 weight, body 400 weight
- Labels INSIDE boxes, not beside them
- Generous whitespace — at least 24px between elements
- NO decorative elements, NO icons — let the structure speak
```

#### 风格 C：「Illustrated Technical」（图标丰富）

生动、易读。适合教程式论文与需自解释的图。

```
VISUAL STYLE — ILLUSTRATED TECHNICAL:
- Each major component has a small MEANINGFUL ICON drawn in a consistent line-art style
  (single color, 2px stroke, ~24x24px): brain icon for reasoning, database cylinder for storage,
  arrow-loop for iteration, network nodes for communication
- Components sit inside soft rounded rectangles with a LEFT COLOR STRIP (4px wide)
- Background is pure white, but each logical group has a very faint colored region behind it
  (#F8FAFC for blue group, #FFF8F0 for orange group)
- Connections use CURVED bezier paths (not straight lines), colored by SOURCE component
- Key data flows are THICKER (3px) than secondary flows (1px, dashed)
- Small annotation badges on arrows: "×N" for repeated operations, "optional" in italics
- Title labels are ABOVE each section in small caps, letter-spaced
- Overall: like a well-designed API documentation diagram
```

#### 风格 D：「Accent Bar」（经典学术）

默认学术风格。各 venue 稳妥，灰度打印友好。

```
VISUAL STYLE — CLASSIC ACCENT BAR:
- Horizontal section bands stacked vertically, pale gray (#F7F7F5) fill
- Thick colored LEFT ACCENT BAR (8px) distinguishes each section
- Content boxes: white fill, thin #DDD border, 4px rounded corners
- Section palette: Blue #4A90D9, Teal #5BA58B, Amber #D4A252, Slate #7B8794
- Sans-serif typography (Helvetica/Arial), bold titles, regular body
- Colored arrows match their SOURCE section
- Clean, flat, zero decoration
```

### 精选色板

**「Ocean Dusk」**（专业、沉静 — 默认推荐）：
`#264653` deep teal, `#2A9D8F` teal, `#E9C46A` gold, `#F4A261` sandy orange, `#E76F51` burnt coral

**「Ink & Wash」**（简笔画风格）：
`#2C2C2C` charcoal ink, `#D6E4F0` washed blue, `#F5DEB3` washed wheat, `#D4E6D4` washed sage, `#E6DFF0` washed lavender

**「Nord」**（现代极简）：
`#2E3440` polar night, `#5E81AC` frost blue, `#A3BE8C` aurora green, `#EBCB8B` aurora yellow, `#BF616A` aurora red

**「Okabe-Ito」**（通用色盲安全，数据图必选）：
`#E69F00` orange, `#56B4E9` sky blue, `#009E73` green, `#F0E442` yellow, `#0072B2` blue, `#D55E00` vermillion, `#CC79A7` pink

### 检查清单

- [ ] **从上下文提取**：阅读论文/描述，识别实体与关系
- [ ] **选择视觉风格**（A/B/C/D）— 与论文语气、venue 一致
- [ ] **选择色板** — 或与已有论文图一致
- [ ] 获取 Gemini API key（`GEMINI_API_KEY` 环境变量）
- [ ] 撰写详细提示词：风格块 + 布局 + 连接 + 约束
- [ ] 在 `figures/gen_fig_<name>.py` 生成脚本，运行 3 次
- [ ] 审阅、选最佳，保存为 `figures/fig_<name>.png`

### 提示词结构（6 节）

每个 Gemini 提示词须按顺序包含：

```
1. FRAMING (5 lines): "Create a [STYLE_NAME]-style technical diagram for a
   [VENUE] paper. The diagram should feel [ADJECTIVES]..."

2. VISUAL STYLE (20-30 lines): Copy the full style block from above (A/B/C/D).
   This is the most important section — it determines the entire visual character.

3. COLOR PALETTE (10 lines): Exact hex codes for every color used.

4. LAYOUT (50-150 lines): Every component, box, section — exact text, spatial
   arrangement, and grouping. Be exhaustively specific.

5. CONNECTIONS (30-80 lines): Every arrow individually — source, target, style,
   label, routing direction.

6. CONSTRAINTS (10 lines): What NOT to include. Adapt per style — e.g., sketch
   style allows slight irregularity but still no clip art.
```

### 生成脚本模板

```python
#!/usr/bin/env python3
"""Generate [FIGURE_NAME] diagram using Gemini image generation."""
import os, sys, time
from google import genai

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: Set GEMINI_API_KEY environment variable.")
    print("  Get a key at: https://aistudio.google.com/apikey")
    sys.exit(1)

MODEL = "gemini-3-pro-image-preview"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
client = genai.Client(api_key=API_KEY)

PROMPT = """
[PASTE YOUR 6-SECTION PROMPT HERE]
"""

def generate_image(prompt_text, attempt_num):
    print(f"\n{'='*60}\nAttempt {attempt_num}\n{'='*60}")
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt_text,
            config=genai.types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )
        output_path = os.path.join(OUTPUT_DIR, f"fig_NAME_attempt{attempt_num}.png")
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")
                return output_path
            elif part.text:
                print(f"Text: {part.text[:300]}")
        print("WARNING: No image in response")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def main():
    results = []
    for i in range(1, 4):
        if i > 1:
            time.sleep(2)
        path = generate_image(PROMPT, i)
        if path:
            results.append(path)
    if not results:
        print("All attempts failed!")
        sys.exit(1)
    print(f"\nGenerated {len(results)} attempts. Review and pick the best.")

if __name__ == "__main__":
    main()
```

### 关键规则

- **始终 3 次尝试** — 各次质量差异大
- **风格块必填** — 否则 Gemini 易退化为通用企业风
- **切勿硬编码 API key** — 使用 `os.environ.get("GEMINI_API_KEY")`
- **保存生成脚本** — 可复现性至关重要
- **逐字指定标签** — Gemini 可能拼错或重排文字

**各风格完整提示词示例**：见 [references/diagram-generation.md](references/diagram-generation.md)

---

## 工作流 2：数据驱动图表（matplotlib/seaborn）

凡含数值数据、坐标轴或定量对比的图均用此工作流。

### 检查清单

- [ ] **从上下文提取**：解析结果/数据，识别方法、指标与对比结构
- [ ] **按数据维度自动选图型**（见下方决策指南）
- [ ] 准备数据（CSV、dict 或内联数组）
- [ ] 应用发表级样式（字体、颜色、尺寸）
- [ ] 用醒目颜色高亮「我们的方法」
- [ ] 同时导出 PDF（矢量）与 PNG（300 DPI）
- [ ] 核对与 LaTeX 字体兼容
- [ ] 脚本保存于 `figures/gen_fig_<name>.py`

### 图表类型决策指南

| 数据模式 | 最佳图表 | 说明 |
|-------------|------------|-------|
| 随时间/step 的趋势 | 折线图 | 训练曲线、scaling law |
| 类别对比 | 分组柱状图 | 模型对比、消融 |
| 分布 | 小提琴 / 箱线图 | 各方法得分分布 |
| 相关 | 散点图 | 嵌入分析、指标相关 |
| 数值网格 | 热力图 | 注意力图、混淆矩阵 |
| 部分与整体 | 堆叠柱（非饼图） | ML 论文优先堆叠柱 |
| 多方法、单指标 | 横向柱状图 | 排行榜式对比 |

### 发表级样式模板

```python
import matplotlib.pyplot as plt
import numpy as np

# --- Publication defaults (polished, not generic) ---
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10, "axes.titlesize": 11, "axes.titleweight": "bold",
    "axes.labelsize": 10, "legend.fontsize": 8.5, "legend.frameon": False,
    "figure.dpi": 300, "savefig.dpi": 300, "savefig.bbox": "tight",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.15, "grid.linestyle": "-",
    "lines.linewidth": 1.8, "lines.markersize": 5,
})

# --- "Ocean Dusk" palette (professional, distinctive, colorblind-safe) ---
COLORS = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51",
          "#0072B2", "#56B4E9", "#8C8C8C"]
OUR_COLOR = "#E76F51"       # coral — warm, stands out
BASELINE_COLOR = "#B0BEC5"  # cool gray — recedes
FIG_SINGLE, FIG_FULL = (3.25, 2.5), (6.75, 2.8)
```

### 常见图型模式

**折线图（训练曲线）** — 带标记与置信带：

```python
fig, ax = plt.subplots(figsize=FIG_SINGLE)
markers = ["o", "s", "^", "D", "v"]
for i, (method, (mean, std)) in enumerate(results.items()):
    color = OUR_COLOR if method == "Ours" else COLORS[i]
    ax.plot(steps, mean, label=method, color=color,
            marker=markers[i % 5], markevery=max(1, len(steps)//8),
            markersize=4, zorder=3)
    ax.fill_between(steps, mean - std, mean + std, color=color, alpha=0.12)
ax.set_xlabel("Training Steps")
ax.set_ylabel("Accuracy (%)")
ax.legend(loc="lower right")
fig.savefig("figures/fig_training.pdf")
fig.savefig("figures/fig_training.png", dpi=300)
```

**分组柱状图（消融）** — 带数值标签：

```python
fig, ax = plt.subplots(figsize=FIG_FULL)
x = np.arange(len(categories))
n = len(methods)
width = 0.7 / n
for i, (method, scores) in enumerate(methods.items()):
    color = OUR_COLOR if method == "Ours" else COLORS[i]
    offset = (i - n / 2 + 0.5) * width
    bars = ax.bar(x + offset, scores, width * 0.9, label=method, color=color,
                  edgecolor="white", linewidth=0.5)
    for bar, s in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f"{s:.1f}", ha="center", va="bottom", fontsize=7, color="#444")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("Score")
ax.legend(ncol=min(n, 4))
fig.savefig("figures/fig_ablation.pdf")
```

**热力图** — 发散色图与清晰边框：

```python
import seaborn as sns
fig, ax = plt.subplots(figsize=(4, 3.5))
sns.heatmap(matrix, annot=True, fmt=".2f", cmap="YlOrRd", ax=ax,
            cbar_kws={"shrink": 0.75, "aspect": 20},
            linewidths=1.5, linecolor="white",
            annot_kws={"size": 8, "weight": "medium"})
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
fig.savefig("figures/fig_confusion.pdf")
```

**横向柱状图（排行榜）** — 高亮「我们的方法」：

```python
fig, ax = plt.subplots(figsize=FIG_SINGLE)
y_pos = np.arange(len(models))
colors = [BASELINE_COLOR] * len(models)
colors[our_idx] = OUR_COLOR
bars = ax.barh(y_pos, scores, color=colors, height=0.55,
               edgecolor="white", linewidth=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(models)
ax.set_xlabel("Accuracy (%)")
ax.invert_yaxis()
for bar, s in zip(bars, scores):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            f"{s:.1f}", va="center", fontsize=8, color="#444")
fig.savefig("figures/fig_leaderboard.pdf")
```

**完整模式库**（scaling law、小提琴图、多面板、雷达图）：见 [references/data-visualization.md](references/data-visualization.md)

---

## 发表样式速查

| Venue | 单栏宽 | 通栏宽 | 字体 |
|-------|-----------|------------|------|
| NeurIPS | 5.5 in | 5.5 in | Times |
| ICML | 3.25 in | 6.75 in | Times |
| ICLR | 5.5 in | 5.5 in | Times |
| ACL | 3.3 in | 6.8 in | Times |
| AAAI | 3.3 in | 7.0 in | Times |

**始终导出 PDF** 以保证矢量质量。PNG 仅用于 AI 生成示意图。

**venue 细则、LaTeX 集成、字体匹配、无障碍检查清单**：见 [references/style-guide.md](references/style-guide.md)

---

## 常见问题

| 问题 | 解决方案 |
|-------|----------|
| LaTeX 中字体不对 | 导出 PDF，设 `text.usetex=True`，或 `font.family=serif` |
| 图超出栏宽 | 查 venue 宽度限制，用英寸 `figsize` |
| 打印时颜色难区分 | 色盲安全色板 + 不同线型/标记 |
| Gemini 标签拼错 | 提示词逐字写出标签，加「SPELL EXACTLY」约束 |
| Gemini 忽略风格 | 加强负向约束，更具体写 hex 色 |
| PDF 中图模糊 | 导出 PDF（矢量）而非 PNG；或 PNG ≥300 DPI |
| 图例遮挡数据 | 用 `bbox_to_anchor`、`loc="upper left"` 或外置图例 |
| 刻度标签过密 | 用 `ax.xaxis.set_major_locator(MaxNLocator(5))` |

## 何时用本 Skill vs 替代方案

| 需求 | 本 Skill | 替代 |
|------|-----------|-------------|
| 架构示意图 | Gemini 生成 | TikZ（手工）、draw.io（交互）、Mermaid（简单） |
| 数据图 | matplotlib/seaborn | Plotly（交互）、R/ggplot2（统计向） |
| 全文写作 | 配合 `ml-paper-writing` | — |
| 海报图 | 更大字号、更宽 | `latex-posters` skill |
| 演示图 | 更大文字、更少细节 | PowerPoint/Keynote 导出 |

---

## 速查：文件命名约定

```
figures/
├── gen_fig_<name>.py      # 生成脚本（务必保留以便复现）
├── fig_<name>.pdf         # 最终矢量输出（LaTeX）
├── fig_<name>.png         # 栅格输出（300 DPI，AI 图或备用）
└── fig_<name>_attempt*.png # Gemini 各次尝试（保留对比）
```
