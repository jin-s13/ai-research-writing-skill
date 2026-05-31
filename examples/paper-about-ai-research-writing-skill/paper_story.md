# Paper Story

## Working Title

AI Research Writing Skill: Claim-Evidence Engineering for Agentic Research Paper Generation

## Thesis

AI Research Writing Skill turns research paper writing from prose generation into a claim-evidence-engineering workflow for agents working inside ML/AI repositories.

## Research Gap

General research-writing skills provide useful writing guidance, and figure-specific tools provide high-quality visualization recipes. However, agentic paper generation for ML/AI repositories needs a narrower operational contract: claims must be tied to local code/results or verified citations, figures and tables must become concrete assets, and submission readiness must be checked rather than assumed.

## Contributions

1. A skill-level workflow that coordinates story, evidence, literature, figures, citations, review, and submission gates.
2. A durable artifact contract for auditable outputs such as `paper_story.md`, `claim_evidence_map.md`, `citation_verification.md`, and `build_check.md`.
3. A portable single-entrypoint design: the root `SKILL.md` is the canonical contract, while agents install or load it using their own platform conventions.
4. A repository-backed template and script collection for major ML/AI venues and deterministic quality checks.

## Claims to Avoid

- The skill guarantees paper acceptance.
- The skill replaces human scientific judgment.
- The skill verifies every possible citation or venue rule without external access.
- The skill has been empirically benchmarked against other writing systems.
