# Venue Templates Reference

Use this when drafting venue-specific checklist, reproducibility, limitations, ethics, or camera-ready text. Verify current official requirements for active submissions.

## NeurIPS-Style Checklist Skeleton

Create or update `checklist.tex` with explicit answers for:

1. Claims alignment.
2. Limitations.
3. Theory assumptions and proofs, if applicable.
4. Reproducibility.
5. Code/data access.
6. Experimental details.
7. Statistical significance.
8. Compute resources.
9. Ethics compliance.
10. Broader impacts.
11. Safeguards.
12. Licenses for existing assets.
13. New assets, if any.
14. Human subjects, if any.
15. IRB or equivalent, if any.
16. LLM usage disclosure when applicable.

Answer format:

```latex
\answerYes{See Section~\ref{sec:experiments}.}
\answerNo{We do not release ... because ...}
\answerNA{The paper does not include ...}
```

## Limitations Template

```latex
\section{Limitations}
Our evaluation focuses on ...
The method currently assumes ...
The main failure modes are ...
These limitations do not affect the central claim that ..., but they leave ... for future work.
```

## Reproducibility Template

```latex
\paragraph{Reproducibility.}
We report ... The implementation uses ...
All evaluated settings use ...
We will release/code is available at ...
```

## Compute Template

```latex
\paragraph{Compute.}
Experiments were run on ... Each run required approximately ...
The total compute budget was ...
```

## Ethics / Broader Impact Template

```latex
\paragraph{Broader Impact.}
This work may benefit ...
Potential risks include ...
We mitigate these risks by ...
```

## LLM Usage Template

```latex
\paragraph{LLM Usage.}
Large language models are used as [core method / coding assistant / writing aid].
In the method, they perform ...
All LLM-generated outputs are checked by ...
```

Use only if applicable to the venue and paper.

## Camera-Ready Template

Before final submission:

- Replace anonymous authors with final authors and affiliations.
- Add acknowledgments and funding if allowed.
- Update code/data URLs.
- Verify license statements.
- Verify checklist answers still match final content.
- Verify appendix references and supplementary material.
