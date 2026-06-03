# SOP 07 Stress Test Report

> **Test Context:** Tracing the full pipeline (Write → Critique → Revise → Optimize → Verify → Render) with Track 01: "The Keeper's Morning" from Keeper of the Light.
> **Input:** Complete song file at `songs/keeper_of_the_light/01_The_Keepers_Morning.md` + album bible
> **Date:** Stress test completed by walking through all 6 stages and checking logic/handoffs.

---

## EXECUTIVE SUMMARY

**Overall Verdict:** SOP 07 is a well-structured orchestration document. The flowchart, decision gates, and stage definitions are clear. The main issues are: (1) stages 3 and 5 define procedures inline that probably deserve their own SOPs (or at minimum, cross-references), (2) the pipeline doesn't acknowledge that SOP 01 already produces fully-formatted output (making Stage 4 a verification pass), (3) there's no escape hatch for conflicts between critique recommendations and album continuity rules, and (4) the rubric mismatch between SOP 01's self-score and SOP 02's critique score creates ambiguity at the decision gate.

**Completion Status:** Full pipeline traceable from start to end. No blocking issues — all stages can be executed. Issues are about clarity, acknowledgment of actual workflow, and edge-case handling.

---

## STAGE-BY-STAGE EXPERIENCE

### Stage 1: WRITE (SOP 01)
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem:** Exit criterion "Basic Suno format applied" undersells SOP 01's Phase 4, which produces FULL Suno formatting (all tags, character counts, sliders, exclude field). This creates confusion with Stage 4: if SOP 01 already fully formats, what does Stage 4 add? Either (a) change "basic" to "full" and note Stage 4 becomes verification, or (b) actually mean "basic" and explain that SOP 01 should only apply preliminary formatting, with Stage 4 doing the full pass.

**Recommendation:** Align with reality — SOP 01 produces full formatting. Stage 4 is verification/polish.

---

### Stage 2: CRITIQUE (SOP 02)
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Rubric ambiguity at decision gate):** The song arrives with a self-score (8.3/10 from SOP 01's rubric). The pipeline's decision gate uses the SOP 02 critique composite. But SOP 01 and SOP 02 use DIFFERENT 12-category rubrics. The pipeline should explicitly state: "The decision gate uses the SOP 02 CRITIQUE composite score. Self-scores from SOP 01 are for the writer's reference only — they do not drive pipeline decisions."

**Problem 2 (Report naming):** Exit criterion references `analysis/[song-filename]_critique.md` — should note multi-album prefix convention from updated SOP 02 (e.g., `analysis/KOTL_01_The_Keepers_Morning_critique.md`).

---

### Stage 3: REVISE
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (No standalone SOP):** This is the only pipeline stage without its own SOP. The revision procedure exists ONLY here. If someone wants to revise a song without running the full pipeline (e.g., they received informal feedback), they'd need to find this pipeline SOP and extract Stage 3. Consider noting: "This revision process is defined here rather than in a standalone SOP because revision always requires a critique as input."

**Problem 2 (Re-critique guidance):** "Optional: Run through Critique again" — when to do this vs. not? If the goal is reaching ≥8.5 or confirming improvement, it seems mandatory rather than optional. Suggested: "Recommended for songs targeting ≥8.5 or when revisions were structural. Optional for polish-only fixes where the original score was already in the 8.0-8.4 range."

---

### Stage 4: OPTIMIZE (SOP 03)
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (Verification vs. Transformation):** For songs written with SOP 01 (which is EVERY song in this pipeline), Stage 4 is primarily a verification pass. The song arrives already formatted. The pipeline describes it as if transformative work happens here. Add a note: "For songs written with SOP 01 (which includes Phase 4 Suno formatting), this stage functions as VERIFICATION. Run all SOP 03 checks to confirm compliance and catch any formatting that was disrupted during revision (Stage 3)."

---

### Stage 5: VERIFY (Album tracks only)
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ NEEDS IMPROVEMENT |
| Missing info | Significant |
| Cross-reference needed | Yes — bible, but which section? |

**Problem 1 (No standalone SOP):** Like Stage 3, this is inline-only. Album verification is important enough (and reusable enough) to warrant at minimum a clear statement of authority: "Verify against the Album Bible (`references/[ALBUM]_BIBLE.md`). The bible is the single source of truth for all continuity checks."

**Problem 2 (No conflict resolution):** What happens when critique recommendations conflict with album continuity rules? Example: Critique says "add harmony vocals for emotional impact in the bridge" but Rule 7 says "keeper sings alone until Track 7." The pipeline has no escape hatch.

**Suggested addition:** "If continuity rules conflict with critique recommendations: continuity rules always win. Adjust the revision to achieve the critique's INTENT through means that don't violate album rules. Document the conflict and resolution in the critique report."

**Problem 3 (Authority unclear):** "Check sonic palette compliance" — against the bible or the steering file? They should be identical, but specify: "All verification checks reference the Album Bible as the source of truth."

---

### Stage 6: RENDER
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** Step 7 says "Evaluate renders against the Production Notes vision" — a practical note about keeping Production Notes visible during evaluation would help real-world usage.

---

## GENERAL ISSUES

### Issue A: Two Stages Without SOPs

Stages 3 (Revise) and 5 (Verify) define procedures inline. Every other stage references a standalone SOP. This means:
- The revision process can't be invoked independently
- The verification process can't be invoked independently
- Both processes are only discoverable inside this pipeline document

This is a design choice (keeps them in context), but it limits reusability.

### Issue B: SOP 01 Already Does Stage 4's Work

The pipeline describes 6 sequential stages, but in practice, Stage 4 is largely redundant for songs that came through SOP 01. The pipeline should acknowledge this reality rather than implying fresh optimization work at Stage 4.

### Issue C: Decision Gate Score Source Unclear

The decision gate uses a composite score, but the pipeline never explicitly says WHICH rubric/scoring system produces it. With two different rubrics in the system (SOP 01 self-score vs. SOP 02 critique score), this needs explicit declaration.

### Issue D: Time Estimate Arithmetic

The summary says "2-3 hours" but the component times sum to 2:10-3:15. Minor, but the low end should be ~2.25 hours, not 2.

---

## RECOMMENDATIONS

### Priority 1 (Would eliminate most confusion)
1. **Clarify decision gate score source:** Add explicit note that the SOP 02 critique composite drives the gate, not SOP 01 self-scores.
2. **Add conflict resolution rule for Stage 5:** "Continuity rules always win over critique recommendations. Achieve the critique's intent through rule-compliant means."
3. **Acknowledge Stage 4 as verification:** For SOP 01-origin songs, note that Stage 4 primarily verifies/catches regression rather than transforms.

### Priority 2 (Would improve flow)
4. **Fix Stage 1 exit criterion:** Change "Basic Suno format applied" to "Suno format applied (full formatting from SOP 01 Phase 4)" to align with reality.
5. **Clarify re-critique guidance in Stage 3:** When it's recommended vs. truly optional.
6. **Specify verification authority in Stage 5:** "All checks reference the Album Bible as single source of truth."
7. **Fix time estimate:** "2.25-3.25 hours" or keep "2-3 hours" with "(approximate)" qualifier.

### Priority 3 (Nice to have)
8. **Note Stage 3's intentional inline design:** "Revision is defined here (not as a standalone SOP) because it requires critique output as input."
9. **Add "verification pass" to When to Skip table:** "Song already formatted from SOP 01 → Stage 4 is verification (still run, expect minimal changes)."
10. **Add practical render note:** "Keep Production Notes visible during render evaluation — they're your quality benchmark."

---

## FINAL VERDICT

**SOP 07 is a solid B+.** As an orchestration document, it does its job: defines the flow, assigns responsibilities, sets decision gates, and gives time estimates. The issues are about alignment with how the sub-SOPs actually work now (SOP 01 producing full formatting, SOP 02 using a different rubric than SOP 01's self-score) and missing edge-case handling (continuity vs. critique conflicts). The flowchart and stage structure are well-designed and easy to follow. A user running the full pipeline for the first time would succeed — they'd just hit a few "wait, didn't I already do this?" moments at Stage 4.

**Time to trace (not execute) the full pipeline:** ~20 minutes for review. Actual execution would be 2-3+ hours per song.

---

*Filed during Keeper of the Light stress test, SOP 07 full pipeline trace with Track 01.*
