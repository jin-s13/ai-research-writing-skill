# 会议模板参考文档

当你起草面向特定会议的清单（checklist）、可复现性（reproducibility）、局限（limitations）、伦理（ethics），或相机就绪（camera-ready）文本时使用本参考文档。
对于正在进行中的投稿，请核验官方要求（官方征稿/模板）是否有更新。

## NeurIPS 风格清单骨架（NeurIPS-Style Checklist Skeleton）

创建或更新 `checklist.tex`，并用明确答案回答：

1. 主张对齐（Claims alignment）。
2. 局限（Limitations）。
3. 理论假设与证明（如适用）。
4. 可复现性（Reproducibility）。
5. 代码/数据访问（Code/data access）。
6. 实验细节（Experimental details）。
7. 统计显著性（Statistical significance）。
8. 计算资源（Compute resources）。
9. 伦理合规（Ethics compliance）。
10. 更广泛影响（Broader impacts）。
11. 安全防护（Safeguards）。
12. 已有素材的许可证（Licenses for existing assets）。
13. 新素材（如有）的许可证/信息（New assets, if any）。
14. 人类受试（如有）。
15. IRB 或等效机构（如有）。
16. 当适用时的 LLM 使用披露（LLM usage disclosure）。

回答格式：

```latex
\answerYes{See Section~\ref{sec:experiments}.}
\answerNo{We do not release ... because ...}
\answerNA{The paper does not include ...}
```

## 局限模板（Limitations Template）

```latex
\section{Limitations}
我们的评估聚焦于 ...
当前方法还假设 ...
主要的失败模式是 ...
这些局限不会影响核心主张：..., 但它为未来工作（future work）留下了 ...
```

## 可复现性模板（Reproducibility Template）

```latex
\paragraph{Reproducibility.}
我们报告 ... 实现使用 ...
所有评估设定使用 ...
我们将发布/代码在 ... 提供。
```

## 计算模板（Compute Template）

```latex
\paragraph{Compute.}
实验在 ... 上运行。每次运行大约需要 ...
总计算预算为 ...
```

## 伦理 / 更广泛影响模板（Ethics / Broader Impact Template）

```latex
\paragraph{Broader Impact.}
这项工作可能带来 ...
潜在风险包括 ...
我们通过 ... 来缓解这些风险。
```

## LLM 使用模板（LLM Usage Template）

```latex
\paragraph{LLM Usage.}
大型语言模型被用作 [core method / coding assistant / writing aid]。
在方法中，它们执行 ...
所有 LLM 生成的输出都会经过 ... 检查。
```

仅在会议与论文确实适用时使用。

## 相机就绪模板（Camera-Ready Template）

在最终提交之前：

- 把匿名作者替换为最终作者与单位（affiliations）。
- 如果允许，加入致谢与资助信息（funding）。
- 更新代码/数据 URL。
- 核验许可证声明。
- 核验清单答案与最终内容仍然一致。
- 核验附录中的引用与补充材料（supplementary material）。

