# 论文故事工作流

当你需要从代码仓库、笔记或实验结果开始撰写论文时，可使用本参考文档。

## 需要产出的“故事”工件

创建 `paper_story.md`，并包含以下部分：

1. **工作标题（Working title）**：简洁、避免泛泛措辞，不要过度承诺。
2. **一句话主张（One-sentence thesis）**：用一句话概括整篇论文。
3. **问题/缺口（Problem gap）**：说明已有工作无法覆盖什么，以及为什么。
4. **技术挑战（Technical challenge）**：用 2-4 条具体理由解释该缺口“为什么难”。
5. **方法洞察（Method insight）**：写核心设计原则，不要列模块清单。
6. **方法总结（Method summary）**：用“流水线阶段 + 为什么需要每一步”来概括。
7. **贡献（Contributions）**：3-5 条，每条格式为“贡献 + 优势”。
8. **实验证据（Experimental evidence）**：数据集、指标、基线，以及最关键的结果数字。
9. **要做出的主张（Claims to make）**：有强证据支撑的主张。
10. **需要谨慎对待的主张（Claims to be careful about）**：结果混合或不完整的主张。
11. **要避免的主张（Claims to avoid）**：无证据或会误导的主张。
12. **审稿风险（Reviewer risks）**：可能的反对点与缺失证据。

如果你是从仓库开始（repo mining），还需要创建 `project_inventory.md`：

1. **仓库地图（Repository map）**：重要文件与目录结构。
2. **方法证据（Method evidence）**：实现方法的代码模块。
3. **实验证据（Experiment evidence）**：结果文件、笔记、日志、脚本、表格。
4. **写作素材（Writing assets）**：模板、已有草稿、图表、幻灯片、笔记。
5. **引用素材（Citation assets）**：现有 `.bib`、论文列表、下载的 PDF。
6. **缺失输入（Missing inputs）**：数据划分、模型版本、算力、许可证、随机种子（seeds）、消融（ablations）。

如果你已经有实验（experiments exist），创建 `experiment_inventory.md`：

1. **基准/数据集（Benchmark / dataset）**。
2. **任务设定（Task setting）**。
3. **基线（Baselines）**。
4. **指标与方向（Metrics and direction）**。
5. **主要数字（Main numbers）**。
6. **方差/种子/重复（Variance / seeds / repeats）**。
7. **注意事项与指标局限（Caveats and metric limitations）**。
8. **论文主张与证据匹配（Paper claim supported）**。

## 叙事规则（Narrative Rules）

- 论文不是一组实验的集合；它是一则技术故事：有清晰的主张（claim）与可验证的证据（evidence）。
- 在引言（Introduction）结束时，读者应该理解：**是什么（what）**、**为什么（why）**、以及**所以呢（so what）**。
- 如果你把系统/工作流贡献写成“统一模型（unified model）”，除非它确实是单一模型，否则不要这么表述。
- 除非对比公平、覆盖完整、且关键指标有支撑，否则不要描述方法为 SOTA。
- 当新颖点来自任务范围或系统范围时，优先用“我们研究/提出一个工作流/系统/基准（we study/introduce a workflow/system/benchmark）”的表达。
- 对于开放式问题，更偏好“supports/enables/bridges/connects”，而不是“solves”。
- 局限性需要在足够早的时候写出来，让审稿人不要第一时间才在最后才发现。
- 如果不是论文的核心就是一个很小修补点，就避免“朴素方法 → 我们的补丁”的故事。应当从先前方法自然留下的技术缺口来引出动机。
- 若是并行工作（concurrent work），要说明关联与任务差异，但不要把它当成叙事中的主要对手，除非你的实验确实与之直接对比。

## 仓库挖掘清单（Repo Mining Checklist）

当你从研究仓库开始时，检查：

- README、docs、项目笔记、进度日志与幻灯片。
- 实验脚本、结果表格、日志、notebook，以及输出目录。
- 评估代码与指标定义。
- 图表脚本与生成出的图。
- prompt 文件、智能体工具（agent tools）、配置文件，以及确定性后处理（deterministic post-processing）。
- 现有 `.bib`、论文列表、下载的 PDF，以及相关工作（related-work）笔记。
- issue 跟踪器、TODO 笔记，或注释中透露的已知局限。

把“哪些是证据（evidence）”与“哪些只是意图（intention）”记录清楚。不要把路线图（roadmap）条目当成已完成的贡献。

## 论文主张测试（Thesis Test）

一句话主张应该回答：

```text
We introduce [artifact/idea] for [task] that enables [capability] by [technical insight], and we show [evidence].
```

如果这句话变成了“模块清单”，说明故事还不够尖锐。先把模块压缩成一个方法洞察（method insight），再在后面展开细节。

## 贡献测试（Contribution Test）

每条贡献都应该回答：

- 有什么是新的？
- 为什么它不是轻而易举的？
- 它提供了什么技术优势？
- 有哪些证据支撑？

如果某条贡献只是实现细节，而没有论文层面的优势，就拒绝或重写。

## 命名测试（Naming Test）

针对方法或系统名称：

- 避免那些已经在语义上描述了广泛类别的泛用名称。
- 如果你的贡献是智能体工作流或系统，而不是单个统一模型，避免让名字暗示它是单一统一模型。
- 优先使用与任务、机制、表征（representation）或隐喻相关的名字。
- 在最终命名前，检查相关工作中是否存在同名或容易混淆的表述。

## 故事模式（Story Patterns）

### 模式 A：两条研究线之间的缺口

当你的论文连接了两个方向时使用。

```text
Line A solves ...
Line B solves ...
However, neither supports ...
We introduce ...
```

适用于：连接生成与验证、学习与系统、或单对象与组合式设定的论文。

### 模式 B：可执行的工作流/系统（Executable Workflow / System）

当论文本质是一个流水线或智能体系统时使用。

```text
Existing methods can produce X, but practical use requires Y.
Y is hard because semantic decisions and exact execution have different failure modes.
We separate semantic reasoning from deterministic execution.
```

强调：接口（interfaces）、工件（artifacts）、验证（verification）、以及失败恢复（failure recovery）。

### 模式 C：基准/评估（Benchmark / Evaluation）

当论文主要贡献是评估时使用。

```text
Prior evaluations measure ...
They miss ...
We introduce a benchmark/protocol that tests ...
The benchmark reveals ...
```

如果中心贡献是“测量/评估”，就不要把它包装成“方法贡献”。

### 模式 D：方法洞察（Method Insight）

当一个关键观察驱动了方法时使用。

```text
We observe that ...
This suggests ...
We operationalize this insight by ...
```

该观察必须容易理解，并且由实验或分析支撑。

## 主张强度等级（Claim Strength Levels）

- **强主张（Strong claim）**：由实验或形式化分析直接支撑。可安全用于 Abstract/Introduction。
- **谨慎主张（Careful claim）**：部分支撑、混合结果，或依赖假设。需要限定措辞（qualified language）。
- **期望性主张（Aspirational claim）**：动机或未来方向。避免出现在大量结果的段落里。
- **禁止主张（Forbidden claim）**：被证据反驳，或目前实验无法支撑。

在 `paper_story.md` 与 `claim_evidence_map.md` 中使用该尺度。

## 故事交付物模板（Story Deliverable Template）

创建 `paper_story.md` 时可使用该紧凑模板：

```text
# Paper Story

## Thesis

## Task Boundary
- Inputs:
- Outputs:
- Supported settings:
- Out-of-scope settings:

## Gap

## Technical Challenge

## Method Insight

## System / Method Stages

## Contributions

## Evidence

## Related Work Positioning

## Claims to Make

## Claims to Be Careful About

## Claims to Avoid

## Reviewer Risks
```

