# SOP 02 Stress Test Report

> **Test Context:** Following SOP 02 step-by-step to critique Track 01: "The Keeper's Morning" from the Keeper of the Light album.
> **Input Song:** `songs/keeper_of_the_light/01_The_Keepers_Morning.md` (complete with lyrics, production notes, and self-score)
> **Date:** Stress test completed following SOP 02 exactly as written.

---

## EXECUTIVE SUMMARY

**Overall Verdict:** SOP 02 is one of the stronger SOPs — clean structure, logical flow, and the 9-step → 12-category → flags → recommendations pipeline works well in practice. However, several assumptions surface when applied to a real concept-album track with existing self-scores. The biggest gaps: rubric mismatch with SOP 01's self-scoring, no guidance for non-lyric flags, and a naming convention that doesn't scale for multi-album repos.

**Completion Status:** All 9 steps followable to completion. Issues are clarity/edge-case problems, not blockers.

---

## STEP-BY-STEP EXPERIENCE

### Step 1 — Read Completely (No Scoring Yet)
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Excellent step. The three absorption questions (what is this trying to be? intended context? emotional thesis?) are the right orientation. No issues.

---

### Step 2 — Apply the 9-Step Analysis
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Notes:** The 9-step list matches the CRITIQUE_REFERENCE's 9-step workflow. Format is clear ("1-2 sentences each" is a good constraint).

**Minor issue:** Step says "work through each quickly" but doesn't specify output format. Should these be bullet points? A numbered list? Prose paragraph? Looking at the Step 9 output template, the 9-step analysis results don't appear anywhere in the final report. So where do they GO? Are they just mental scaffolding? If so, say that. If they're supposed to be documented, show where in the template.

---

### Step 3 — Score Each Category (1-10)
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | Yes — critical |

**Issues found:**

**Problem 1 (Rubric mismatch with SOP 01):** The song already has a self-score using a DIFFERENT 12-category rubric (from SOP 01 Step 26: "Emotional Truth, Prosody/Singability, Hook Strength, Imagery/Specificity, Structure/Pacing, Originality, Genre Authenticity, Production Clarity, Album Continuity, Lyric Economy, Dynamic Range, Replay Value"). SOP 02 uses: "Hook, Lyrics, Prosody, Arc, Structure, Originality, Singability, Commercial, Genre, Arrangement, Voice, Emotional Intelligence." These are DIFFERENT systems. A user who writes a song with SOP 01's self-score and then critiques it with SOP 02's rubric gets non-comparable numbers. This is confusing and undermines the score-based decision gate in SOP 07 (which says "if composite ≥8.5, skip revision").

**Problem 2 (Context rule placement):** "Score relative to INTENDED context" appears as a single line AFTER the scoring table. For a concept album track, this is the most important instruction — it fundamentally changes how you score categories like Commercial (#8) and Structure (#5). It should appear BEFORE or at the top of the table, not after.

**Problem 3 (Score definitions not in SOP):** The SOP gives "questions to answer" per category but not the actual 1-10 scale definitions. Those are in `references/CRITIQUE_REFERENCE.md`. A user following only the SOP has no rubric granularity — they'd guess what "7" vs "8" means. The SOP should either inline the rubric or explicitly say "Score using the definitions in CRITIQUE_REFERENCE.md — this is required, not optional."

---

### Step 4 — Calculate Composite
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Simple, clear. Average 12 scores.

---

### Step 5 — Identify Strongest Line
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Good step. Clear instruction, good constraint (ONE line, 1-2 sentence explanation). Works perfectly — "When the world forgets you wait" is an obvious strongest-line candidate.

---

### Step 6 — Flag 2-3 Issues
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ PARTIALLY UNCLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Assumes all flags are lyric issues):** The instruction says "Quote the current line" and "Provide 2-3 alternative lines." But what about NON-LYRIC flags? When critiquing this track, valid flags might include:
- "Dynamics arc is too predictable (additive bloom without surprise)"
- "No melodic hook — relies entirely on lyric hook; singability suffers"
- "Bridge is too short (4 lines) for the emotional weight it carries"

None of these can be addressed by "quoting a line" and "providing alternative lines." The SOP doesn't account for structural, arrangement, or production-level flags.

**Problem 2 (Rule: "Alternatives must be BETTER, not just different"):** This is good guidance but impossible to verify objectively. Better by whose standard? The writer's? The critic's? A clearer formulation: "Alternatives must solve the stated problem while maintaining the song's thesis and voice."

---

### Step 7 — Write 3 Priority Recommendations
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem:** The three slots are labeled: "1. The ONE change that would improve the song most, 2. The structural/pacing fix, 3. The polish-level improvement." But what if the biggest improvement IS structural? Or what if the song has no structural issues but three lyric-level problems? The labels are prescriptive about the TYPE of fix per slot, rather than just ordering by impact.

**Suggested fix:** Make all three "ordered by impact (biggest improvement first)" and drop the type labels. Or make them flexible: "1. Highest impact, 2. Second priority, 3. Third priority — at least one should address lyrics and one should address structure/arrangement."

---

### Step 8 — Save the Report
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Naming convention doesn't scale):** The examples show:
- `songs/album_act2/08_First_Blood.md` → `analysis/08_First_Blood_critique.md`
- `songs/experimental/The_Wound_Speaks.md` → `analysis/The_Wound_Speaks_critique.md`

For my song at `songs/keeper_of_the_light/01_The_Keepers_Morning.md`, the pattern drops the subdirectory. So the critique goes to `analysis/01_The_Keepers_Morning_critique.md`. But with multiple albums, BOTH might have a Track 01. This creates collisions. 

**Suggested fix:** Prefix with album identifier: `analysis/KOTL_01_The_Keepers_Morning_critique.md` or use subdirectories: `analysis/keeper_of_the_light/01_The_Keepers_Morning_critique.md`.

**Problem 2 (No mention of overwriting):** If the song gets revised and re-critiqued (as SOP 07 suggests), does the new critique overwrite the old one? Or do you version it (`_critique_v2.md`)? The SOP doesn't address re-critique scenarios.

---

### Step 9 — Format Output
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** The template shows "Flagged Issues" with numbered items containing "Current: 'the line'" — which again assumes lyric-level flags. The template should accommodate non-lyric flags.

---

## GENERAL ISSUES (Not Step-Specific)

### Issue A: No Guidance for Songs with Existing Self-Scores

The Keeper's Morning already has a "Quick Self-Score" section. SOP 02 never mentions this scenario. Should the critic:
- Acknowledge the self-score and note disagreements?
- Ignore it entirely (fresh eyes)?
- Use it as calibration (the SOP's Principles section says "Self-critiques inflate by ~1.0 point")?

The inflation rule in Principles is helpful but it's buried at the bottom. It should be referenced in Step 3 or as a pre-step: "If the song has a self-score, note it but do NOT let it anchor your assessment. Expect self-scores to inflate by ~1.0 point."

### Issue B: 9-Step Analysis Output Location

The 9-step analysis (Step 2) produces content that doesn't appear in the final output template (Step 9). Where does it go? Options:
1. It's internal scaffolding (don't save it) — if so, say that
2. It should appear in the report above the scores — if so, add it to the template
3. It informs the "Notes" column in the score table — if so, clarify that connection

### Issue C: No Album-Context Guidance

When critiquing a concept album track, certain categories need special handling:
- **Commercial (#8):** The song's "commercial" value is as PART of an album experience, not as a standalone. But the SOP only has one line about this ("Score relative to INTENDED context"). More specific: "For album tracks, Commercial assesses whether the track serves its position in the album's emotional arc, not standalone chart potential."
- **Arc (#4):** Does "arc" mean the song's internal arc or its contribution to the album's arc? Probably internal — but clarify.
- **Hook (#1):** "Arrives within 15s" — but concept album openers often have atmospheric intros. Same ambiguity flagged in SOP 01 stress test.

### Issue D: Time Estimate May Be Optimistic for Rich Songs

The SOP estimates 30-35 minutes. For a song as detailed as The Keeper's Morning (with production notes, album context, multiple motifs to assess), a thorough critique using the full rubric takes closer to 40-50 minutes. The time estimate might be calibrated for simpler standalone songs.

---

## RECOMMENDATIONS

### Priority 1 (Would eliminate most confusion)
1. **Add explicit cross-reference to CRITIQUE_REFERENCE.md in Step 3:** "Score using the rubric definitions in `references/CRITIQUE_REFERENCE.md`. The 1-10 scale meanings there are required for consistent scoring — do not guess at score boundaries."
2. **Move "Context rule" ABOVE the scoring table:** "⚠️ CONTEXT RULE: Score relative to the song's INTENDED context. A concept album track is scored against concept album standards, not radio singles. A folk ballad is scored against folk conventions, not pop hooks."
3. **Fix Step 6 to handle non-lyric flags:** Add guidance for flagging structural/production/arrangement issues where "alternative lines" don't apply.

### Priority 2 (Would improve flow)
4. **Clarify 9-step analysis destination:** Add note — "The 9-step analysis is your SCAFFOLDING. It doesn't appear verbatim in the output — it informs the one-sentence justification per score in Step 3."
5. **Fix Step 7 recommendation labels:** Change from prescriptive types to pure impact ordering with flexible categories.
6. **Fix naming convention for multi-album repos:** Add album prefix or subdirectory guidance.

### Priority 3 (Nice to have)
7. **Address self-score scenario:** Add a note about how to handle songs with existing self-scores.
8. **Address re-critique versioning:** What happens when a revised song gets critiqued again?
9. **Add album-context notes** for categories that behave differently for concept album tracks.
10. **Reconcile SOP 01 self-score rubric with SOP 02 critique rubric** — they should use the same 12 categories, or the disconnect should be documented.

---

## FINAL VERDICT

**SOP 02 is a solid A-.** The core workflow (absorb → analyze → score → flag → recommend) is sound and produces useful output. The issues are edge-case handling (concept albums, non-lyric flags, multi-album naming) and cross-SOP consistency (rubric mismatch with SOP 01). A user with access to CRITIQUE_REFERENCE.md and some common sense will produce a good critique. A user following ONLY the SOP text will miss scoring nuance.

**Time actually spent:** ~40 minutes (above the 30-35 minute estimate, because the song has rich production notes and album context to evaluate).

---

*Filed during Keeper of the Light stress test, SOP 02 critique of Track 01.*
