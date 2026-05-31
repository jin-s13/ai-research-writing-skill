@echo off
setlocal

REM SessionStart hook for AI Research Writing Skill on Windows.
REM Usage: run-hook.cmd session-start

if "%1"=="session-start" (
  echo {"additional_context": "AI Research Writing Skill is available. For ML/AI/CV/NLP paper writing, revision, citation verification, figures, LaTeX drafts, reviewer checks, and submission packaging, follow the root SKILL.md and load narrow references as needed."}
) else (
  echo {"error": "Unknown hook: %1"}
)

endlocal
