# Fractured Shadows — Album Continuity Rules

> Auto-loaded. Enforces continuity when working on album material.
> Full bible: references/FRACTURED_SHADOWS_BIBLE.md
> System: Suno v5.5 (Personas, Stems, Era Tags, Parenthetical Layers)

---

## Active Album

**Fractured Shadows** — 17 tracks (Act 1: T1-7, Act 2: T8-17)

## ALBUM EXTENSION PROTOCOL

**⚠️ STOP — Before writing ANY track outside the current registry (T1-17):**
1. Update `references/FRACTURED_SHADOWS_BIBLE.md` with new track registry (including Persona assignment)
2. Extend the sonic palette evolution map
3. Define which existing rules carry forward vs which are act-specific
4. Get the bible update committed BEFORE writing new songs
5. Use SOP 05 — supports sequels (T18+), prequels (P01+), and insertions (T3a+)

Failure to do this creates cascading continuity errors that compound with each new track.

---

## 12 Hard Rules (Never Break)

1. **No electronic/industrial after Track 8 (First Blood)** — digital world is gone. Synth stems must read ZERO from T9+.
2. **Alaric's voice = same production in T11 (The Custodian) and T15 (The Sword Remembers)** — same `(spoken, deep)` delivery cue, same reverb. Recognizable.
3. **Obsidian shard pulse appears T7-T10** — then absorbed into score. Gone after T10.
4. **"I won't let the line die here" in T11 AND T15** — the thread connecting mentor to grief.
5. **First natural sound (birdsong) = T12 outro** — life after war.
6. **First major key = T16 (Campfire) — D major** — earned after 15 minor tracks. D major is RESERVED.
7. **Key change in T17 = the ONLY key change** — Am→C major. Maximum impact.
8. **Rikan's vocal texture evolves EVERY track** — never the same twice. Enforce via per-track Style Prompt vocal descriptors.
9. **T12 Fm (Fall of Dawnwatch) rhymes with T6 Fm (Fracture Protocol)** — war and transfer are related trauma.
10. **Album title phrase ONLY in T17 final chorus** — "The fracture made the shadows / But the shadows made the dawn." Nowhere else.
11. **No two adjacent tracks may share >70% instrument palette** — sonic differentiation mandatory.
12. **`(robotic layer:)` notation ONLY in T4-5** — AI voice is confined to Act 1. Scan Act 2 for any robotic/digital voice leakage.

## Sonic Palette by Track Range

| Tracks | Allowed Palette | Era Tag |
|---|---|---|
| 1-5 | Industrial, electronic, cold synths, glitch | NO decade tags — "modern cinematic, cold digital, clinical" |
| 6-7 | Chaos → cave ambient (transition) | None |
| 8 | Tribal, primal (PIVOT — organic begins) | "Prehistoric organic, primal" — NOT "1990s tribal" |
| 9-11 | Cinematic orchestral + acoustic folk | None |
| 12 | Maximum war rock, orchestral metal | None |
| 13-14 | Cold psychological, spare | None |
| 15 | Orchestral grief ballad | None |
| 16 | Warm indie folk (D major) | Optional: "2010s indie folk warmth" |
| 17 | Folk rock → full orchestra + choir (Am→C major) | None |

**Era Tag Rule:** Avoid decade tags for most tracks — this album spans digital→fantasy, not real-world eras. Exception: T16 can use "2010s indie folk warmth" for that specific Bon-Iver/Mumford analog texture.

## v5.5 Production

### Persona: Rikan/Draeven (Single Voice, Delivery Variants)

All tracks use the SAME vocal Persona (male baritone, A2-E4). Delivery controlled per track via Style Prompt:
- T1-3: `hollow clinical detached, close-mic, slight digital processing, dissociative`
- T4-5: `fracturing at edges, breath catching, clinical with instability`
- T6: `breaking screaming, panicked, raw, vocal fry, losing control`
- T7: `terrified whisper, small, raw, cave acoustics, unprocessed`
- T8: `guttural primal, projected, aggressive, low register emphasis`
- T9-10: `storytelling, road-worn, conversational, warm creeping in`
- T11: `reverent overwhelmed, quiet power, restrained awe`
- T12: `maximum projection, desperate, war-cry, strained at limits`
- T13: `cold controlled fury, precise articulation, seething`
- T14: `ashamed breaking, quiet, intimate, self-confronting`
- T15: `grieving restrained, held together barely, careful`
- T16: `warm relaxed, intimate, campfire storytelling, safe`
- T17: `steady confident, full range, building to powerful, integrated`

### Stems: Post-Render Checks

After extracting stems, verify:
- **Synth stem:** Content in T1-7 ONLY. Must be ZERO from T8+ (Rule 1).
- **Guitar stem:** Absent T1-7 (electronic world). Acoustic from T8+, electric from T12.
- **Backing Vocals stem:** No backing in T1-7 (solo voice). Choir only in T17 final chorus.
- **The Pivot (T7→T8):** T7 effects stem fades to silence. T8 has ZERO synth/electronic content. First T8 sound = percussion stem only (single tribal hit).

### Render Sliders

| Track Group | Weirdness | Style | Audio (Inspo) |
|---|---|---|---|
| T1-5 (Digital) | 55% | 55% | 40% (dark ambient ref) |
| T6 (Chaos) | 60% | 50% | 35% |
| T7 (Cave) | 55% | 55% | 40% |
| T8 (Pivot) | 50% | 60% | 40% |
| T9-11 (Cinematic) | 50% | 60% | 45% |
| T12 (War) | 50% | 65% | 45% |
| T13-14 (Psychological) | 55% | 55% | 40% |
| T15 (Grief) | 50% | 55% | 45% |
| T16 (Warmth) | 50% | 55% | 50% (folk ref) |
| T17 (Resolution) | 50% | 60% | 45% |

**Inspo rule:** NEVER use Inspo across the digital→organic boundary (T7→T8). The pivot must be a clean sonic break.

### Parenthetical Layers

| Tracks | Allowed Layer Patterns | Style Declaration? |
|---|---|---|
| T1-3 | Delivery cues: `(hollow)`, `(dissociative)` | No |
| T3 | Self-questioning: `(who was I)`, `(no results found)` | Best with: "internal voice as quiet whispered layer" |
| T4-5 | **Named Layer: `(robotic layer: text)`** | **YES** — "low-register AI voice layered during system sections" |
| T6 | Delivery cues: `(too loud)`, `(desperate)` | No |
| T7-10 | Minimal: `(whispered)` in T7 only | No |
| T11, T15 | Alaric: `(spoken, deep) text` | No (delivery cue) |
| T12 | Absence: `(not Lyra)` / `(never Lyra)` | Best with: "parenthetical as quiet absence" |
| T14 | Self-confrontation: `(you went willingly)` | Best with: "parenthetical as internal echo" |
| T16-17 | **NONE** — resolution is clear, unified, single voice | N/A |

**Layer Rule:** `(robotic layer:)` appears ONLY in T4-5. NO named layers in Act 2.

## Character Voices (Quick)

- **Rikan/Draeven:** Male baritone A2-E4, single Persona, texture evolves per track via Style Prompt. Slight digital artifacts T1-5, clean from T7+, warmth from T16.
- **Alaric:** Deep spoken male, `(spoken, deep)` delivery cue, reverbed, ancient. T11 + T15 (ghost). Same production both times.
- **AI/Prime Directive:** Female contralto + `(robotic layer: text)`. T4-5 ONLY. Must declare in Style Prompt. NOT in Act 2.
- **Lyra:** NEVER voiced — absence is her presence. `(not Lyra)` notation in T12.
- **Shadow Weaver:** Never voiced — choir whispers name (T13). Production effect only.

## Key Motifs to Track

- Obsidian shard pulse (T7-10 — then gone)
- Nexus hum (T11, T14, T17)
- Alaric's piano theme (T11 introduced, T15 retired)
- "Vole-tek online" (T1-2, T5, T7 — not after)
- Heartbeat percussion (T8, T12, T14)
