# Platform Generalization Implementation Plan

**Date:** 2026-06-09

**Status:** Completed — all steps below were implemented and tested on 2026-06-09.

This plan implements the first bounded migration from the review in `docs/RESEARCH_METHODOLOGY_REVIEW_AND_GENERALIZATION_PLAN.md`: preserve the current `.kiro/` automation adapter, while making the repository usable through platform-neutral docs, command-line checks, and auditable research records.

## Optimized execution steps

### ✅ Step 1 — Establish this implementation plan

**Work:** Add this file so the migration has an ordered plan with tests.

**Testing before completion:**
- Confirm this file exists.
- Confirm every implementation step below includes a testing requirement.
- Confirm the plan references the review that motivated it.

### ✅ Step 2 — Add platform support matrix

**Work:** Add `README_PLATFORM_SUPPORT.md` explaining which repo features require `.kiro/`, which can be used without platform automation, and which can be used manually.

**Testing before completion:**
- Confirm the matrix contains current-platform, non-platform, and manual-use columns.
- Confirm all referenced repo paths exist.
- Confirm README links to the matrix.

### ✅ Step 3 — Add platform-neutral core methodology summaries

**Work:** Add `core/methodology/` summary files for writing, critique, Suno optimization, concept-album continuity, and character voice. These are concise canonical summaries that point back to current detailed SOPs/references.

**Testing before completion:**
- Confirm every core methodology file exists.
- Confirm each file has Purpose, Canonical sources, Core workflow, and Testing/validation sections.
- Confirm every referenced source path exists.

### ✅ Step 4 — Add first deterministic validator

**Work:** Add `tools/count-suno-fields.py` to count Style Prompt and Lyrics field characters from song markdown and report OK/WARN/OVER against the repo's current limits.

**Testing before completion:**
- Confirm `--help` exits successfully.
- Run the validator against at least two existing songs.
- Run a known-over-limit fixture and confirm it fails.
- Run JSON output and confirm it parses.

### ✅ Step 5 — Add initial claim registry and bibliography

**Work:** Add `core/claims/claim-registry.yml` and `core/claims/source-bibliography.md` to seed evidence tracking for operational repo claims.

**Testing before completion:**
- Parse the YAML successfully.
- Confirm required fields are present on every claim.
- Confirm referenced repo files exist.
- Confirm bibliography IDs used by claims exist in the bibliography.

### ✅ Step 6 — Add Suno experiment harness template

**Work:** Add `experiments/suno/README.md` and `experiments/suno/TEMPLATE.yml` for model-versioned prompt/tag testing.

**Testing before completion:**
- Parse the template YAML successfully.
- Confirm the template contains model version, date, settings, prompt, lyrics, observations, and conclusion fields.
- Confirm the experiment README links back to the claim registry and Suno methodology.

### ✅ Step 7 — Final review and checks

**Work:** Review all new/changed files for consistency, run repository checks, commit, and create the PR.

**Testing before completion:**
- Run `git diff --check`.
- Run all step validation commands again.
- Confirm no unintended references to unrelated platforms were added.
- Confirm `git status --short` is clean after commit.
