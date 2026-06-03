# Keeper of the Light — Album Continuity Rules

> Auto-loaded. Enforces continuity when working on album material.
> Full bible: references/KEEPER_OF_THE_LIGHT_BIBLE.md
> System: Suno v5.5 (Personas, Stems, Era Tags, Layers)

---

## Active Album

**Keeper of the Light** — 8 tracks
Genre: Folk-horror / sea-shanty / dark ambient

## ALBUM EXTENSION PROTOCOL

**⚠️ STOP — Before writing ANY track outside the current registry (T1-8):**
1. Update `references/KEEPER_OF_THE_LIGHT_BIBLE.md` with new track registry (including Persona assignment)
2. Extend the sonic palette evolution map
3. Define which existing rules carry forward vs which are act-specific
4. Get the bible update committed BEFORE writing new songs
5. Use SOP 05 — supports sequels, prequels (P01, P02...), and insertions (T3a, T3b...)

---

## 12 Hard Rules (Never Break)

1. **The sea is always audible** — every track has ocean sound in some form
2. **D Mixolydian = T1 (The Keeper's Morning) and T8 (Lullaby for Leviathan) ONLY** — keeper's identity key, protected
3. **Fm = Track 7 (It Remembers the Sun) ONLY** — creature's key, never borrowed
4. **No distortion/effects before Track 3** — T1-2 must be warm and handmade
5. **"The light keeps" appears in T1, T3, T5, T8 only — each meaning different** — pride → question → panic → truth
6. **The creature is NEVER named** — always oblique ("it," "what sleeps," etc.)
7. **Keeper sings alone until Track 7** — no harmony, no choir, no human duets before then
8. **Track 6 = quietest track on album** — near-silence, drones only
9. **Concertina in T1, T2, T8 ONLY** — keeper's instrument, timbral motif
10. **T8 BPM = T1 BPM (92)** — same heartbeat, different existence
11. **No two adjacent tracks share >70% palette** — sonic differentiation mandatory
12. **T5 = loudest moment (dynamic ceiling)** — nothing after exceeds the storm

## Sonic Palette by Track Range

| Tracks | Allowed Palette | Era Tag |
|---|---|---|
| 1-2 | Warm acoustic folk, concertina, bodhran, sea-wash, close-mic vocal | NO decade tags — use "handmade, analog warmth, organic" |
| 3 | Darkened folk, fingerpicked guitar, bowed drone, whispered harmony | None |
| 4 | Dark ambient + folk bones, sub-bass, reversed choir | None |
| 5 | Storm percussion, distorted fiddle, desperate vocal, chaos | None |
| 6 | Near-silence, drone ambient, whale-song bass, glass textures | None |
| 7 | Massive choir, orchestral, creature's lament, sub-bass | None |
| 8 | T1 palette reversed/submerged, glass harmonica, underwater filter | None |

**Era Tag Rule:** Do NOT use decade-era tags for this album. The sound is "timeless coastal folk" — not any specific real-world era. Use feeling-descriptors instead.

## v5.5 Production

### Persona: Maren (Single Voice, 4 Delivery Variants)

All tracks use the SAME vocal Persona (female mezzo, coastal folk timbre). Delivery is controlled per track via Style Prompt:
- T1-2: `warm conversational, close-mic, slight coastal rasp, intimate`
- T3: `hushed careful, reading tone, close-mic, quiet`
- T4: `awed whisper, intimate, reverbed, haunted`
- T5: `raw desperate, shouting, breaking, vocal fry edges, projected`
- T6: `barely whispered, dissociative, close-mic, near-silence`
- T7: `small defiant, intimate against vastness, reverbed`
- T8: `serene, underwater reverb, doubled, becoming glass harmonica`

### Stems: Post-Render Checks

After extracting stems from each track, verify:
- **Backing Vocals stem:** EMPTY for T1-6 (Rule 7 — keeper sings alone)
- **Bass stem:** No sub-bass in T1-2 (creature hasn't stirred yet)
- **Effects/Ambience stem:** Sea-wash present in ALL tracks (Rule 1)
- **Synth stem:** EMPTY for T1-2 (Rule 4 — no effects before T3)

### Render Sliders

| Track | Weirdness | Style | Audio (Inspo) |
|---|---|---|---|
| T1 | 50% | 55% | 45% (folk ref) |
| T2 | 50% | 55% | 50% (use T1 as Inspo) |
| T3-4 | 55% | 50% | 45% |
| T5 | 50% | 60% | 40% |
| T6 | 60% | 45% | 35% |
| T7 | 55% | 60% | 40% |
| T8 | 50% | 60% | 50% (use T1 as Inspo) |

### Parenthetical Layers

This album uses **delivery cues only** — no Named Layers:
- T3: `(spoken, flat) text` — logbook entries
- T5: `(desperate)` or `(shouted)` — intensity cues
- T6: `(whispered) text` — near-silence
- T8: `(serene, doubled) text` — transformation

**No `(layer-name: text)` patterns.** The horror is SONIC (production), not vocal (layers). The creature is expressed through instruments and sub-bass, not a secondary voice.

## Character Voices (Quick)

- **Maren (The Keeper):** Female mezzo A3-E5, single Persona, texture evolves per track via Style Prompt. Dry/close T1-2, increasingly reverbed, underwater by T8. SINGS ALONE until T8 (self-harmony only).
- **The Ancient Thing:** NOT a voice — sonic presence only. Sub-bass + 40-voice glossolalia choir at half-tempo. T7 only. Never speaks words. Expressed through production tags, NOT parenthetical layers.
- **Logbook Voice:** Maren reading flatly, `(spoken, flat)` delivery cue. Filtered/crackled. T3 only. 4-6 lines max.

## Key Motifs to Track

- "The light keeps..." (T1, T3, T5, T8 — evolving meaning)
- Keeper's Melody / concertina theme (T1, T2 hummed, T8 glass harmonica)
- Sea-wash rhythm (all tracks — evolving form — ride via Effects/Ambience stem in mastering)
- Sub-bass pulse (T4 first, T5, T6, T7 — creature stirring → waking)
- Lighthouse beam sweep / phaser (T1, T3, T5, T8)
- Descending 5ths (T3, T4, T6, T7 — depth/descent)
- Glass resonance (T4, T6, T7, T8 — the membrane)
