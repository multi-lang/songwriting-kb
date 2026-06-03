# SOP 06: Character Voice Design

> Step-by-step procedure for creating a complete vocal identity for a character,
> from accent through instrumentation through mode selection.

---

## Prerequisites

- Know WHO the character is (name, background, emotional state)
- Know WHAT they're singing about (the song's concept)
- Know the GENRE context (what instrumentation ecosystem they live in)

---

## Procedure

### Step 1 — Identify the Speaker

Answer these questions:
```
Who: [name/identity]
What are they: [human? creature? entity? concept?]
Age/era: [young? ancient? timeless?]
Emotional state: [at the START of the song]
Cultural origin: [real-world basis or fantasy]
```

### Step 2 — Choose Accent Base

**For real-world characters:** Pick the regional accent that matches their identity.

**For fantasy characters:** Choose a BLEND of real-world phonetic models:
```
Primary accent model: [e.g., Scottish]
Secondary influence: [e.g., Nordic]
Tertiary texture: [e.g., Semitic consonant weight]
```

**For non-human entities:** Choose by FEELING, not geography:
```
What does this voice FEEL like? → [e.g., stone, wind, fire, water]
What real-world sounds share that quality? → [e.g., Icelandic vowels, throat singing]
```

### Step 3 — Define Vowel Character

| Question | Answer |
|---|---|
| Open or closed vowels? | [open = warm/vast, closed = tight/urgent] |
| Long or short? | [long = sustained/patient, short = percussive/urgent] |
| Warm or cold? | [warm = human/close, cold = distant/alien] |
| Which vowels sustain best? | [list 2-3: "ah", "oh", "ee", etc.] |
| Which to avoid sustaining? | [list 1-2] |

### Step 4 — Define Consonant Character

| Question | Answer |
|---|---|
| Hard or soft? | [hard = aggressive/grounded, soft = flowing/ethereal] |
| Any special features? | [rolled R? glottal stops? sibilants?] |
| Consonant clusters? | [few = singable, many = rhythmic/percussive] |
| Plosives present? | [yes = punchy, no = flowing] |

### Step 5 — Define Rhythmic Tendency

Where does this voice sit relative to the beat?

| Position | Feels Like | Character Types |
|---|---|---|
| Behind the beat | Lazy, exhausted, ancient, vast | Dwarves, wounded entities, Southern characters |
| On the beat | Grounded, deliberate, inevitable | Warriors, mentors, Nordic |
| Ahead of the beat | Urgent, anxious, eager | Young characters, city dwellers |
| Floating/rubato | Ethereal, timeless, untethered | Elves, spirits, cosmic entities |

### Step 6 — Fill the Character Voice Template

```
CHARACTER VOICE:
• Name/Identity:
• Accent base:
• Vowel character:
• Consonant character:
• Rhythmic tendency:
• Register: [bass/baritone/tenor/alto/soprano + specific range]
• Texture: [gravelly/smooth/breathy/raspy/clear/cavernous/etc.]
• Emotional subtext: [what the voice FEELS like underneath]
• Dialect words: [5-10 words to use in lyrics that reinforce the accent]
• Instruments that match:
• Production space: [where does this voice live — cave/forest/battlefield/void?]
• Mode/scale: [what harmonic language matches this culture?]
```

### Step 7 — Select Matching Instrumentation

Based on the accent/culture, choose instruments that BELONG:

**Use the reference tables** in `references/CHARACTER_VOICE_REFERENCE.md`

If the character's cultural ecosystem doesn't have obvious instruments, build from the FEELING:
```
Voice feels like: [stone? wind? fire? water? machine?]
→ Instruments that evoke that: [deep drums? flutes? distortion? ambient pads?]
```

### Step 8 — Choose Mode/Scale

The harmonic language should match the cultural DNA:
- Celtic/Irish → Dorian, Mixolydian
- Nordic/Viking → Aeolian, Phrygian
- Elvish/ethereal → Lydian, Ionian
- Dwarvish/heavy → Aeolian, natural minor
- Middle Eastern → Phrygian dominant
- Southern US → Mixolydian, major pentatonic

### Step 9 — Write Dialect into Lyrics

Choose 5-10 words from the dialect/accent that will appear IN the lyrics to reinforce the vocal:
```
Dialect words chosen: [list them]
Usage plan: [1-2 per verse, more in intimate moments]
```

**Important:** Dialect in the lyrics FORCES the vocal model to commit to the accent. Without dialect words, the style prompt alone may produce inconsistent results.

### Step 10 — Craft the Suno Style Prompt Accent Descriptor

Write the vocal portion of the Style Prompt:
```
[accent descriptor], [voice quality], [register], [delivery style]
```

**Examples:**
- "Scottish burr accent, rolled R's, deep gravelly baritone, intimate storytelling"
- "ethereal flowing vocal, musical liquid consonants, ancient soprano, reverb-heavy"
- "cold clinical delivery, precise articulation, subtle digital artifacts, female contralto"

### Step 11 — Document Voice Evolution (If Album)

If this character appears in multiple tracks:
```
Track X: [voice at this point — texture, state, delivery]
Track Y: [how it's changed — what happened, what's different]
Track Z: [final evolution]
```

**Rule 8:** The voice must be DIFFERENT in every track. Document what changes.

---

## Verification Checklist

Before using the voice design:
- [ ] All 12 template fields filled?
- [ ] Vowel choices are SINGABLE in the chosen key?
- [ ] Instruments match the cultural ecosystem?
- [ ] Mode/scale matches the culture?
- [ ] Dialect words chosen and placed in lyrics?
- [ ] Suno accent descriptor written?
- [ ] If album: voice evolution documented?
- [ ] Production space chosen (reverb/room type)?

---

## Time Estimate: 15-25 minutes per character
