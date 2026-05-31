# 开源增长与发布清单

这个项目的技术内容已经比较扎实，增长瓶颈主要是陌生人无法在 10 秒内判断“我为什么要 star”。下面是一套轻量发布方案。

## GitHub 仓库设置

建议添加 topics：

```text
ai-writing
research-paper
academic-writing
latex
machine-learning
computer-vision
nlp
codex-skill
claude-code
cursor
gemini-cli
opencode
```

仓库描述建议：

```text
Turn ML/AI research repos into evidence-backed, build-ready conference paper drafts.
```

## 首发内容

### 中文标题

```text
我做了一个能把 AI 研究仓库整理成论文草稿的 Agent Skill
```

### 英文标题

```text
I built an agent skill that turns ML research repos into evidence-backed paper drafts
```

## 推荐发布渠道

- GitHub README + pinned repo。
- 知乎文章：展示 before/after 和 demo repo。
- X / Twitter：30 秒流程图 + demo prompt。
- Reddit：`r/MachineLearning`, `r/LaTeX`, `r/PhD`，语气要像分享 workflow，不要像广告。
- Hugging Face / Papers with Code 社区讨论区，如果后续有 demo video。

## 发布帖模板

```text
I often found AI paper-writing tools too eager to write fluent prose from memory.

So I built AI Research Writing Skill: an agent workflow for turning ML/AI repos into auditable paper artifacts:

- paper_story.md
- claim_evidence_map.md
- verified BibTeX
- figure plans and assets
- LaTeX build/submission checks

It supports Claude Code, Cursor, Codex, Gemini CLI, and OpenCode.

Demo repo included:
https://github.com/jin-s13/ai-research-writing-skill/tree/main/examples/minimal-paper-repo
```

## 下一步最有用的素材

- 60 秒 GIF：从 demo repo 到 `paper_story.md` / `claim_evidence_map.md`。
- 一张 PDF 编译结果截图。
- 一张 Figure 1 生成前后对比图。
- 一个真实但脱敏的 paper package 示例。
