# SOP 08 Stress Test Report

> **Test Context:** Following SOP 08 as a new user setting up the Keeper of the Light album as their own project, then attempting a contribution flow.
> **Scenario:** New user clones the repo, wants to work with the Keeper of the Light album, and later wants to contribute a new Suno tag finding back to the community.
> **Date:** Stress test completed following SOP 08 exactly as written.

---

## EXECUTIVE SUMMARY

**Overall Verdict:** SOP 08 is well-organized and covers the right topics (onboarding, customization, contribution). The main issues are staleness — the SOP was clearly written when only Fractured Shadows existed, and hasn't been updated to reflect the addition of Keeper of the Light content, additional hooks, or the `#[[file:]]` syntax. The contribution section is solid but could be more specific about WHERE contributions land (which file to edit). No blocking issues — a motivated user will succeed.

**Completion Status:** All steps followable. Issues are primarily outdated counts, missing references to newer content, and minor clarity gaps.

---

## STEP-BY-STEP EXPERIENCE

### Step 1 — Clone the Repo
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | None |
| Cross-reference needed | No |

**Notes:** Simple git clone. No issues.

---

### Step 2 — What You Get Immediately
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ OUTDATED |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (Hook count wrong):** SOP says "3 hooks (format-check, char-count, prosody-lint)" but the repo actually has 5 hooks:
1. `song-format-check.md` (universal)
2. `suno-char-count.md` (universal)
3. `prosody-lint.md` (universal)
4. `continuity-check.md` (album-specific — Fractured Shadows)
5. `keeper-continuity-check.md` (album-specific — Keeper of the Light)

The count should say "3 universal hooks + album-specific continuity hooks" or be updated to reflect reality.

---

### Step 3 — What You Should Customize
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ OUTDATED / INCOMPLETE |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1 (Missing Keeper of the Light references):** The customization table only mentions Fractured Shadows (`FRACTURED_SHADOWS_BIBLE.md`, `concept-album.md`). The repo now ALSO has:
- `references/KEEPER_OF_THE_LIGHT_BIBLE.md`
- `.kiro/steering/keeper-of-the-light.md`
- `.kiro/hooks/keeper-continuity-check.md`
- `songs/keeper_of_the_light/`

These aren't listed as "files to customize/replace." A new user setting up their OWN album wouldn't know these exist or what to do with them.

**Problem 2 (No hook customization mentioned):** The table covers steering, references, and songs — but not hooks. Album-specific hooks need to be replaced/deleted when setting up a new album. Add hooks to the customization table.

**Problem 3 (Example vs. active content unclear):** Are the Fractured Shadows and Keeper of the Light bibles "examples to learn from" or "active content to delete"? The instruction says "Replace with YOUR album bible" which implies delete — but they're valuable as format references. Clarify: "These are example bibles — keep them as format references until you've created your own, then optionally remove them."

---

### Step 4 — Create Your Preferences File
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem:** "Customize: What should Production Notes include? What's your preferred rhyme scheme?" — good questions, but no format guidance. Should answers be bullet points? Prose paragraphs? The note "use the existing file as a FORMAT template" would set expectations.

---

### Steps 5-7 — Set Up Album / Update Skills & Agents
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ MOSTLY CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Problem (Step 6 — `#[[file:]]` syntax unexplained):** "Change the `#[[file:...]]` reference" — assumes user knows what this syntax does. Add brief explanation: "The `#[[file:path]]` syntax is Kiro's file-reference system — it embeds the referenced file's content when the skill is activated."

---

### Contributing Back Section
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issues:**
1. "New Suno tag findings" in the What We Accept table doesn't specify the target file. Add: "→ goes to `references/SUNO_TAGS_REFERENCE.md`"
2. Verification step "no personal references in universal files" could be more actionable: "Search for your album name, character names, or personal details in universal files."

---

### File Organization Rules
| Aspect | Rating |
|---|---|
| Clarity | ⚠️ INCOMPLETE |
| Missing info | Moderate |
| Cross-reference needed | No |

**Problem 1:** The Universal files list includes only 3 hooks by name. Album-specific hooks (`continuity-check.md`, `keeper-continuity-check.md`) should be in the Personal files list.

**Problem 2:** The "Example: Starting From Scratch" bash script deletes Fractured Shadows content but NOT Keeper of the Light content. The script is outdated. A user following it literally would be left with KOTL files they might not want.

---

### FAQ
| Aspect | Rating |
|---|---|
| Clarity | ✅ CLEAR |
| Missing info | Minor |
| Cross-reference needed | No |

**Minor issue:** "Can I use this without Kiro IDE?" answer mentions agents/skills/hooks/powers as Kiro-specific — but doesn't mention that SOPs (`.kiro/sops/`) are also universal/tool-agnostic content. Add SOPs to the universal-content list.

---

## GENERAL ISSUES

### Issue A: Written Before Keeper of the Light Existed

The SOP references only Fractured Shadows as the example album. All customization instructions, file lists, and the "Starting From Scratch" script need updating to reflect that the repo now contains TWO example albums. This creates confusion about what to keep vs. delete.

### Issue B: No Explicit Hook Customization Path

Steering, agents, skills, and references all have customization guidance. Hooks don't. Album-specific hooks are a significant piece of the system (they enforce continuity rules) and new users need to know: (1) which hooks are universal, (2) which are album-specific and need replacing, (3) how to create their own album hook.

### Issue C: Contribution Target Files Not Specified

The "What We Accept" table says contributions are welcome but doesn't always specify WHERE the contribution goes (which file to edit). For Suno tag findings, knowledge base additions, etc., specifying the target file would reduce PR friction.

---

## RECOMMENDATIONS

### Priority 1 (Would eliminate most confusion)
1. **Update hook count and list:** Change "3 hooks" to "3 universal hooks (format-check, char-count, prosody-lint) + album-specific continuity hooks (one per album)."
2. **Update Step 3 customization table:** Add Keeper of the Light files, add hooks to the customization list, clarify that example bibles are format references.
3. **Update "Starting From Scratch" script:** Include Keeper of the Light cleanup alongside Fractured Shadows.

### Priority 2 (Would improve clarity)
4. **Add `#[[file:]]` syntax explanation** in Step 6.
5. **Specify contribution target files** in the What We Accept table.
6. **Add hooks to the Personal files list** in File Organization Rules.
7. **Add SOPs to the FAQ's "universal content" answer.**

### Priority 3 (Nice to have)
8. **Add format guidance to Step 4:** "Use the existing preferences file as a format template."
9. **Make verification more actionable:** "grep for your album/character names in universal files."
10. **Note in Step 3:** "These example files are valuable format references — keep as read-only examples until you've created your own."

---

## FINAL VERDICT

**SOP 08 is a solid B.** The structure and coverage are good — it addresses onboarding, customization, and contribution. The main issue is staleness: it was written for a single-album repo (Fractured Shadows only) and hasn't been updated for the multi-album reality (Keeper of the Light addition, extra hooks, expanded file structure). A new user will succeed but will encounter several "wait, this doesn't match what I'm seeing" moments. The fixes are mostly updates and additions rather than structural changes.

**Time to follow:** ~10 minutes for reading/planning (actual setup work would take 30-60 minutes depending on whether you're creating a new album or just customizing preferences).

---

*Filed during Keeper of the Light stress test, SOP 08 new-user onboarding simulation.*
