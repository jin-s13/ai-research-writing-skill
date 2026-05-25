# Venue Profiles Reference

Use this reference when the target venue, template, page limit, anonymity mode, or checklist affects writing decisions. Always verify current venue rules from the official call for papers or template when the user is actively submitting; venue rules can change.

Load `venue-templates.md` when drafting checklist, limitations, reproducibility, ethics, LLM usage, or camera-ready text.

## General Venue Workflow

1. Identify the target venue and year.
2. Identify whether the current template matches the target.
3. Record page limits, anonymity requirements, appendix policy, checklist policy, and camera-ready differences.
4. Decide which sections must be inside the main page limit.
5. Record conflicts in `project_inventory.md` or `submission_readiness.md`.

Do not assume that last year's rules still apply for an active submission.

## NeurIPS-Style ML Venues

Typical expectations:

- Strong claim-evidence alignment in Abstract and Introduction.
- Clear limitations section or limitations paragraph.
- Reproducibility and checklist answers.
- Ethical and societal impact discussion when relevant.
- Compute, dataset, code, license, and human-subject details when relevant.
- Anonymous submission unless final/camera-ready is requested.

Writing emphasis:

- State a precise technical contribution early.
- Avoid broad "solves" language for open-ended tasks.
- Put the central workflow or method overview in Figure 1.
- Use ablations and difficulty breakdowns to show why the design matters.
- Keep related work scoped; reviewers reward clarity over encyclopedic coverage.

## ICML-Style Submissions

Typical expectations:

- Concise technical framing and rigorous empirical or theoretical evidence.
- Careful reproducibility details and clean appendices.
- Strong emphasis on fair baselines and statistical support when experiments vary.

Writing emphasis:

- Make assumptions explicit.
- Avoid hidden benchmark choices.
- Report variance or repeated runs when claims depend on stability.

## ICLR-Style Submissions

Typical expectations:

- OpenReview discussion readiness.
- Clear motivation and empirical insight.
- Strong ablations and qualitative analysis.
- Honest limitations and reproducibility statements.

Writing emphasis:

- Make the paper easy to defend in public review.
- Anticipate reviewer questions in the main text, not only the appendix.
- Treat failure analysis as a strength when it clarifies the method's scope.

## ACL / NLP-Style Submissions

Typical expectations:

- Limitations and ethics sections are often required or strongly expected.
- Dataset, annotation, human evaluation, and license details matter.
- Claims about language, safety, bias, or human preferences need careful evidence.

Writing emphasis:

- Define annotation or evaluation protocols precisely.
- Avoid overgeneralizing beyond evaluated languages, domains, or populations.
- Put prompt, model, and decoding details where reproducibility requires them.

## Systems Venues

Relevant examples include OSDI, SOSP, NSDI, ASPLOS, and related systems conferences.

Typical expectations:

- A real system problem with clear design constraints.
- Explicit system architecture and implementation details.
- End-to-end evaluation, component breakdown, and stress tests.
- Artifact availability or reproducibility discussion.
- Strong comparison to realistic baselines.

Writing emphasis:

- Explain why each system boundary exists.
- Separate design goals from implementation choices.
- Show robustness, overhead, and failure behavior.
- Include deployment or integration details when they affect the claim.

## CAD / Robotics / Graphics-Adjacent Papers

When writing for CAD, geometry, robotics, or graphics-adjacent ML work:

- Define representations precisely: meshes, B-Rep, STEP, code, constraints, assemblies, joints, transforms, or point clouds.
- State whether the task is part generation, assembly construction, text-to-CAD, retrieval, editing, verification, or benchmark creation.
- Distinguish executable geometry from visual appearance.
- Use metrics carefully: IoU, Chamfer distance, Hausdorff distance, success rate, compile rate, and functional correctness measure different things.
- Explain what is deterministic geometry processing and what is LLM reasoning.

## Conflict Handling

If the user's target and local files disagree:

```text
The user asked for TARGET, but the repository currently uses TEMPLATE.
I will preserve the template files unless changing them is necessary, and I will write requirements according to TARGET.
```

Ask only when the conflict changes what must be written or built.

## Venue Metadata Template

Record this in `project_inventory.md`:

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
