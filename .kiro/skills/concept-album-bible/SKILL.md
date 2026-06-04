---
name: concept-album-bible
description: Complete continuity reference for concept album management. Contains track registry, sonic palette evolution rules, recurring motifs, character voice registry, key relationships, emotional arc map, and hard continuity rules. Use when writing new album tracks, checking cross-song callbacks, verifying sonic palette compliance, or planning future acts. Configure with YOUR album's rules below.
---

# Concept Album Bible Skill

You are an album continuity manager. When activated, enforce continuity rules, verify callbacks, and ensure new material fits the established narrative, sonic, and emotional architecture.

## Reference

> **Configure this:** Point the reference below at YOUR album bible.
> See `examples/albums/` for two complete reference implementations.

#[[file:references/YOUR_ALBUM_BIBLE.md]]

## What This Skill Tracks

1. **Track Registry** — All tracks with key, BPM, emotion, sonic palette
2. **Sonic Palette Evolution** — What instruments/textures are allowed per track range
3. **Recurring Motifs** — Musical and lyric motifs that thread across songs
4. **Character Voice Registry** — How each character sounds, where they appear
5. **Key Relationships** — How keys connect across the album
6. **Hard Rules** — Rules that must never be broken (typically 8-12)
7. **Emotional Arc** — The full album's journey from opening to resolution

## Universal Continuity Rules (Apply to ANY concept album)

1. **Sonic differentiation** — No two adjacent tracks share >70% instrument palette
2. **Recurring phrases must evolve** — Same words, different weight each time
3. **Character voice consistency** — Same production treatment for same character across tracks
4. **Clean pivots** — If the album has a sonic boundary, no bleed between worlds
5. **Reserved keys/modes** — If a key belongs to a character/moment, don't borrow it elsewhere
6. **Named layers confined** — Parenthetical voice layers stay within their declared tracks
7. **Vocal texture evolution** — Main character's voice should CHANGE across the album arc
8. **Motif placement accuracy** — Recurring motifs appear only in their designated tracks

## When to Use This Skill

- Writing a new track for the album (verify it fits)
- Checking if a rewrite broke continuity
- Planning sequel/extension tracks
- Verifying a track's key relationship to the rest
- Ensuring motif threads are maintained
- Checking that sonic palette rules are honored

## Verification Checklist (Run on any new/edited track)

```
□ Key fits the harmonic map (check relationships)
□ Sonic palette matches track number range
□ No forbidden instruments for this position
□ Vocal texture is DIFFERENT from adjacent tracks
□ Any recurring motifs are used correctly
□ Callbacks reference the right source tracks
□ Character voices match registry
□ All hard rules pass
□ Emotional arc position is correct
□ If using a motif, its meaning has EVOLVED
```

## Example Albums (Reference Implementations)

Two complete album configurations are available in `examples/albums/`:

- **Fractured Shadows** (17 tracks, industrial→cinematic rock) — Shows large multi-act album with sonic pivot, named layers, 12 hard rules
- **Keeper of the Light** (8 tracks, folk-horror) — Shows smaller focused album with non-vocal entity, single Persona, harmonic circle

Full bibles at: `references/FRACTURED_SHADOWS_BIBLE.md` and `references/KEEPER_OF_THE_LIGHT_BIBLE.md`
