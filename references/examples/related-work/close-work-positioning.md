# Related Work Example: Close Work Positioning

Use this pattern when one prior paper is close enough that reviewers may ask why the new paper is needed. The goal is precise positioning, not dismissal.

## Pattern

```text
[Close work] is particularly related because it also addresses [shared problem] using [shared idea or setting]. The key difference is [task definition / supervision / input-output / evaluation target]. Whereas [close work] focuses on [their target], our paper focuses on [our target], which requires [technical requirement] and is evaluated by [evidence]. This distinction means the methods are complementary rather than directly substitutable.
```

## Annotated Example

```text
Concurrent work on open-vocabulary segmentation is particularly related because it also uses language supervision to broaden visual recognition beyond fixed label sets. The key difference is the prediction setting: those methods primarily assign semantic regions in images, whereas our paper studies [your structured output] under [your constraint]. This requires modeling [technical requirement] and is evaluated through [your benchmark or metric], so the comparison is best framed as complementary rather than as a direct replacement.
```

## Checklist

- Name the similarity first.
- State the task difference in neutral language.
- Tie the difference to a technical requirement or evaluation target.
- Avoid "unlike prior work, which fails to..." unless the paper truly demonstrates that failure.
- Make sure the close work has a note in `literature/notes/` before drafting this paragraph.
