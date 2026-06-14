# Core Methodology: Concept Album Continuity

## Purpose

Define the platform-neutral continuity process for concept albums: keep each song strong as a track while preserving album story, motifs, character voices, sonic palette, and hard rules.

## Canonical sources

- `.kiro/sops/04-setting-up-concept-album.md`
- `.kiro/sops/05-extending-an-album.md`
- `.kiro/agents/album-continuity.md`
- `.kiro/steering/concept-album.md`
- `.kiro/skills/concept-album-bible/SKILL.md`
- `references/YOUR_ALBUM_BIBLE.md`
- `references/FRACTURED_SHADOWS_BIBLE.md`
- `references/KEEPER_OF_THE_LIGHT_BIBLE.md`
- `examples/README.md`

## Core workflow

1. Create an album bible before writing or extending an album.
2. Define track registry, emotional arc, hard rules, motifs, callbacks, character voices, sonic palette, and key relationships.
3. For each new track, verify position, intention, sonic differentiation, motif usage, callback accuracy, and character voice.
4. Record continuity reports or exceptions under `analysis/`.
5. Treat hard-rule failures as revision triggers unless the album bible records an intentional exception.

## Testing/validation

- Album bibles should eventually be backed by machine-readable schemas.
- Continuity checks should distinguish fatal violations, warnings, informational notes, and intentional exceptions.
- Hooks and manual reviews should reference the same album source of truth.
