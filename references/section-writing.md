# Section Writing Reference

Use this for Method, Experiments, Related Work, Limitations, Conclusion, and whole-paper consistency. For Abstract and Introduction, load `abstract-introduction.md` instead.

## Writing Loop

For each section:

1. Write a one-sentence section thesis.
2. Assign one role to each paragraph.
3. Map strong claims to evidence before polishing.
4. Draft one message per paragraph.
5. Reverse-outline paragraph message, evidence, and risk.
6. Repair flow and terminology across sections.

## Related Work

Load `literature-review.md` and `citation-workflow.md` first. Build the paper inventory, related-work matrix, and positioning before prose.

For each line of work, state what it solves, cite verified representative papers, identify the remaining boundary, and explain how this paper relates. Group by research problem rather than chronology. Avoid citation lists, strawman comparisons, and strong claims based only on task-adjacent work.

## Method or System Design

For each component describe:

- purpose and motivating failure mode;
- concrete inputs and outputs;
- operation or algorithm;
- invariant, contract, or design advantage;
- failure behavior and limitation.

For agent systems, separate model reasoning from deterministic parsers, tools, data, and execution checks. Describe artifact flow and control flow, not only implementation filenames.

## Experiments and Evaluation

For each experiment record:

- research question;
- dataset, split, and benchmark;
- baselines and fairness assumptions;
- metrics and direction;
- seeds, uncertainty, and compute;
- main result, interpretation, and caveat.

A strong evaluation normally includes the main comparison, ablation, failure/stress analysis, qualitative cases, and cost or efficiency when relevant. Missing elements must be justified or moved into limitations.

Use `shows` only for direct evidence, `suggests` for limited evidence, and `is consistent with` for non-causal interpretations. Never hide negative or mixed metrics.

## Limitations

State scope restrictions, assumptions, failure modes, missing evaluation, reproducibility gaps, and cost constraints that a reviewer could infer. Write them as scientific boundaries rather than apologies.

## Conclusion

Restate the problem and demonstrated contribution, summarize the strongest evidence, and name the main remaining boundary. Do not introduce new results.

## Revision Output

For substantial revisions, produce:

- mini-outline with paragraph roles;
- revised manuscript text;
- reverse outline with evidence;
- claim/evidence changes;
- remaining experiments, citations, definitions, or reviewer risks.
