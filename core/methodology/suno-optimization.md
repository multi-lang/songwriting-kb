# Core Methodology: Suno Optimization

## Purpose

Define the platform-neutral process for preparing finished songs for Suno rendering while separating stable songcraft from model-version-sensitive prompt behavior.

## Canonical sources

- `.kiro/sops/03-optimizing-for-suno.md`
- `.kiro/agents/suno-optimizer.md`
- `.kiro/steering/suno-formatting.md`
- `.kiro/skills/suno-meta-tags/SKILL.md`
- `references/SUNO_TAGS_REFERENCE.md`
- `references/SUNO_STYLE_GENRE_REFERENCE.md`
- `SONGWRITING_KNOWLEDGE_BASE.md`

## Core workflow

1. Confirm the song is finished enough for formatting; do not use optimization to hide unresolved craft problems.
2. Separate Style Prompt, Lyrics, Exclusions, and Production Notes.
3. Check Style Prompt and Lyrics character counts against current repo limits.
4. Verify section tags, vocal/dynamic tags, and exclusions are placed in the correct fields.
5. Keep model-version-sensitive claims traceable through claims and experiment logs.
6. Record optimization changes and render observations when results affect universal guidance.

## Testing/validation

- Run `tools/count-suno-fields.py` on Suno-ready songs for deterministic field validation.
- Claims about tags, model behavior, and UI features should include model version, date, and confidence.
- Render tests should be recorded in `experiments/suno/` before promoting new universal guidance.
