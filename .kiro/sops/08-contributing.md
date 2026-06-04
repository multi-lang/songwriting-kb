# SOP 08: Contributing (Community Guide)

> How to use this system for your own projects, add your own album,
> customize preferences, and contribute back.

---

## For New Users: Getting Started

### Step 1 — Clone the Repo

```bash
git clone https://github.com/Voletek/songwriting-kb.git
```

The `.kiro/` directory auto-configures Kiro IDE with all agents, skills, hooks, and steering.

### Step 2 — What You Get Immediately (Universal)

These work for ANY songwriter with zero customization:
- 4 agents (songwriter, critic, suno-optimizer, album-continuity)
- 5 skills (critique, suno-tags, music-theory, character-voice, concept-album-bible)
- 3 universal hooks (format-check, char-count, prosody-lint) + album-specific continuity hooks (one per example album)
- 8 SOPs (writing, critiquing, optimizing, album setup, extending, character voice, full pipeline, contributing)
- Full songwriting knowledge base (13 sections)
- Full music production theory (12 disciplines + 23 frameworks)
- Complete Suno tag reference (35 confirmed tags + v5.0)
- Character voice design system

### Step 3 — What You Should Customize

These files contain templates — personalize them:

| File | What to Do |
|---|---|
| `.kiro/steering/output-preferences.md` | Edit with YOUR output format preferences |
| `.kiro/steering/concept-album.md` | Generic framework — add your album's conditional steering (see examples/) |
| `.kiro/agents/album-continuity.md` | Configure with YOUR album's rules |
| `references/YOUR_ALBUM_BIBLE.md` | Replace with YOUR album bible (or delete if no album) |
| `songs/` | Replace with YOUR songs |

**Example albums** are in `examples/albums/` — study them for format reference, then copy patterns to your active files. The bibles in `references/` (Fractured Shadows, Keeper of the Light) are kept as format references you can study.

---

## Setting Up Your Own Preferences

### Step 4 — Create Your Preferences File

Edit `.kiro/steering/output-preferences.md` directly — it ships as a generic template.

See `examples/preferences/voletek-preferences.md` for a filled-in reference implementation showing all options.

Customize:
- What should Production Notes include? (minimum: Key, Tempo, Chords, Vocal, Instruments)
- What's your preferred rhyme scheme?
- What are YOUR hit formulas (your audience, your genre)?
- How do you format duets?
- Any personal conventions?

---

## Setting Up Your Own Concept Album

### Step 5 — Follow SOP 04

Use SOP 04 (Setting Up a Concept Album) to create:
1. Your Album Bible in `references/[YOUR_ALBUM]_BIBLE.md`
2. Your steering file in `.kiro/steering/[your-album].md`
3. Your continuity hook in `.kiro/hooks/[album]-continuity-check.md`

### Step 6 — Update the Concept Album Bible Skill

Edit `.kiro/skills/concept-album-bible/SKILL.md`:
- Change the `#[[file:...]]` reference to point at YOUR bible
- Update the rule list to YOUR rules

**Note:** The `#[[file:path]]` syntax is Kiro's file-reference system — it embeds the referenced file's content when the skill is activated. Replace the path with your bible's location (e.g., `#[[file:references/YOUR_ALBUM_BIBLE.md]]`).

### Step 7 — Update the Album Continuity Agent

Edit `.kiro/agents/album-continuity.md`:
- Replace specific rule checks with YOUR rules
- Replace the key map with YOUR key map
- Replace the emotional arc with YOUR arc

---

## Contributing Back to the Community

### What We Accept

| Type | Examples | Requirements | Target File |
|---|---|---|---|
| **Knowledge base additions** | New genre conventions, new Suno tag findings, new theory | Must be sourced, verified, and universal | `SONGWRITING_KNOWLEDGE_BASE.md` or `MUSIC_PRODUCTION_THEORY.md` |
| **Suno tag findings** | New confirmed tags, updated tag behavior | Must be tested and verified | `references/SUNO_TAGS_REFERENCE.md` |
| **New skills** | Genre-specific skills (metal songwriting, hip-hop production) | Must follow SKILL.md format with reference doc | `.kiro/skills/[new-skill]/` |
| **New hooks** | Additional quality checks | Must be useful to >1 person | `.kiro/hooks/` |
| **Bug fixes** | Incorrect tag syntax, outdated Suno info | Must include evidence of the fix | Relevant file |
| **SOPs** | New procedures for workflows not covered | Must follow SOP format | `.kiro/sops/` |
| **Example albums** | YOUR completed album bible as a reference | Helps others see how a filled system looks | `references/` |

### What We Don't Accept

- Personal preferences as universal rules
- Unverified Suno tag claims (test first)
- Genre opinions disguised as facts
- Style prescriptions ("you SHOULD write in minor keys")

### How to Submit

1. Fork the repo
2. Create a branch: `contribution/[your-addition]`
3. Add your content following existing format
4. Verify: no personal references in universal files (search for your album name, character names, or personal details — these should only appear in personal files)
5. Submit PR with description of what you're adding and why

---

## File Organization Rules

### Universal Files (Don't Put Personal Content Here)
```
SONGWRITING_KNOWLEDGE_BASE.md
MUSIC_PRODUCTION_THEORY.md
references/CRITIQUE_REFERENCE.md
references/SUNO_TAGS_REFERENCE.md
references/CHARACTER_VOICE_REFERENCE.md
.kiro/steering/songwriting.md
.kiro/steering/suno-formatting.md
.kiro/steering/output-preferences.md
.kiro/steering/concept-album.md
.kiro/agents/songwriter.md
.kiro/agents/critic.md
.kiro/agents/suno-optimizer.md
.kiro/skills/*/SKILL.md
.kiro/hooks/song-format-check.json
.kiro/hooks/suno-char-count.json
.kiro/hooks/prosody-lint.json
.kiro/sops/*.md
```

### Personal Files (Customize These)
```
.kiro/agents/album-continuity.md (configure YOUR rules)
.kiro/hooks/[album]-continuity-check.json (create for YOUR album)
references/YOUR_ALBUM_BIBLE.md (replace with YOUR bible)
references/[YOUR_ALBUM]_BIBLE.md
songs/**/*
```

### Example/Reference Files (Study, don't edit)
```
examples/albums/*/
examples/preferences/
references/FRACTURED_SHADOWS_BIBLE.md
references/KEEPER_OF_THE_LIGHT_BIBLE.md
```

---

## Example: Starting From Scratch

```bash
# Clone
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb

# Edit preferences (already a generic template — just fill in your conventions)
# See examples/preferences/voletek-preferences.md for a filled-in reference
nano .kiro/steering/output-preferences.md

# Optional: remove example album bibles (or keep as format references)
rm references/FRACTURED_SHADOWS_BIBLE.md
rm references/KEEPER_OF_THE_LIGHT_BIBLE.md

# Optional: remove example song files
rm -rf songs/album_act2 songs/album_act3 songs/experimental songs/keeper_of_the_light
rm songs/0*_*.md songs/Shadow* songs/Shapes* songs/What_If* songs/Evil* songs/Cat*

# Create your own album (follow SOP 04)
# This creates your bible, steering, and hooks

# Start writing songs (follow SOP 01)
# Use the full pipeline (SOP 07) for best results
```

---

## FAQ

**Q: Do I need a concept album to use this system?**
A: No. The songwriter agent, critic, suno-optimizer, and all knowledge base files work for standalone songs. The album continuity system is optional.

**Q: Can I use this without Kiro IDE?**
A: Yes. The knowledge base files, SOPs, and reference docs work with any AI assistant. The agents/skills/hooks/powers are Kiro-specific features but the CONTENT they contain is universal. SOPs (in `.kiro/sops/`) are tool-agnostic procedures — follow them with any AI assistant or manually.

**Q: Do I need to use Suno?**
A: No. The songwriting methodology (9-step, 12-category rubric, Nashville method) works for any songwriting — human performance, other AI tools, or traditional recording. The Suno-specific sections (tags, formatting, sliders) are only relevant if using Suno.

**Q: Can I use this for genres not covered in the knowledge base?**
A: Yes. The framework is genre-agnostic. The theory, prosody, and arrangement principles apply to any style. If you write metal, hip-hop, jazz, or country — the 9-step analysis still works. You'd just apply different genre conventions in Step 6.
