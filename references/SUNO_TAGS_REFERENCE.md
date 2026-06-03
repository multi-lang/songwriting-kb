# Suno AI — Complete Tag Reference

> All confirmed meta-tags, formatting rules, and v5.0 techniques for Suno AI song generation.
> Consolidation of Sections 12 + 13 from the Songwriting Knowledge Base.

---

## FIELD LIMITS

| Field | Limit | Overflow |
|---|---|---|
| Style of Music | 1000 chars | Negatives → Advanced box |
| Lyrics | 5000 chars | Direction blocks → Advanced box |
| Advanced box | Extra space | Catches overflow from both |

---

## STYLE PROMPT FORMULA

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Direction
```

Priority order when hitting 1000 char limit:
1. Genre + BPM + Key
2. Vocal type + delivery
3. Instruments (top 3-5)
4. Mood/direction
5. Negatives (→ Advanced if needed)

---

## GLOBAL CONTROL TAGS (Top of Lyrics field)

| Tag | Purpose | Example |
|---|---|---|
| `[track: ...]` | Global defaults (genre, mood, length, instruments) | `[track: genre: dark cinematic rock, mood: haunted, length: 270]` |
| `[control: ...]` | Behavioral directives | `[control: no-repeat, dynamic transitions]` |
| `[length: XXX]` | Target duration in seconds | `[length: 270]` |
| `[sequence: ...]` | Explicit section ordering | `[sequence: intro, verse, pre-chorus, chorus, verse, chorus, bridge, final chorus, outro]` |
| `[end]` | Song termination signal | `[end]` (at very bottom) |

---

## SECTION TAGS

### Core Structure
`[Intro]` `[Verse]` `[Verse 1]` `[Verse 2]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Outro]` `[Instrumental]` `[Hook]` `[Break]` `[Build]` `[Drop]` `[Breakdown]` `[Interlude]` `[End]`

### Vocal Assignment
`[Male Vocal]` `[Female Vocal]` `[Duet]` `[Both]` `[Choir]` `[Ad-lib]` `[Spoken Male]` `[Spoken Female]`

### Performance/Delivery
`[Soft]` `[Powerful]` `[Whispered]` `[Belting]` `[Crescendo]` `[Intimate]` `[Energetic]` `[Falsetto]` `[A Cappella]`

### Advanced Structure
`[Ascending progression]` `[Atmospheric shift]` `[Bridge modulation]` `[Key change]` `[Half-time feel]` `[Double-time feel]`

---

## PIPE NOTATION (Inline Parameters)

**Syntax:** `[SectionName | param1, param2, param3]`

```
[chorus | powerful, wide stereo, choir swell, anthemic]
[verse | vulnerable vocals, close-mic, sparse piano only]
[bridge | stripped, near-silence, spoken delivery]
```

Saves characters vs stacking multiple `[tag]` lines. Can combine vocal + production + mood.

---

## DYNAMICS & INTENSITY TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[crescendo]` | Gradual increase | slow, fast, layered, orchestral, electronic |
| `[diminuendo]` | Gradual decrease | slow, fast, layered, orchestral |
| `[silence: sudden]` | Dead silence | short, sudden, gradual, echoed |
| `[power-off drop]` | Abrupt cut-off | sudden, glitchy, resonant, percussive |
| `[build]` | Intensity ramp section | rising tension, more drums, layers thickening |
| `[big finish]` | Grand climactic ending | orchestral, rock, electronic, percussive |
| `[swell]` | Gradual volume rise | orchestral, synth-driven, percussive, dramatic |

---

## TEMPO & RHYTHM TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[modulation]` | Key change | sudden, ascending, descending, gradual, chromatic |
| `[beat-switch]` | Rhythm change | sudden, gradual, double-time, half-time, syncopated |
| `[accelerando]` | Tempo increase | gradual, sudden, layered |
| `[ritardando]` | Tempo decrease | gradual, sudden, expressive |
| `[fermata]` | Held note/chord | sustained, dramatic, subtle |

---

## VOCAL DELIVERY TAGS (v4.5+/v5.0)

| Tag | Purpose | When to Use |
|---|---|---|
| `[vulnerable vocals]` | Fragile, intimate, exposed delivery | Confessional verses, grief, quiet moments |
| `[whisper]` | Main vocal whispered (lead) | Intro lines, intimate moments, secrets |
| `[whispering]` | Background whisper layer (texture) | Atmosphere, psychological tension, ghost voices |
| `[spoken word]` | Poetic/rhythmic speech | Bridge monologues, narrative sections |
| `[narrator]` | Clear storyteller/presenter voice | Alaric quotes, system voices, framing |
| `[vocalist]` | Voice character description | `[vocalist \| weathered baritone, close-mic]` |
| `[chant]` | Repetitive vocal phrase | Hook repetition, name-as-mantra, ritual |
| `[chant-loop]` | Looped vocal pattern (building) | Background layers, hypnotic sections |
| `[call-and-response]` | Interaction pattern | Dialogue, duet exchanges, internal argument |
| `[distorted vocals]` | Gritty/processed voice | Industrial sections, breakdown moments |

---

## HARMONIC & TEXTURAL TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[pedal-point]` | Sustained bass note | low, high, suspended, dissonant |
| `[texture: X]` | Sound density | thin, dense, polyphonic |
| `[aria-rise]` | Soaring vocal climax | solo, choral, orchestral |
| `[articulation: X]` | Note style | staccato, legato, marcato |
| `[tessitura: X]` | Vocal pitch area | low, mid, high |

---

## STRUCTURAL DISTINCTIONS

| This | Means | vs This | Which Means |
|---|---|---|---|
| `[breakdown]` | Strip DOWN (subtractive, extended) | `[break]` | Brief PAUSE (transitional) |
| `[whisper]` | Lead vocal whispered | `[whispering]` | Background whisper texture |
| `[build]` | Rising intensity section | `[drop]` | Sudden intensity shift (arrival) |

---

## FADE PARAMETERS

```
[fade: slow]        — Long gradual decrease
[fade: layered]     — Instruments fade at different times
[fade: reverb-tail] — Relies on reverb decay
[fade: fast]        — Quick, abrupt
```

---

## GLITCH PARAMETERS

```
[glitch: stutter]     — Repetitive audio chopping
[glitch: bit-crush]   — Lower resolution, pixelated
[glitch: tape-stop]   — Sudden halt
[glitch: granular]    — Fragmented playback
[glitch: randomized]  — Unpredictable
```

---

## EQ HINTS

```
[eq: bass-heavy]  — Emphasize low end
[eq: bright]      — Boost highs
[eq: warm]        — Midrange-heavy
[eq: lo-fi]       — Reduced highs, vintage
```

---

## SUNO v5.0 CAPABILITIES

### Genre Mashups (use + to combine)
```
[genre: dark cinematic rock + nordic folk]
[genre: industrial + neoclassical]
```

### Natural Language Tempo
```
[tempo: slow funeral march, processional weight]
[tempo: urgent combat heartbeat, elevated but controlled]
```

### Extended Prompt Parsing
Tags embedded in natural language sentences now parse correctly in v5.0.

### Unrecognized Tags = Section Labels
`[Verse 1 – Cold / Vast]` is parsed as a section. Our mood-labeled sections work.

---

## BPM REFERENCE

| Range | Feel | Genres |
|---|---|---|
| 60-70 | Ballad, ambient, cinematic | Grief, intimate, dirge |
| 70-85 | R&B, soul, trip-hop | Vulnerability, confession |
| 85-100 | Hip-hop, neo-soul | Indie, alternative |
| 100-115 | Pop, indie, folk | Walking pace, accessible |
| 115-125 | Pop, dance-pop, funk | Energy, dance |
| 125-135 | Rock, EDM | Driving, aggressive |
| 135+ | Punk, metal, D&B | Maximum intensity |

---

## DUET MODES

### Mode A — Per-Line Tags (Complex/Cinematic)
`[Male Vocal]`/`[Female Vocal]` per line + Direction blocks as anchors

### Mode B — Parenthetical (Space-Efficient)
Main voice unformatted, response in `()`. Style must declare: "male voice for sections without (), female voice for response in ()"

### Mode C — Custom Layers (Theatrical)
Custom conventions `(robotic layer: text)` + mood-labeled sections + stacked production tags

---

## NEGATIVE PROMPTS / EXCLUSIONS

Format: `[Exclusions: ‑item, ‑item, ‑item]`

Common exclusions by genre:
- **Dark/cinematic:** ‑bright synths, ‑upbeat energy, ‑cheerful melodies, ‑trap drums
- **Folk/acoustic:** ‑EDM drops, ‑heavy distortion, ‑industrial textures
- **Always include:** ‑beatboxing, ‑vocal hums (prevents common Suno artifacts)

---

## OBSOLETE TAGS (Avoid)

| Tag | Status | Use Instead |
|---|---|---|
| `[bpm: 80]` | ❌ Ignored | BPM in Style Prompt |
| `[key: Am]` | ❌ Ignored | Key in Style Prompt |
| `[loop]` | ❌ Unsupported | Manual repetition |
| `[autotune]` | ❌ Deprecated | Describe vocal style |
| `[mix]`/`[master]` | ❌ Ineffective | Use `[eq]` or describe |
| `[volume]` | ❌ Ineffective | Use dynamics tags |
| `[filter]` | ❌ Ineffective | Describe in direction |
| `[section]` | ❌ Redundant | Use specific names |

---

## COMPLETE TEMPLATE (v5.0 Optimized)

```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]

STYLE PROMPT:
Genre, BPM, Mood, Instruments, Vocal Style, Production Direction

[Exclusions: ‑item, ‑item, ‑item]

LYRICS:

[Title: Song Title]

[Production Direction: Overall tone, dynamics, key decisions]
[Vocal Direction: Voice type, delivery, emotional progression]

[intro | atmospheric, sparse]
(lyrics)

[verse | vulnerable vocals, close-mic]
(lyrics — 4-8 lines, no end punctuation)

[build | rising tension]
(pre-chorus — 2-4 lines)

[chorus | powerful, wide]
(chorus — 4-6 lines, hook prominent)

[bridge | stripped]
[silence: sudden]
(bridge — 3-4 lines, the turn)

[modulation: ascending to relative major]
[final chorus | big finish, choir]
(final chorus — 4-6 lines)

[outro]
[fade: layered, reverb-tail]
(outro — 2-4 lines)
[end]
```

---

## LYRIC RULES

1. Section tags on own line — never same line as lyrics
2. 4-8 lines per section maximum
3. NO punctuation at end of lines
4. Each line = one melodic phrase
5. Total lyrics under 5000 characters
6. Em dashes (—) for breath/phrasing within lines
7. Line breaks guide rhythm
