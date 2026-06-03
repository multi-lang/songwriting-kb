---
title: Song Format Validation
description: Validates that new song files contain all required sections (Style Prompt, Exclusions, Title tag, Production/Vocal Direction blocks, Production Notes)
event: file_create
path: songs/**/*.md
---

# Song Format Check

When a new song file is created in the `songs/` directory, validate it contains all required sections.

## Required Sections (Flag if missing)

1. **Style Prompt** — Must exist, comma-separated descriptors
2. **`[Exclusions: ...]`** — Must be present after Style Prompt
3. **`[Title: Song Name]`** — Must be first tag in lyrics
4. **`[Production Direction: ...]`** — Overall tone guidance block
5. **`[Vocal Direction: ...]`** — Voice type and delivery block
6. **Section tags** — At minimum: `[Intro]` or `[Verse 1]`, `[Chorus]`, `[Bridge]` or equivalent
7. **Production Notes block** — Must contain at minimum:
   - Key (with reasoning)
   - Tempo (BPM)
   - Time Signature
   - Chord Progression (Nashville + actual chords)
   - Vocal description
   - Instruments
   - Dynamics arc
   - Hook Type
   - Rhyme Scheme
   - Emotional Arc

## Validation Actions

For each missing section, report:
```
⚠️ MISSING: [Section Name] — Required for Suno-ready output
```

If all sections present:
```
✅ Song format valid — all required sections present
```

## Additional Checks

- Style Prompt should be under 1000 characters (flag if over)
- Total lyrics content should be estimatable under 5000 characters (flag if likely over)
- Verify `[Title:]` tag matches the filename/heading
