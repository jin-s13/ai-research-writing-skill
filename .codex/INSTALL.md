# Installing AI Research Writing Skill for Codex

Use Codex's native skill discovery by symlinking this repository into the Codex skills directory.

## macOS / Linux

```bash
git clone https://github.com/jin-s13/ai-research-writing-skill.git ~/.codex/skills/ai-research-writing-skill
```

If you already cloned the repository elsewhere:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/ai-research-writing-skill ~/.codex/skills/ai-research-writing-skill
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills"
cmd /c mklink /J "$env:USERPROFILE\.codex\skills\ai-research-writing-skill" "C:\path\to\ai-research-writing-skill"
```

Restart Codex after installation.

## Verify

Ask Codex:

```text
Use AI Research Writing Skill to inspect this repo and create a paper story.
```

The skill should load the root `SKILL.md`, then selectively load files from `references/`.
