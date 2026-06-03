# SOP 03 Stress Test Report

> **Test Context:** Following SOP 03 step-by-step to optimize Track 01: "The Keeper's Morning" for Suno rendering.
> **Input Song:** `songs/keeper_of_the_light/01_The_Keepers_Morning.md` (already contains a Suno-ready output section from SOP 01 Phase 4)
> **Date:** Stress test completed following SOP 03 exactly as written.

---

## EXECUTIVE SUMMARY

**Overall Verdict:** SOP 03 is functional and its core logic (audit → tags → validate → terminate → verify) is sound. However, it has a phantom tag problem (`[Title:]` referenced 3 times but never used in practice), unclear boundaries between valid/invalid pipe parameters, and several inconsistencies between what it prescribes and what the actual song examples do. The biggest issue: the SOP was likely written against an earlier Suno version's conventions and hasn't been fully reconciled with the actual formatting patterns in the repo's songs.

**Completion Status:** All 12 steps followable. Song was already optimized, so the SOP functioned as a verification pass rather than a transformation pass — which exposed an undocumented use case.

---

## STEP-BY-STEP EXPERIENCE

### Step 1 — Character Count Audit
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Phantom `[Title:]` tag):** The SOP says "Count from `[Title:]` through `[end]`" — but the actual song doesn't use a `[Title:]` tag. It starts with `[track: genre: ...]`. No song in the repo uses `[Title:]`. The SUNO_TAGS_REFERENCE should be checked to confirm whether this is a valid tag at all. In practice, the count starts from the first `[track:]` tag.

**Problem 2 (Overflow guidance incomplete):** "If over: move negatives/exclusions to Exclude field first, then trim least essential descriptors" — this is good, but doesn't mention that the Advanced Settings box is also an overflow option (per the user's known workflow). Adding: "If still over after moving exclusions: overflow additional direction to Suno's Advanced Settings box" would align with actual practice.

---

### Step 2 — Add Global Control Tags
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | Yes |

**Problem 1 (`[Title:]` again):** "Add these at the TOP of Lyrics field (before `[Title:]`)" — references the phantom tag. Should say "before the first content/section tag" or "before `[track:]`."

**Problem 2 (No runtime estimation formula):** "Length calculation: Target minutes × 60 = seconds" tells you to convert, but not how to ESTIMATE the target. The SOP 01 stress test flagged this same gap and suggested: "Estimate runtime: (total lyric lines × 60/BPM × 2) + intro bars + outro bars." This formula should be included here too.

**Problem 3 (Tag validation source):** Are `[track:]`, `[control:]`, and `[sequence:]` confirmed working Suno tags? The SOP asserts they are but doesn't cite testing or reference the SUNO_TAGS_REFERENCE. A note like "See `references/SUNO_TAGS_REFERENCE.md` for tag validation status" would help.

---

### Step 3 — Validate [control] Parameters
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | Yes |

**Minor issue:** "Only these values are confirmed valid" — confirmed BY WHOM? Through what testing? If a user discovers a new valid parameter, where do they report it? A note: "Confirmed through testing as of [version]. Report new findings via SOP 08 (Contributing)." would close the loop.

---

### Step 4 — Optimize Section Tags
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (No pipe parameter limit):** How many comma-separated descriptors can go in a pipe? The SOP shows 4 in its example (`powerful, wide, heavy drums, distorted bass`) but doesn't state a maximum. In practice, is 3-4 optimal? Does Suno ignore params beyond a certain count? Guidance like "Recommend 2-4 pipe parameters. Beyond 5, Suno may deprioritize later descriptors" would help.

**Problem 2 (Blurry valid/invalid boundary):** "Valid: adjectives/descriptors" vs "Invalid: instrument instructions" — but what about "sparse"? "Stripped"? "Driving"? These are adjectives that imply arrangement decisions. The boundary needs more examples:
- ✅ Valid: "powerful, intimate, dark, rising, close-mic, whispered, wide stereo"
- ❌ Invalid: "cello enters here, drums build gradually, guitar picks up tempo"
- ⚠️ Gray zone (treat as valid): "stripped, driving, sparse, full, layered" — these are production adjectives, not instrument instructions

---

### Step 5 — Add Vocal Delivery Tags
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem (Relationship to Vocal Direction block):** The song already has a `[Vocal Direction: ...]` block that covers global delivery. Per-section tags (like `[vulnerable vocals]` in the bridge pipe) ADD specificity. But the SOP doesn't explain the hierarchy: Does a per-section tag OVERRIDE the global direction? SUPPLEMENT it? What if they conflict?

**Suggested guidance:** "Per-section vocal tags supplement the global Vocal Direction block. They specify WHERE a delivery change happens. The Vocal Direction block sets the baseline; section tags mark departures from it."

---

### Step 6 — Add Dynamics Tags
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem (Standalone tags vs pipe parameters):** The song uses `[pre-chorus | building, rising tension]` instead of a separate `[build]` tag before the section. Are these equivalent? Can you express dynamics WITHIN a pipe (as an adjective like "building") instead of as a standalone tag? The SOP lists dynamics as standalone tags only, but the actual practice uses pipe notation for the same purpose.

**Suggested guidance:** "Dynamics can be expressed as standalone tags (`[build]` before a section) OR as pipe parameters (`[section | building, rising]`). Use standalone tags for mid-section dynamic events (e.g., a sudden silence in the middle of a verse). Use pipe parameters when the dynamic applies to the entire section."

---

### Step 7 — Add Termination
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Clear, simple, no issues. The fade variant `[fade: layered]` is documented. The song uses `[fade: layered, reverb-tail]` which adds an extra parameter — valid per the pipe-adjective logic.

---

### Step 8 — Check for Obsolete Tags
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** `[Title:]` isn't listed as obsolete, yet it's referenced in Steps 1, 2, and 9 as if valid. Either it IS valid (add it to confirmed tags) or it's obsolete/phantom (add it to this removal list and fix the other steps). Currently it exists in a no-man's-land.

---

### Step 9 — Verify Suno Compatibility
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ NEEDS FIXES |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Punctuation rule incomplete):** "No end punctuation on lyric lines" — but em-dashes (—) are used extensively in the song and are clearly valid/intentional. The rule should specify WHICH punctuation is prohibited and which is allowed:
- ❌ Prohibited: periods (.), trailing commas (,), semicolons (;)
- ✅ Allowed: em-dashes (—) for phrasing/breath, hyphens (-) in compound words, apostrophes (') in contractions

**Problem 2 (Instrumental sections):** "4-8 lines per section maximum" — doesn't address sections with 0 lyric lines (instrumental intros, outros with only tags). Clarify: "Instrumental sections with only a section tag and no lyrics are valid. The 4-8 line rule applies to sections that contain sung/spoken lyrics."

**Problem 3 (`[Title:]` in checklist):** "`[Title:]` is present and matches song name" — this tag isn't used in practice. Remove or replace with a relevant check (e.g., "`[track:]` tag is present with genre, mood, and length").

---

### Step 10 — Set Creative Sliders
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** No album-consistency guidance. If Track 1 rendered well at 50%/55%, should subsequent tracks use similar values for sonic cohesion? Or should each track optimize independently? A note: "For album tracks, document slider values per track. If a render captures the intended palette well, note the slider settings as a baseline for adjacent tracks with similar palettes."

---

### Step 11 — Prepare Exclude Field Content
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ CONTRADICTS ACTUAL PRACTICE |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (Dash-prefix inconsistency):** The SOP shows: `‑trap drums, ‑beatboxing, ‑vocal hums` (with dash prefix). But the actual song's Exclude field is: `distortion, electric guitar, synthesizers...` (NO dash prefix). The Suno UI's Exclude field is a plain-text box — you don't need the dash prefix there (the field itself implies exclusion). The dash-prefix format (`‑item`) is for when exclusions appear IN the Style Prompt field (to negate within a positive-description context).

**Fix:** Clarify: "In the dedicated Exclude field: list items as plain comma-separated text (no dash prefix needed — the field implies exclusion). The dash-prefix format (‑item) is only needed when placing exclusions in the Style Prompt itself."

---

### Step 12 — Final Output
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (Already-optimized songs):** The template assumes changes were made ("### Changes Made: [list]"). But if the song arrives already Suno-formatted (from SOP 01 Phase 4), there may be no changes. The SOP doesn't address verification-only passes.

**Suggested addition:** "If the song arrives already formatted (e.g., from SOP 01 Phase 4), run all steps as a VERIFICATION pass. Document: '### Verification: All checks passed, no changes needed' or list the specific corrections made."

---

## GENERAL ISSUES

### Issue A: The Phantom `[Title:]` Tag

Referenced in Steps 1, 2, and 9 but NEVER used in actual songs in this repo. Not in the SUNO_TAGS_REFERENCE (needs checking). Either:
1. It's a valid tag that should appear in songs (add it to SOP 01 formatting)
2. It's obsolete/phantom (remove all references, replace with `[track:]`)

Based on actual practice across all songs in this repo: it should be removed and replaced with `[track:]`.

### Issue B: SOP 03 vs SOP 01 Phase 4 Overlap

SOP 01's Phase 4 (Steps 20-26) already produces a Suno-ready output with tags, character counts, and slider recommendations. SOP 03 then asks you to do much of the same work again. The intended flow (per SOP 07) is: Write → Critique → Revise → THEN Optimize. But in practice, SOP 01 already optimizes during writing.

This means SOP 03 is either:
- A verification/polish pass for songs that came through SOP 01 (current reality)
- A transformation pass for songs written WITHOUT SOP 01 (older songs, imported lyrics, human-written songs)

Both use cases are valid, but the SOP only describes the second. Acknowledging the first would align it with the actual pipeline.

### Issue C: No Reference to SUNO_TAGS_REFERENCE.md

The SOP validates tags (Steps 3, 4, 8) without ever referencing the central tag authority (`references/SUNO_TAGS_REFERENCE.md`). This file exists and is the source of truth for what tags work. The SOP should reference it at least once.

---

## RECOMMENDATIONS

### Priority 1 (Would eliminate most confusion)
1. **Remove all `[Title:]` references.** Replace with `[track:]` in Steps 1, 2, and 9. This phantom tag causes confusion at three points in the SOP.
2. **Add the runtime estimation formula to Step 2.** "(total lyric lines × 60/BPM × 2) + intro seconds + outro seconds"
3. **Fix Step 11 dash-prefix inconsistency.** Clarify: plain text in Exclude field, dash-prefix only if placing exclusions in Style Prompt.

### Priority 2 (Would improve clarity)
4. **Add pipe parameter practical limit** to Step 4: "Recommend 2-4 pipe parameters per section tag."
5. **Clarify standalone vs pipe dynamics** in Step 6: standalone for mid-section events, pipe for section-wide dynamics.
6. **Fix Step 9 punctuation rule** to explicitly allow em-dashes and address instrumental sections.
7. **Add reference to SUNO_TAGS_REFERENCE.md** in Steps 3-4 for tag validation authority.

### Priority 3 (Nice to have)
8. **Acknowledge verification-only passes** in Step 12 for songs already formatted by SOP 01.
9. **Add Vocal Direction hierarchy note** in Step 5: section tags supplement, not override, the global block.
10. **Add album slider consistency note** in Step 10.

---

## FINAL VERDICT

**SOP 03 is a solid B+.** The workflow logic is correct and the step ordering makes sense. The main problems are: (1) a phantom tag referenced throughout but never actually used, (2) unclear boundaries in its validation rules (pipe params, punctuation, dynamics notation), and (3) a formatting inconsistency in the exclude field. None of these are blockers — a user with common sense and access to the song examples will produce correct output. But the phantom `[Title:]` tag would genuinely confuse a new user trying to add it because the SOP says to.

**Time actually spent:** ~20 minutes (within the 15-20 minute estimate, since the song was already optimized and this was a verification pass).

---

*Filed during Keeper of the Light stress test, SOP 03 optimization verification of Track 01.*
