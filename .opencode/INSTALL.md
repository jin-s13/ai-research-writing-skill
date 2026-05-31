# Installing AI Research Writing Skill for OpenCode

OpenCode can consume this repository as a plugin or as a local project-level skill source.

## Plugin Install

Add the repository to the `plugin` array in your global or project `opencode.json`:

```json
{
  "plugin": [
    "ai-research-writing-skill@git+https://github.com/jin-s13/ai-research-writing-skill.git"
  ]
}
```

Restart OpenCode so it can install and discover the skill.

## Local Install

If you work from a local clone, point OpenCode at this repository from your project configuration according to your OpenCode version's plugin/skill path support.

## Use

```text
use skill tool to list skills
use skill tool to load ai-research-writing-skill
```

Then ask for paper story, citation verification, figure planning, LaTeX drafting, reviewer checks, or submission packaging.
