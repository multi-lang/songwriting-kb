# SOP 05 Stress Test Report

> **Test Context:** Following SOP 05 step-by-step to extend the Keeper of the Light album with a 3-track prequel act ("Who built the lighthouse? Who taught the first keeper?").
> **Input Album:** `references/KEEPER_OF_THE_LIGHT_BIBLE.md` (8-track concept album, complete bible)
> **Extension Concept:** A prequel act (3 tracks) exploring the lighthouse's construction and the first keeper's appointment, set ~200 years before Track 1.
> **Date:** Stress test completed following SOP 05 exactly as written.

---

## EXECUTIVE SUMMARY

**Overall Verdict:** SOP 05 works well for its designed use case (SEQUELS — appending new tracks after existing ones) but has significant blind spots for PREQUELS and INSERTIONS. The core issue: the entire SOP assumes extension means "adding to the end." Track numbering, rule references, sonic palette direction, and motif guidance all default to a left-to-right/chronological-forward model. The Keeper of the Light bible explicitly lists "prequel" as a potential extension direction, making this a realistic test case that the SOP can't fully handle.

**Completion Status:** All 12 steps followable, but Steps 2-5 and 7-8 required significant improvisation for a prequel scenario that the SOP doesn't address.

---

## STEP-BY-STEP EXPERIENCE

### Step 1 — STOP. Ask: Should This Be a New Album?
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Excellent gate. The 4 questions are well-chosen — they genuinely help distinguish "extension" from "new album." For a prequel that shares the same thesis and world, the answer is clearly "extend." No issues.

---

### Step 2 — Define the Extension Scope
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Position options incomplete):** The template asks for position: "sequel to existing tracks / inserted between / parallel." PREQUEL (before existing tracks) isn't listed. A prequel is arguably "inserted before," but that's not what "inserted between" means. Add "prequel (before existing tracks)" to the position options.

**Problem 2 (No numbering convention for prequels):** If I add 3 tracks before the existing 8, do I:
- Renumber everything (new T1-T3, old T1→T4, old T8→T11)?
- Use prefix numbering (P1, P2, P3 + existing T1-T8)?
- Use act-based numbering (Act 0: T01-T03, Act 1: T04-T11)?

The SOP doesn't specify. Looking at Fractured Shadows (which uses Act 2/3 numbering after an initial set), the pattern suggests act-based approach. But this should be explicit.

**My decision:** Used prefix approach (P01, P02, P03) to avoid renumbering existing tracks and invalidating all number-based rules.

---

### Step 3 — Update the Track Registry
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem (Rule-by-number fragility):** The existing bible has rules like "D Mixolydian = T1 and T8 ONLY." When adding prequel tracks, these number references become ambiguous. Does the rule mean:
- "The tracks currently called T1 and T8" (content-based → keeps working)?
- "The first and last tracks of the album" (position-based → breaks if new tracks are added around them)?

In practice, it means the content ("The Keeper's Morning" and "Lullaby for Leviathan") — but the SOP doesn't flag this as something to verify. The bible's rules should ideally reference tracks by TITLE as well as number for resilience.

---

### Step 4 — Extend the Sonic Palette Map
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem (Template assumes appending):** The template shows:
```
Existing Tracks 1-17: [existing palette evolution]
New Tracks 18-XX: [what the palette does now]
```

For a prequel, the new palette section goes BEFORE the existing one chronologically. The template format doesn't demonstrate this. Should be:
```
Prequel (P1-P3): [ancient/primitive palette → leads to T1's established sound]
Existing (T1-T8): [existing palette — unchanged]
```

The SOP should note: "For prequels, the new palette section PRECEDES the existing map. Show how the prequel's final track sonically ARRIVES at T1's established palette."

---

### Step 5 — Review Existing Rules
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ NEEDS IMPROVEMENT |
| Missing info | Significant |
| Cross-reference needed | No |

**Problem 1 (Number-referenced rules in prequels):** This is the SOP's biggest structural issue for non-sequel extensions. The instruction says "For each Hard Rule, answer: Does this rule still apply?" — which is correct. But it doesn't flag the specific danger of NUMBER-REFERENCED rules when tracks are added before or between existing ones.

Example rules that become ambiguous:
- "D Mixolydian = T1 and T8 ONLY" — still means those specific tracks? Or the new first/last?
- "No distortion before Track 3" — Track 3 of what? The original sequence? The new combined sequence?
- "Concertina in T1, T2, T8 ONLY" — the content tracks? Or the positions?

**Suggested addition:** "⚠️ If adding tracks BEFORE or BETWEEN existing tracks: review all rules that reference track NUMBERS. Determine whether the rule means the track CONTENT (specific song) or the track POSITION (first, third, last). Clarify in the updated bible by adding track titles alongside numbers."

**Problem 2 (No "new rules for the extension" template):** The SOP says "Are new rules needed for the extension?" but doesn't give a template or examples of what extension-specific rules look like. For a prequel, new rules might include: "Prequel tracks must NOT use motifs that don't exist yet in the story timeline" or "The sonic palette of P3 must audibly transition toward T1's sound."

---

### Step 6 — Update Character Voice Registry
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | Yes — not linked |

**Problem (Template reference ambiguous):** "For new characters: Fill out full Character Voice Template" — but WHICH template? Options in this repo:
1. The template in SOP 06 (Step 6 — "Fill the Character Voice Template")
2. The format in `references/CHARACTER_VOICE_REFERENCE.md`
3. The format used in the existing bible's Character Voice Registry

These have slightly different fields. The SOP should specify: "Use the Character Voice Template from SOP 06, Step 6. The resulting entry will be formatted to match the existing bible's Character Voice Registry section."

---

### Step 7 — Plan New Motifs + Existing Motif Fate
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem (Prequel motif logic differs from sequel):** The questions "Which [motifs] continue? Which have completed their arc? Which transform?" assume FORWARD motion (sequel logic). For a prequel, the questions should be:
- Which existing motifs should be FORESHADOWED in the prequel (planted as seeds)?
- Which existing motifs have ORIGINS in this time period (their first historical appearance)?
- Which existing motifs DON'T EXIST YET in the story timeline (must NOT appear)?

Example: "The light keeps..." can't appear in a prequel set before the lighthouse is built — unless as dramatic irony (a prophecy, a builder's phrase). The SOP doesn't offer this temporal-direction awareness for motif planning.

**Suggested addition:** "For PREQUELS: reverse the motif logic. Ask: Which existing motifs can be SEEDED here (origin point)? Which must be ABSENT (they don't exist yet in the story timeline)? Which can appear as dramatic irony (the audience knows the future significance, the characters don't)?"

---

### Step 8 — Verify Key Relationships
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (No harmonic-direction guidance for prequels):** For a sequel, the question is "do new keys depart meaningfully from the resolution?" For a prequel, the question should be "do the prequel's keys ARRIVE at T1's key in a way that feels like a harmonic runway?" The SOP doesn't distinguish these two harmonic design philosophies.

**Suggested addition:** "For prequels: the final prequel track's key should create a natural harmonic gravity toward the existing T1's key — the listener should feel 'arrival' when the original album begins."

---

### Step 9 — Update the Album Bible
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** The checklist says "Track Registry (new rows)" — for prequels, clarify whether new rows go at the TOP of the table (chronological order) or the BOTTOM (order of creation). Recommendation: chronological order with clear act headers.

---

### Step 10 — Update Steering File
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem:** If the steering file has rules with hard-coded track numbers (the Keeper steering file has "D Mixolydian = T1 and T8 ONLY"), and those numbers now refer to content (not position), the steering file needs updating to include title references for clarity. The SOP should note: "If rules in the steering file reference track numbers, add track titles for disambiguation after extension."

---

### Steps 11-12 — Commit & Write
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** No issues. The principle of committing documentation before writing is well-stated and important.

---

## GENERAL ISSUES

### Issue A: Sequel-Centric Design

The entire SOP assumes APPENDING. Templates, numbering, palette evolution direction, motif questions, and key relationship logic all default to "add after existing." Three extension types exist:
1. **Sequel** (after) — fully supported ✅
2. **Prequel** (before) — poorly supported ⚠️
3. **Insertion** (between) — not supported ❌

The bible explicitly lists "prequel" as an extension direction. The SOP should accommodate it.

### Issue B: Number-Referenced Rules Are Fragile

When rules say "Track 3" they could mean content or position. This ambiguity is latent in the existing bible and becomes acute during extension. The SOP should flag this as a hazard and recommend title+number references for all rules.

### Issue C: No Cross-Reference to Bible's Extension Protocol

The Keeper bible has its own "Album Extension Protocol" section that says "⚠️ Before writing ANY track outside this registry (T1-8), you MUST: [5 steps]." SOP 05 is essentially the expanded version of those 5 steps, but the SOP never references the bible's protocol or says "this SOP IS the procedure referenced in your bible's extension protocol." Making that connection explicit would help.

---

## RECOMMENDATIONS

### Priority 1 (Would eliminate most confusion)
1. **Add prequel support to Step 2:** Include "prequel (before existing tracks)" in the position options. Add a numbering convention note: "For prequels, use prefix numbering (P01, P02...) to avoid renumbering existing tracks. For sequels, continue sequential numbering. For insertions, use decimal notation (T3a, T3b) or renumber with act headers."
2. **Add number-reference warning to Step 5:** Flag that rules referencing track numbers may be content-based or position-based. Recommend adding track titles alongside numbers in all rules for resilience.
3. **Add prequel motif logic to Step 7:** Reverse the motif questions for prequels (seeding, absence, dramatic irony).

### Priority 2 (Would improve flow)
4. **Add prequel palette guidance to Step 4:** "For prequels, show how the new palette ARRIVES at T1's established sound."
5. **Add prequel key guidance to Step 8:** "Final prequel track should create harmonic gravity toward existing T1."
6. **Specify which Character Voice Template in Step 6:** Reference SOP 06, Step 6 explicitly.
7. **Add cross-reference to bible's extension protocol:** Note that this SOP is the expanded procedure referenced in album bibles.

### Priority 3 (Nice to have)
8. **Add insertion guidance** for tracks added between existing ones (decimal numbering, adjacency re-checks).
9. **Clarify bible table ordering** in Step 9: chronological with act headers.
10. **Add steering file number-check** to Step 10: verify hard-coded track numbers are still accurate.

---

## FINAL VERDICT

**SOP 05 is a solid B.** For its designed use case (sequels/appending), it's thorough and logical — the step ordering is correct, the "Common Extension Mistakes" table is excellent, and the "commit before writing" principle is critical. But the Keeper of the Light bible EXPLICITLY lists "prequel" as a planned extension, and the SOP can't handle it without significant improvisation. The fundamental gap is that "extension" is treated as synonym for "continuation" when it actually encompasses three distinct operations (append, prepend, insert) that require different numbering, rule-review, and harmonic-design approaches.

**Time actually spent:** ~45 minutes (vs the SOP's "1-2 hours" estimate — faster because this was documentation planning only, no actual writing. The estimate is likely accurate for a full documentation pass including bible updates.)

---

*Filed during Keeper of the Light stress test, SOP 05 extension planning (prequel scenario).*
