# SOP 05: Extending an Album

> Step-by-step procedure for safely adding new tracks to an existing album.
> Prevents continuity errors from undocumented extensions.

---

## Prerequisites

- A completed Album Bible for the existing tracks
- The new concept/story material that justifies extension
- Clear understanding of WHERE the new tracks fit (sequel act? inserted? appendix?)

---

## Procedure

### Step 1 — STOP. Ask: Should This Be a New Album?

Before extending, ask:
- Does the new material continue the SAME character arc?
- Does it share the same album thesis?
- Will the sonic palette evolution make sense with additional tracks?
- Is there a narrative reason these belong TOGETHER vs separately?

**If NO to 2+ questions:** Start a new album (go to SOP 04).
**If YES:** Continue below.

### Step 2 — Define the Extension Scope

Document:
```
Extension: Act [X] — Tracks [XX-XX]
Reason: [why the story continues]
Position: [sequel to existing tracks / inserted between / parallel]
New track count: [X]
```

### Step 3 — Update the Track Registry

Add new rows to the Album Bible's track table:
```
| # | Working Title | Key | BPM | Core Emotion | Sonic Palette |
|---|---|---|---|---|---|
| [new] | [title] | [key] | [bpm] | [emotion] | [palette] |
```

**Verify:**
- [ ] No key duplicates without intentional reason
- [ ] BPM varies from adjacent tracks
- [ ] Emotions progress (don't repeat)
- [ ] Sonic palette follows the evolution map

### Step 4 — Extend the Sonic Palette Map

Add the new range to the evolution:
```
Existing Tracks 1-17: [existing palette evolution]
New Tracks 18-XX: [what the palette does now — continues? transforms? returns?]
```

**Rule 11 check:** Does any new track share >70% palette with an existing track? If yes, document the differentiation.

### Step 5 — Review Existing Rules

For each Hard Rule, answer:
- Does this rule still apply to the new tracks? (Y/N)
- Does it need modification? (If yes, what?)
- Are new rules needed for the extension?

Document:
```
Rules carrying forward: [list numbers]
Rules that are act-specific (no longer apply): [list numbers]
New rules for Act X: [list new rules]
```

### Step 6 — Update Character Voice Registry

For returning characters:
- How has their voice EVOLVED since last appearance?
- What new vocal texture distinguishes this act?

For new characters:
- Fill out full Character Voice Template
- Specify which tracks they appear in
- Define their production treatment

### Step 7 — Plan New Motifs + Existing Motif Fate

**Existing motifs:**
- Which continue into the new act?
- Which have completed their arc (don't use again)?
- Which transform into something new?

**New motifs:**
- What new recurring elements are introduced?
- Where do they first appear?
- How do they evolve across the new tracks?

### Step 8 — Verify Key Relationships

Map the new keys against the existing harmonic architecture:
- Do the new keys create meaningful relationships to the old ones?
- If the album had a key change (e.g., T17 Am→C), does the extension respect that resolution or deliberately depart from it?
- Are there harmonic callbacks that strengthen cross-act continuity?

### Step 9 — Update the Album Bible

Open `references/[ALBUM]_BIBLE.md` and update:
- [ ] Track Registry (new rows)
- [ ] Sonic Palette Evolution (extended)
- [ ] Key Relationships (new entries)
- [ ] Rules (reviewed, new ones added)
- [ ] Character Voice Registry (evolved/new)
- [ ] Motifs (status updated, new ones added)
- [ ] Emotional Arc (extended)
- [ ] Extension Protocol (note that this extension happened)

### Step 10 — Update Steering File

Open `.kiro/steering/[album].md` and update:
- [ ] Track count
- [ ] Rules (if changed)
- [ ] Palette table (extended)
- [ ] Character voices (if new ones)

### Step 11 — Commit BEFORE Writing

**Commit all bible/steering updates to version control BEFORE writing any new songs.**

This ensures:
- The documentation is the source of truth
- The hooks can check against updated rules
- Anyone else working on the album has the current state
- If songs violate rules, the rules existed first (not retrofitted)

### Step 12 — Write New Tracks

NOW proceed to SOP 01 (Writing a Song) for each new track, with the updated bible available.

---

## Common Extension Mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Writing songs before updating bible | Continuity violations discovered too late | Step 11: commit documentation FIRST |
| Keeping all old rules unchanged | New context may need different constraints | Step 5: review each rule explicitly |
| Same sonic palette as earlier tracks | Album sounds repetitive, no progression | Step 4 + Rule 11: differentiate |
| Ignoring motif completion | Motifs that were "resolved" get resurrected cheaply | Step 7: check motif status |
| Not evolving character voices | Characters sound static across acts | Step 6: mandate evolution |

---

## Time Estimate: 1-2 hours (documentation updates before writing begins)
