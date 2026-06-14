# Core Methodology: Critique Rubric

## Purpose

Define the platform-neutral critique process used to evaluate songs consistently, identify high-impact revisions, and decide whether a song should be revised, optimized, or rethought.

## Canonical sources

- `.kiro/sops/02-critiquing-a-song.md`
- `.kiro/agents/critic.md`
- `.kiro/skills/song-critique/SKILL.md`
- `references/CRITIQUE_REFERENCE.md`
- `references/CRITIQUE_REPORT_TEMPLATE.md`
- `analysis/README.md`

## Core workflow

1. Read the full song without scoring.
2. Run the same analysis lenses used in songwriting: semantic, emotional, prosodic, narrative, voice, genre, arrangement, production, and commercial.
3. Score the core 12 categories using the critique reference.
4. Add advanced assessments only when the task needs deeper production, semiotic, or album-context review.
5. Identify the strongest line, the highest-impact issues, and concrete fixes.
6. Apply the pipeline decision gate: high scores can proceed to optimization, mid scores should revise, and low scores should rethink concept or structure.
7. Save critique reports under `analysis/` using the report naming conventions.

## Testing/validation

- Every critique report should identify the analyzed version, score basis, strongest line, major issues, and next action.
- Score anchors should be added before treating composite scores as research-grade measurements.
- Self-score vs independent-score deltas should be tracked when both are available.
