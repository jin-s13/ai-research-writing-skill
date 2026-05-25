# Paper Story Workflow

Use this reference when starting a paper from a repo, notes, or experiments.

## Required Story Artifacts

Create `paper_story.md` with these sections:

1. **Working title**: concise, non-generic, no overclaiming.
2. **One-sentence thesis**: the whole paper in one sentence.
3. **Problem gap**: what prior work cannot cover and why.
4. **Technical challenge**: 2-4 concrete reasons the gap is hard.
5. **Method insight**: the central design principle, not a list of modules.
6. **Method summary**: pipeline stages and why each exists.
7. **Contributions**: 3-5 bullets, each "contribution + advantage".
8. **Experimental evidence**: datasets, metrics, baselines, headline numbers.
9. **Claims to make**: strongly supported claims.
10. **Claims to be careful about**: mixed or partial results.
11. **Claims to avoid**: unsupported or misleading claims.
12. **Reviewer risks**: likely objections and missing evidence.

Create `project_inventory.md` when starting from a repo:

1. **Repository map**: important files and directories.
2. **Method evidence**: code modules implementing the method.
3. **Experiment evidence**: result files, notes, logs, scripts, tables.
4. **Writing assets**: templates, prior drafts, figures, slides, notes.
5. **Citation assets**: existing `.bib`, paper lists, downloaded PDFs.
6. **Missing inputs**: data splits, model versions, compute, licenses, seeds, ablations.

Create `experiment_inventory.md` when experiments exist:

1. **Benchmark / dataset**.
2. **Task setting**.
3. **Baselines**.
4. **Metrics and direction**.
5. **Main numbers**.
6. **Variance / seeds / repeats**.
7. **Caveats and metric limitations**.
8. **Paper claim supported**.

## Narrative Rules

- A paper is not a collection of experiments; it is a technical story with a clear claim and evidence.
- The reader should understand the **what**, **why**, and **so what** by the end of the Introduction.
- Do not frame a workflow contribution as a "unified model" unless it truly is a single model.
- Do not describe a method as SOTA unless the comparison is fair, complete, and supported on the main metrics.
- Prefer "we study/introduce a workflow/benchmark" when the novelty is task or evaluation scope.
- Prefer "supports", "enables", "bridges", or "connects" over "solves" for broad open-ended problems.
- State limitations early enough that reviewers do not discover them first.
- Avoid a "naive method then our patch" story unless the paper is genuinely about one small fix. Instead, motivate from a technical gap that prior methods naturally leave open.
- For concurrent work, state relationship and task difference without turning it into the central opponent unless the paper's experiments directly compare to it.

## Repo Mining Checklist

When starting from a research repository, inspect:

- README, docs, project notes, progress logs, and slides.
- Experiment scripts, result tables, logs, notebooks, and output directories.
- Evaluation code and metric definitions.
- Figure scripts and generated figures.
- Prompt files, agent tools, configuration files, and deterministic post-processing.
- Existing `.bib` files, paper lists, downloaded PDFs, and related-work notes.
- Issue trackers, TODO notes, or comments that reveal known limitations.

Record what is evidence and what is only intention. Do not turn roadmap items into completed contributions.

## Thesis Test

The one-sentence thesis should answer:

```text
We introduce [artifact/idea] for [task] that enables [capability] by [technical insight], and we show [evidence].
```

If this sentence becomes a list of modules, the story is not yet sharp enough. Compress modules into a method insight, then expand details later.

## Contribution Test

Each contribution should answer:

- What is new?
- Why is it nontrivial?
- What technical advantage does it provide?
- What evidence supports it?

Reject or rewrite contributions that are only implementation details without a paper-level advantage.

## Naming Test

For method or artifact names:

- Avoid generic names that already describe a broad category.
- Avoid names that imply a single unified model when the contribution is an agent workflow or tool.
- Prefer names connected to the task, mechanism, representation, or metaphor.
- Check likely collisions in related work before finalizing a name for a paper.

## Story Patterns

### Pattern A: Gap Between Two Research Lines

Use when the paper bridges two areas.

```text
Line A solves ...
Line B solves ...
However, neither supports ...
We introduce ...
```

Good for papers connecting generation and verification, learning and tool use, or single-object and compositional settings.

### Pattern B: Executable Workflow

Use when the paper is a pipeline or agent workflow.

```text
Existing methods can produce X, but practical use requires Y.
Y is hard because semantic decisions and exact execution have different failure modes.
We separate semantic reasoning from deterministic execution.
```

Emphasize interfaces, artifacts, verification, and failure recovery.

### Pattern C: Benchmark / Evaluation

Use when the paper's main contribution is evaluation.

```text
Prior evaluations measure ...
They miss ...
We introduce a benchmark/protocol that tests ...
The benchmark reveals ...
```

Avoid claiming a method contribution if the central contribution is measurement.

### Pattern D: Method Insight

Use when one observation drives the method.

```text
We observe that ...
This suggests ...
We operationalize this insight by ...
```

The observation must be easy to understand and supported by experiments or analysis.

## Claim Strength Levels

- **Strong claim**: directly supported by experiments or formal analysis. Safe for Abstract/Introduction.
- **Careful claim**: partially supported, mixed, or dependent on assumptions. Use qualified language.
- **Aspirational claim**: motivation or future direction. Keep out of results-heavy prose.
- **Forbidden claim**: contradicted by evidence or unsupported by current experiments.

Use this scale in `paper_story.md` and `claim_evidence_map.md`.

## Story Deliverable Template

Use this compact template when creating `paper_story.md`:

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
