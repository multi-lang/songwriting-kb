# Suno AI Formatting Rules

> Auto-loaded. Quick-reference for Suno formatting. Full tag details in the suno-meta-tags skill.

---

## Field Limits

| Field | Limit | Overflow To |
|---|---|---|
| Style of Music | 1000 chars | Advanced box |
| Lyrics | 5000 chars | Advanced box |

## Style Prompt Formula

```
Genre, BPM, Mood, Instruments, Vocal Style, Production Direction
```

## Essential Tags (Use in every song)

```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, ...]
```

Place at top of Lyrics field. Add `[end]` at bottom.

## Section Rules

- Tags on their OWN line — never same line as lyrics
- 4-8 lines per section maximum
- NO punctuation at end of lines
- Each line = one melodic phrase = one breath
- Target 7-12 syllables per line

## Pipe Notation (saves chars)

```
[chorus | powerful, wide, choir swell]
[verse | vulnerable vocals, close-mic, sparse]
```

## Duet Modes

- **Mode A:** `[Male Vocal]`/`[Female Vocal]` per line (complex)
- **Mode B:** Main + `()` response, declared in Style (efficient)
- **Mode C:** Custom layers + stacked tags (theatrical)

## Exclusions Format

```
[Exclusions: ‑trap drums, ‑beatboxing, ‑vocal hums, ‑bright synths]
```

## Output Template (Every Song)

Always include: Style Prompt + Exclusions + Title tag + Production Direction + Vocal Direction + Lyrics with section tags + Production Notes block (Key, Tempo, Time Sig, Chords Nashville+actual, Vocal, Instruments, Dynamics, Hook Type, Rhyme Scheme, Emotional Arc)
