# 会议/期刊画像参考文档

当目标会议、模板、页数上限、匿名模式，或清单（checklist）会影响你的写作决策时使用本参考文档。
如果用户正在提交（actively submitting），请始终从官方征稿（call for papers）或官方模板中核验最新规则；因为会议规则可能会变化。

起草时，如果你需要清单、局限（limitations）、可复现性、伦理（ethics），或 camera-ready 文本，可加载 `venue-templates.md`。

## 通用会议工作流（General Venue Workflow）

1. 确定目标会议与年份。
2. 判断当前模板是否匹配目标会议。
3. 记录页数上限、匿名要求、附录政策、清单政策，以及 camera-ready 的差异。
4. 决定哪些部分必须放在主页面页数限制内。
5. 把冲突记录在 `project_inventory.md` 或 `submission_readiness.md`。

不要假设去年的规则对今年仍然适用。

## NeurIPS 风格的 ML 会议

典型期待：

- 摘要与引言中的“主张-证据对齐（claim-evidence alignment）”很强。
- 有清晰的局限部分（或局限段落）。
- 可复现性与清单问题的回答。
- 如果相关，讨论伦理与社会影响。
- 当相关时给出计算资源、数据集、代码、许可证与人类受试细节。
- 匿名投稿，除非你已经被要求在最终稿/相机就绪稿（camera-ready）阶段提供。

写作强调点：

- 及早写出精确的技术贡献。
- 对开放式任务避免使用宽泛的 “solves（解决）” 语言。
- 把核心工作流或方法概览放在 Figure 1。
- 用消融（ablation）与难度分解（difficulty breakdown）解释设计为什么重要。
- 把相关工作范围控制得更聚焦；评审更奖励清晰，而非百科式覆盖。

## ICML 风格的投稿

典型期待：

- 技术框架简洁，且有严格的经验或理论证据。
- 细致、干净的可复现性细节与附录。
- 实验存在差异时，公平基线与统计支撑非常受重视。

写作强调点：

- 把假设写清楚（explicit）。
- 避免隐藏的基准选择（benchmark choices）。
- 当主张依赖稳定性时，报告方差（variance）或重复运行的结果。

## ICLR 风格的投稿

典型期待：

- 面向 OpenReview 的讨论准备充分。
- 动机与经验洞察表达清晰。
- 强消融与定性分析（qualitative analysis）。
- 局限诚实，并包含可复现性陈述。

写作强调点：

- 让论文在公开评审中容易“为自己辩护（defend）”。
- 预判评审会在正文里就提出的问题，而不只是等你在附录里回答。
- 当失败分析能澄清方法的适用范围时，把它当成优势。

## ACL / NLP 风格的投稿

典型期待：

- 局限与伦理部分经常是必需或强烈期待。
- 数据集、标注（annotation）、人类评估与许可证细节很重要。
- 关于语言、安全（safety）、偏差（bias）、或人类偏好（human preferences）的主张需要谨慎证据支持。

写作强调点：

- 精确定义标注或评估协议（protocol）。
- 不要把结论过度泛化到未评估的语言、领域或人群。
- 把提示词、模型与解码细节放在可复现所需的位置。

## 系统类会议（Systems Venues）

相关示例包括 OSDI、SOS P、NSDI、ASPLOS 等同类系统会议。

典型期待：

- 一个真实的系统问题，并有清晰的设计约束。
- 明确的系统架构与实现细节。
- 端到端评估、组件拆解（component breakdown）与压力测试（stress tests）。
- 提供 artifact 可用性或讨论可复现性。
- 与现实可行（realistic）的基线进行强对比。

写作强调点：

- 解释为什么每个系统边界必须存在。
- 把设计目标（design goals）与实现选择（implementation choices）区分开。
- 展示鲁棒性、开销（overhead）、以及失败表现。
- 当部署/集成细节会影响主张时，把它们纳入说明。

## CAD / 机器人 / 图形相邻方向论文

当你在写 CAD、几何、机器人、或图形相邻的 ML 工作时：

- 精确定义表征（representations）：如网格、B-Rep、STEP、代码、约束、装配（assemblies）、关节（joints）、变换（transforms）、或点云（point clouds）。
- 说明任务属于哪一类：部分生成、装配构建、文本到 CAD、检索、编辑、验证，或基准创建。
- 区分“可执行的几何（executable geometry）”与“视觉外观（visual appearance）”。
- 指标要谨慎：IoU、Chamfer distance、Hausdorff distance、成功率（success rate）、编译率（compile rate）、以及功能正确性度量（functional correctness）往往衡量的不是同一件事。
- 解释哪些几何处理是确定性的（deterministic geometry processing），哪些推理来自 LLM。

## 冲突处理（Conflict Handling）

如果用户目标与本地文件存在不一致：

```text
The user asked for TARGET, but the repository currently uses TEMPLATE.
I will preserve the template files unless changing them is necessary, and I will write requirements according to TARGET.
```

仅当冲突会改变“必须写什么或必须构建什么”时才需要进一步询问。

## 会议元数据模板（Venue Metadata Template）

把下面信息记录到 `project_inventory.md`：

```text
Target venue:
Template detected:
Main tex file:
Anonymous mode:
Main paper page limit:
Appendix policy:
Checklist required:
Limitations required:
Build command:
Conflicts / unknowns:
```

