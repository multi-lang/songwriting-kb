# SOP 01 — Stress Test Notes

> Issues, confusions, and improvement suggestions encountered while writing Track 1: "The Keeper's Morning" for the Keeper of the Light album.

---

## Test Context

- **Song:** Track 01 — The Keeper's Morning
- **Album:** Keeper of the Light (8-track concept album)
- **SOP Version:** Current (as of stress test)
- **Tester:** AI (following all 27 steps exactly)

---

## Issues Encountered

### 1. Hook Timing Ambiguity (Step 8 & Step 18)

**Problem:** Step 8 says "hook must be within 15s of first vocal." Step 18 repeats this as a checklist item. But neither step clarifies:
- Does "first vocal" mean first sung word, or does a spoken intro count?
- If the intro is instrumental (as in this track), does the 15s clock start when the voice enters in V1?
- What counts as "the hook"? The hook LINE landing, or the hook PHRASE beginning?

**Impact:** I had to restructure my verse length to ensure compliance. The ambiguity made me second-guess whether a 4-line verse + 2-line pre-chorus was tight enough.

**Suggested Fix:** Add clarifying note: "15s from first sung lyric to the beginning of the hook phrase. Instrumental intros do not count against this clock."

---

### 2. Step 8 (Arrangement Design) vs Step 25 (Production Notes) Overlap

**Problem:** Step 8 asks for "growth pattern, negative space, contrast pairs, hook placement" — which is essentially an abbreviated version of what Step 25 requires in full (dynamics arc, instruments, etc.). This creates redundant work: you plan it in Step 8, then rewrite the same information more formally in Step 25.

**Impact:** Minor — just felt like I was doing the same work twice with slightly different formatting.

**Suggested Fix:** Either (a) make Step 8 explicitly a "sketch" that Step 25 formalizes, or (b) merge them and have Step 8 say "fill out the Production Notes template now — you'll paste it into the output in Step 25."

---

### 3. No Guidance on Intro Instrumentation (Step 16)

**Problem:** Step 16 says "Intro: 2-4 lines max, sets mood" — but for instrumental intros (very common in folk, cinematic, and concept-album openers), there's no guidance on how to notate this. Do you count instrumental bars? Write a description in parentheses? Skip the lyrics field for that section?

**Impact:** I improvised with a parenthetical description: `(sea-wash, 4 bars → concertina enters with keeper's melody)`. Works fine, but a newer user might not know what to do.

**Suggested Fix:** Add note: "For instrumental intros, write a brief parenthetical description of the arrangement. In the Suno-ready output, use the section tag with pipe notation alone: `[intro | atmospheric, warm, sparse]`"

---

### 4. Step 10 (Write Chorus First) — No Guidance on Hook Phrase vs Hook Line

**Problem:** Step 10 says "must contain the hook" but the KB distinguishes between hook types (lyric hook, melodic hook, rhythmic hook, production hook). The SOP doesn't tell you which type to target or how to mark it.

**Impact:** Low — I defaulted to lyric hook (declarative statement) which is the most common. But for tracks where the hook is a melodic concertina phrase or a production element (like the sea-wash), the instruction is unclear.

**Suggested Fix:** Add: "Identify your hook TYPE (lyric, melodic, rhythmic, or production) before writing. If lyric hook: it must be in the chorus. If melodic/production hook: the chorus must still contain the emotional peak even if the hook is instrumental."

---

### 5. Step 22 (Global Meta-Tags) — [track] Length vs Song Reality

**Problem:** Step 22 says to add `[track: ... length: XXX]` but at this point in the SOP, you haven't calculated actual runtime yet. You're estimating. The SOP doesn't tell you HOW to estimate runtime from BPM + line count.

**Impact:** I guessed 225 seconds based on 92 BPM × typical section durations. Could be off by 20-30 seconds.

**Suggested Fix:** Add a quick formula: "Estimate runtime: (total lyric lines × 60/BPM × 2) + intro bars + outro bars. At 92 BPM, each line ≈ 2.6s with breath. Typical: 20 lines + intro/outro ≈ 3:00-4:00."

---

### 6. Step 27 (Continuity Check) — No Template for T1

**Problem:** Step 27's checklist asks about "callbacks reference correct source tracks" and "vocal texture different from adjacent tracks" — but for Track 1 of an album, there ARE no previous tracks to callback to, and "adjacent" only means forward (T2). The checklist items feel designed for mid-album tracks.

**Impact:** Minor — I just noted "N/A, this is T1" for some items. But it reads like an incomplete pass.

**Suggested Fix:** Add conditional: "For Track 1: focus on establishing motifs correctly, setting up future callbacks, and verifying no forbidden elements are present. Adjacency check is forward-only (does T2's planned palette differ sufficiently?)."

---

### 7. Phase Order — Writing Pre-Chorus Before Verse Feels Backwards

**Problem:** Step 11 says write pre-chorus BEFORE Verse 1 (Step 12). The Nashville Method rationale makes sense (work backward from the chorus). But in practice, I needed to know what V1 established before I could write a pre-chorus that "builds into" the chorus FROM the verse's world.

**Impact:** I actually wrote V1 first, then the pre-chorus, then just documented them in SOP order. The SOP order is theoretically correct but practically awkward for narrative songs where V1 sets the scene.

**Suggested Fix:** Add note: "For narrative/story songs, you may find it easier to sketch V1's TOPIC before writing the pre-chorus, then return to polish V1 after. The key principle: the chorus is your destination — everything else serves it."

---

### 8. Missing Step: "Test the Motif Phrase"

**Problem:** For concept albums with recurring phrases (like "the light keeps"), there's no step that says "verify your recurring phrase works in all its future contexts." I had to mentally check that "the light keeps ships from harm" (pride) can naturally evolve to "what does the light keep?" (question) in T3, "the light keeps— the light keeps—" (panic) in T5, and "the light keeps it dreaming" (truth) in T8.

**Impact:** If I'd written a phrase that only worked in ONE meaning, I'd have to rewrite later.

**Suggested Fix:** Add to Step 27 or as a sub-step: "If this track introduces a recurring phrase, test it forward: write out ALL planned future uses and verify the phrase is flexible enough to carry each meaning."

---

## Overall Assessment of SOP 01

**Strengths:**
- The Nashville Method order (chorus first) is excellent — forces clarity
- Phase 1 analysis prevents "writing without a thesis" syndrome
- Quality gates in Phase 3 catch real problems
- The Phase 4 formatting steps produce genuinely Suno-ready output

**Weaknesses:**
- Some redundancy between planning (Phase 1) and documentation (Phase 4)
- Assumes mid-album position in Step 27 — needs T1/T8 edge cases
- No runtime estimation guidance
- Hook timing definition needs tightening

**Verdict:** SOP 01 works well for its purpose. The 27 steps are thorough without being paralyzing. Main issues are edge-case clarity (first/last tracks, instrumental intros, recurring-phrase validation) rather than structural problems.

---

*Filed during Keeper of the Light stress test, Track 01.*
