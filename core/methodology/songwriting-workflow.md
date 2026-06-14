# Core Methodology: Songwriting Workflow

## Purpose

Define the platform-neutral songwriting process used by this repository: analyze the song before drafting, write toward a clear chorus/hook destination, validate craft quality, and document production intent.

## Canonical sources

- `.kiro/sops/01-writing-a-song.md`
- `.kiro/agents/songwriter.md`
- `.kiro/steering/songwriting.md`
- `SONGWRITING_KNOWLEDGE_BASE.md`
- `MUSIC_PRODUCTION_THEORY.md`

## Core workflow

1. State the song thesis in one sentence.
2. Complete semantic, emotional, prosodic, narrative, voice, genre, arrangement, production, and commercial analysis.
3. Draft the chorus first so verses and bridge serve a known emotional destination.
4. Draft pre-chorus, verse 1, verse 2, bridge, final chorus variation, intro, and outro.
5. Run craft gates: hook timing, V2 new information, bridge turn, prosody, singability, and no filler.
6. Assemble style prompt, lyrics, exclusions, and production notes.
7. Save the song under `songs/` and record critique/optimization outputs under `analysis/`.

## Testing/validation

- Every song should contain a thesis or equivalent concept note before finalization.
- Lyric lines should be checked for prosody and weak endings.
- Song files should contain style, lyrics, and production notes sections before final render.
- Songs intended for Suno should be checked with `tools/count-suno-fields.py` for deterministic field validation.
