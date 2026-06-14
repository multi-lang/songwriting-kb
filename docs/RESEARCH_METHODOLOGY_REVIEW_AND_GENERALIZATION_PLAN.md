# Research Methodology Review and Platform Generalization Plan

**Date:** 2026-06-09  
**Scope reviewed:** top-level knowledge-base documents, `.kiro/` agents/skills/hooks/SOPs/power files, references, examples, songs, and analysis outputs.  
**User question addressed:** evaluate the repository's stated research and production methodologies, identify problems, recommend improvements, and plan whether the repository should continue relying exclusively on the current `.kiro/` platform configuration or be generalized for broader use.

---

## Executive conclusion

This repository contains a strong creative-production methodology: it combines a 9-step prewriting analysis, Nashville-style chorus-first drafting, prosody and structure quality gates, a layered critique rubric, Suno optimization, and concept-album continuity controls. The best parts of the system are the repeatable workflow design, the separation between steering/agents/skills/SOPs, the existence of example outputs, and the explicit quality gates for prosody, hook timing, verse progression, bridge turns, character voice, and album continuity.

However, the repository is not yet a rigorous research methodology in the academic or empirical sense. It has many named theoretical sources and practical claims, but it lacks a claim registry, inline citations, test logs, versioned Suno experiments, inter-rater calibration, reproducible validators, and a clear distinction between evidence-backed findings, craft heuristics, personal preferences, and platform-specific prompt lore. The most important improvement is therefore not simply to add more theory; it is to make every actionable rule traceable, testable, and portable.

The platform recommendation is: **do not keep the repository exclusively dependent on the current `.kiro/` platform configuration. Keep that platform as the best-supported first-class adapter for the current repo, but move the canonical methodology into platform-neutral core files.** The current `.kiro/` setup is worth retaining because the repo is already built around its steering, agents, hooks, skills, and powers. The problem is exclusivity: the methodology should be usable even when those platform-specific automation features are unavailable.

---

## Evidence base used for this review

### Internal repository evidence

- Top-level onboarding and architecture: `README.md`, `.kiro/README.md`, `WORKFLOW_DIAGRAM.md`.
- Core knowledge and theory: `SONGWRITING_KNOWLEDGE_BASE.md`, `MUSIC_PRODUCTION_THEORY.md`.
- Operational procedures: `.kiro/sops/*.md`.
- Agent and skill prompts: `.kiro/agents/*.md`, `.kiro/skills/*/SKILL.md`, `.kiro/powers/songwriting/POWER.md`.
- Automated checks: `.kiro/hooks/*.hook.json` and `.kiro/settings/settings.json`.
- Reference templates and bibles: `references/*.md`, `examples/**/*.md`.
- Outputs and analysis artifacts: `songs/**/*.md`, `analysis/**/*.md`.

### Current external platform checks

The platform findings below use current public documentation checked on 2026-06-09:

- Kiro docs say Kiro is an agentic IDE with specs, steering, hooks, agentic chat, MCP servers, and privacy controls: <https://kiro.dev/docs/>.
- Kiro skills use progressive disclosure: startup loads skill metadata, activation loads full instructions, and execution loads scripts/reference files as needed: <https://kiro.dev/docs/skills/>.
- Kiro powers dynamically load specialized knowledge and MCP tools when task keywords match: <https://kiro.dev/docs/powers/>.
- Kiro's February 2026 changelog added custom subagents, Agent Skills, and pre/post tool-use hooks: <https://kiro.dev/changelog/ide/0-9/>.
- Suno announced v5.5 on 2026-03-26 with Voices, Custom Models, and My Taste: <https://suno.com/blog/v5-5>.

---

## What the repository's methodology currently is

### 1. Song creation methodology

The writing process is a structured professional workflow rather than a blank-page prompt. It starts by defining a song thesis, then asks for semantic, emotional, prosodic, narrative, voice, genre, arrangement, production, and commercial analysis before drafting. The core writing sequence is Nashville-inspired: write the chorus first, use the pre-chorus to build tension, write V1 as setup, V2 as new information, bridge as the turn, and final chorus as variation.

**Strengths**

- Good anti-generic safeguards: thesis first, physical detail, V2-new-information rule, bridge-turn rule, and no filler.
- Prosody is treated as a prewriting and revision concern, not only a final lint pass.
- The method separates analysis, drafting, QA, formatting, and documentation.
- It supports album tracks, standalone songs, and experiments.

**Weaknesses**

- The method does not yet distinguish required gates from optional craft preferences in a machine-readable way.
- The chorus-first approach is treated as the default universal method even though some genres and narrative forms may benefit from beat-first, title-first, groove-first, top-line-first, or improvisational workflows.
- Runtime estimation and syllable limits are heuristics, but they are often presented as fixed rules.
- There is no empirical log tying these rules to successful renders or listener outcomes.

### 2. Critique methodology

The critique methodology uses a multi-layer framework: core 12-category scoring, advanced production/semiotic assessments, album-context checks, Suno optimization, and calibration/technical audit. This is conceptually strong because it avoids reducing a song to lyrics alone.

**Strengths**

- The 12-category model covers lyric, structural, vocal, emotional, commercial, genre, and arrangement concerns.
- The advanced layer introduces production-as-meaning, proxemic distance, functional layers, musemic interpretation, scope of vision, and skip-test realism.
- The album module recognizes that a song can be good in isolation but wrong for the story sequence.
- The full pipeline uses critique scores as decision gates, which creates operational discipline.

**Weaknesses**

- Scoring anchors are insufficiently calibrated. A `7`, `8.5`, and `9.5` need concrete exemplars and failure modes by category.
- Composite scoring appears to be simple averaging unless otherwise specified; that may overweight easy-to-score categories and underweight showstopper failures.
- There is no inter-rater reliability process, blind review protocol, or calibration set.
- The critic is asked to perform many interpretive tasks at once, which increases inconsistency unless outputs are decomposed and validated.
- The repository keeps critique reports, but it does not yet mine them into a quantitative improvement dashboard.

### 3. Suno optimization methodology

The Suno methodology organizes style prompts, lyric-field tags, exclusions, section tags, character limits, sliders, v5/v5.5 features, and render-stage guidance.

**Strengths**

- It enforces practical constraints: style prompt length, lyrics length, section tags on their own lines, and avoid negative prompts in the wrong field.
- It treats prompt specificity as a multi-dimensional system: genre, emotion, key, BPM, instruments, production space, and vocal delivery.
- It includes troubleshooting for repetition, drift, endings, section confusion, and voice assignment.
- It recognizes that v5.5 Voices, Custom Models, and My Taste are UI/model features, not necessarily text tags.

**Weaknesses**

- Suno claims are mixed across v4.5, v5.0, and v5.5 with uneven version dating.
- Several “confirmed” tag claims need a reproducible test matrix with prompt, model version, slider settings, seed/variation where available, observed output, and date.
- Some advice is likely model-version-sensitive and should expire or require revalidation.
- The methodology needs a render audit loop: prompt → generation settings → output evaluation → revision decision → retained evidence.
- Legal/ethical guidance for Voices, custom models, reference artists, and generated output disclosure is underdeveloped for a professional workflow.

### 4. Concept-album continuity methodology

The album methodology uses bibles, track registries, hard rules, motifs, callbacks, sonic palettes, character voices, key relationships, and continuity hooks.

**Strengths**

- The bible/steering/hook triad is a sound information architecture.
- Track-position requirements prevent “good song, wrong moment” failures.
- Character-voice and sonic-palette controls are especially useful for AI-generated music, where consistency can drift.
- Examples demonstrate how to instantiate the method.

**Weaknesses**

- Album-specific rules are not abstracted into a neutral schema; they live mostly as prose and prompts.
- There is no machine-readable continuity registry for track IDs, motifs, characters, keys, callbacks, prohibited phrases, and sonic palettes.
- The active album-continuity agent still points at `references/YOUR_ALBUM_BIBLE.md`, which is a placeholder rather than an enforceable canonical source for a real album.
- “Hard rules” are not separated into severity levels such as fatal, warning, informational, and intentional exception.

### 5. Platform methodology

The repository's active automation is currently Kiro-shaped: `.kiro/steering`, `.kiro/agents`, `.kiro/skills`, `.kiro/hooks`, `.kiro/powers`, and `.kiro/sops`. The content is often tool-agnostic, but the loading and automation model is not.

**Strengths**

- Kiro is a natural fit for the existing architecture because it currently supports steering, hooks, agents, skills, powers, and MCP-related dynamic loading.
- The hidden `.kiro/` directory keeps operational prompts organized.
- Skills and references use progressive disclosure, which is appropriate for a large knowledge base.

**Weaknesses**

- Users outside Kiro cannot easily tell what is canonical versus Kiro adapter material.
- Hook automation is LLM-prompt-based instead of deterministic for checks like character counts and required sections.
- The README promises auto-configuration through `.kiro/`, which creates immediate platform lock-in.
- Users outside the current platform cannot easily tell which parts are still usable without `.kiro/` automation.
- There is no platform support matrix that says which features are core repo methodology, which require the current `.kiro/` automation, and which can be used manually.

---

## Major problems identified

| Severity | Problem | Why it matters | Recommended fix |
|---|---|---|---|
| High | Evidence is not traceable at claim level | Users cannot distinguish sourced research, tested Suno behavior, expert heuristic, and preference | Add a claim registry with source, confidence, version, date verified, and affected files |
| High | Suno version drift | Prompt/tag behavior can change monthly; repo mixes v4.5/v5.0/v5.5 language | Add a model-version matrix and revalidation cadence |
| High | Deterministic checks are delegated to an LLM | Character counts, required sections, and section-tag rules should not vary by agent interpretation | Add scripts for char counts, format validation, tag validation, and continuity schema checks |
| High | Platform lock-in | `.kiro/` is excellent for Kiro users but obscures general use | Move canonical methodology to platform-neutral `core/` or `methodology/`; keep `.kiro/` as adapter |
| High | Calibration gap in scoring | Scores drive pipeline decisions but lack reliability controls | Add score anchors, calibration examples, multi-rater protocol, and optional weighted gates |
| Medium | Personal/example material leaks into universal docs | New users may inherit one user's preferences or album assumptions | Separate `core/`, `examples/`, `personal/`, and `adapters/` clearly |
| Medium | Platform-specific files are not labeled as adapters | New users may mistake `.kiro/` automation for the methodology itself | Label the current platform files as an adapter and move canonical rules into platform-neutral core docs |
| Medium | Legal/ethical risks under-specified | Voice cloning, custom models, reference artists, and distribution create non-craft risks | Add rights/ethics checklist and disclosure policy |
| Medium | Hooks count and feature descriptions are inconsistent | README and `.kiro/README.md` describe “3 universal hooks” while five hook JSON files exist | Normalize docs and add a generated inventory check |
| Medium | Album continuity is prose-first | Prose rules are harder to validate consistently | Add machine-readable album schema and compile prompts/hooks from it |
| Low | Time estimates are precise without measurement basis | 35-55 min and 50-75 min look empirical but may be anecdotal | Mark as estimates or collect workflow duration data |
| Low | Some markdown headings and output formats vary across songs | Inconsistent examples weaken validators and teaching value | Add canonical templates and migrate examples gradually |

---

## Explanation of each recommendation

This section expands the recommendations so they are actionable for this repository, not generic platform advice.

### Recommendation 1 — Do not keep the current platform as the exclusive way to use the repo

**What it means:** Keep the current `.kiro/` directory working, but stop treating it as the only authoritative home for the songwriting system.

**Why:** The repository's real value is the songwriting methodology: SOPs, critique rubrics, Suno formatting rules, character-voice methods, and album-continuity practices. Those should be usable even if a user does not run the exact platform that reads `.kiro/` files. The current platform should remain the best-supported automation adapter because the repo already uses it deeply, but exclusivity makes the knowledge base fragile and harder to adopt.

**Repo change implied:** Add platform-neutral methodology files and describe `.kiro/` as an adapter that automates those files.

### Recommendation 2 — Move canonical methodology into `core/`

**What it means:** Create a neutral `core/` area for the authoritative songwriting workflow, critique rubric, Suno optimization rules, concept-album continuity method, and character-voice method.

**Why:** Today, universal rules are spread across top-level docs, `.kiro/` steering, agents, skills, references, examples, and songs. That makes it hard to know which text is the source of truth. A core directory gives future maintainers one place to update universal rules before syncing them into platform adapters.

**Repo change implied:** Add `core/methodology/*.md` and migrate/cross-link the core rules from existing SOPs and references.

### Recommendation 3 — Keep `.kiro/` as the first-class adapter during migration

**What it means:** Do not delete or break `.kiro/`. Instead, make it consume or mirror the neutral core methodology.

**Why:** The current repository is already organized around `.kiro/` steering, agents, hooks, skills, powers, and SOPs. Removing that would throw away the only working automation layer. The problem is not that the current platform exists; the problem is that the repo currently reads as if the platform is required.

**Repo change implied:** Keep `.kiro/` active, but document which `.kiro/` files are generated/adapted from core methodology and which are platform-specific automation prompts.

### Recommendation 4 — Add a platform support matrix

**What it means:** Add a `README_PLATFORM_SUPPORT.md` that says what works with the current platform automation, what works with any AI assistant, and what works manually.

**Why:** Users need to know whether a feature is methodology, automation, or example content. For example, a writing SOP can be followed manually; a hook requires the current platform; a deterministic validator can run from the command line.

**Repo change implied:** Add a small matrix covering SOPs, agents, skills, hooks, powers, validators, album bibles, examples, songs, and analysis reports.

### Recommendation 5 — Add deterministic validators

**What it means:** Write scripts for checks that should not depend on LLM interpretation: character counts, required sections, tag syntax, weak line endings, approximate syllable counts, and album-schema checks.

**Why:** The repo currently asks agents/hooks to perform checks that a script can do more consistently. LLMs are useful for judgment and revision advice; scripts are better for exact counts and structural validation.

**Repo change implied:** Add `tools/count-suno-fields.py`, `tools/validate-song-format.py`, and later `tools/validate-album-continuity.py`; then have hooks reference those tools.

### Recommendation 6 — Add a claim registry and bibliography

**What it means:** Track the repo's actionable claims with source, confidence, verification date, affected files, and retest date.

**Why:** The repo currently contains academic theory, craft heuristics, user preferences, and platform-specific Suno prompt claims side by side. A claim registry prevents unverified or outdated statements from becoming invisible doctrine.

**Repo change implied:** Add `core/claims/claim-registry.yml` and `core/claims/source-bibliography.md`.

### Recommendation 7 — Version and retest Suno-specific guidance

**What it means:** Treat Suno instructions as model-version-sensitive unless proven stable.

**Why:** Suno behavior changes over time. A tag, field limit, UI feature, or prompt strategy that worked in one model version may not work the same way later. The repo should preserve useful Suno guidance, but it should label version, date, confidence, and test status.

**Repo change implied:** Add a Suno model/version matrix and an `experiments/suno/` test-log template.

### Recommendation 8 — Calibrate critique scores

**What it means:** Add score anchors and example critiques so the difference between a 6, 7.5, 8.5, and 9.5 is concrete.

**Why:** The pipeline uses critique scores to decide whether to revise, optimize, or rethink a song. If the scores are not calibrated, the decision gate looks precise but may be inconsistent.

**Repo change implied:** Add rubric anchors, calibration examples, and a blind-review procedure to the critique reference or a new core rubric file.

### Recommendation 9 — Convert album continuity into schemas

**What it means:** Keep prose album bibles, but add machine-readable registries for tracks, characters, motifs, keys, sonic palettes, callbacks, and hard rules.

**Why:** Album continuity is one of the repo's strongest ideas, but prose-only rules are hard to validate consistently. A schema allows scripts and platform hooks to check the same source of truth.

**Repo change implied:** Add `core/schemas/album-bible.schema.json` and eventually migrate example album bibles into structured data plus human-readable docs.

### Recommendation 10 — Separate universal, example, and personal material

**What it means:** Make it clear which files are universal methodology, which are examples, and which are user-specific preferences or album content.

**Why:** New users should not accidentally inherit one album's rules, one writer's preferences, or one set of example songs as universal doctrine.

**Repo change implied:** Add an inventory, strengthen README labels, and avoid placing personal album assumptions in universal methodology files.

### Recommendation 11 — Add rights and ethics checks for AI music workflows

**What it means:** Add a short checklist for voice models, custom models, reference artists, generated output disclosure, and distribution rights.

**Why:** The repo's workflow is not only craft; it is a production workflow. Voice/model training and artist-style prompting can create legal and ethical risks that should be handled before rendering or release.

**Repo change implied:** Add rights/ethics checks to the Suno optimization SOP and the full pipeline SOP.

### Recommendation 12 — Normalize templates and generated inventories

**What it means:** Standardize song, critique, continuity, and optimization report headings; then add a simple inventory check for docs and hooks.

**Why:** Current examples vary in heading style and format. That is normal for a growing repo, but inconsistent examples make validation harder and confuse new users.

**Repo change implied:** Add canonical templates and migrate examples gradually instead of rewriting all song history at once.


---

## Recommended repository restructuring

### Proposed target architecture

```text
songwriting-kb/
├── core/
│   ├── methodology/
│   │   ├── songwriting-workflow.md
│   │   ├── critique-rubric.md
│   │   ├── suno-optimization.md
│   │   ├── concept-album-continuity.md
│   │   └── character-voice.md
│   ├── schemas/
│   │   ├── song.schema.json
│   │   ├── critique.schema.json
│   │   ├── album-bible.schema.json
│   │   └── suno-test.schema.json
│   └── claims/
│       ├── claim-registry.yml
│       └── source-bibliography.md
├── tools/
│   ├── validate-song-format.py
│   ├── count-suno-fields.py
│   ├── validate-album-continuity.py
│   └── compile-adapters.py
├── adapters/
│   ├── current-platform/
│   │   ├── steering/
│   │   ├── agents/
│   │   ├── skills/
│   │   ├── hooks/
│   │   └── powers/
│   └── manual/
│       ├── workflow-checklists/
│       └── prompt-packets/
├── examples/
├── references/
├── songs/
└── analysis/
```

### Canonical-source rule

After restructuring, the canonical methodology should live in `core/`. Platform directories should be generated, copied, or clearly marked as adapters. No `.kiro/`, Suno, or personal-preference adapter should be the only place where a universal rule exists.

---

## Detailed improvement plan

### Phase 1 — Inventory and terminology cleanup

1. Add a repository inventory that lists every file by role: core methodology, platform adapter, reference, example, song output, analysis output.
2. Rename documentation language from “Kiro ecosystem” to “platform-neutral songwriting system with a current-platform adapter.”
3. Add a platform support matrix:
   - Current `.kiro/` platform: steering, hooks, agents, skills, powers, SOPs.
   - Non-platform use: markdown SOPs, prompt packets, and reference docs only.
   - Manual/human workflow: SOPs, templates, validators.
4. Fix count and version inconsistencies, especially hooks and Suno version labels.

### Phase 2 — Evidence and research governance

1. Create `core/claims/claim-registry.yml` with fields:
   - `id`
   - `claim`
   - `category` (`academic`, `craft`, `platform`, `empirical-test`, `preference`)
   - `source`
   - `source_quality`
   - `date_added`
   - `date_verified`
   - `applies_to_versions`
   - `confidence`
   - `files_using_claim`
   - `expiry_or_retest_date`
2. Convert source lists into real bibliography entries with URLs, editions, dates, and notes on what each source supports.
3. Mark unverified Suno tag behavior as `experimental` until tested.
4. Add a quarterly Suno revalidation checklist because model behavior and UI features are unstable.

### Phase 3 — Deterministic validators

1. Build scripts for:
   - Style prompt character count.
   - Lyrics field character count.
   - Required section detection.
   - Tag syntax validation.
   - Weak line-ending detection.
   - Approximate syllable count with manual override support.
2. Make Kiro hooks call scripts first and ask the agent only for interpretive follow-up.
3. Add equivalent command-line usage instructions for the same scripts.
4. Add CI checks so docs and examples cannot drift silently.

### Phase 4 — Rubric calibration

1. Add score anchors for every category at 3, 5, 7, 8.5, and 10.
2. Create a calibration set from existing songs and critiques.
3. Add a blind-review SOP:
   - First pass: no score, just observations.
   - Second pass: score with anchors.
   - Third pass: compare to calibration examples.
4. Track self-score vs independent-score deltas in `analysis/`.
5. Decide whether fatal gates should override averages, e.g., album hard-rule failure, nonfunctional chorus, or unsafe/rights issue.

### Phase 5 — Album schema and adapter compilation

1. Convert album bibles into machine-readable registries for tracks, characters, motifs, keys, callbacks, and sonic palettes.
2. Generate conditional steering summaries from each bible.
3. Generate continuity hooks from the same registry.
4. Support exception records for intentional rule-breaking.
5. Keep prose bibles for human readability, but make schemas authoritative for validation.

### Phase 6 — Current-platform and general-use adapter implementation

1. Keep `.kiro/` for backward compatibility during migration.
2. Document `.kiro/` as the current-platform adapter, not as the canonical source of every rule.
3. Add manual prompt packets/checklists for users who want the methodology without the platform automation.
4. Add a generated `README_PLATFORM_SUPPORT.md` showing exactly what requires `.kiro/` and what works without it.

### Phase 7 — Suno test harness and ethics

1. Create `experiments/suno/` for prompt tests and render audits.
2. Record model version, date, settings, prompt, lyrics, output notes, and whether a tag/control worked.
3. Add rights checks for Voices and Custom Models:
   - Confirm ownership or permission for all uploaded voice/model training material.
   - Avoid impersonation of living artists without consent.
   - Record distribution/license constraints.
4. Add a disclosure policy for AI-generated or AI-assisted tracks.

---

## Platform recommendation: should the current platform remain exclusive?

### Recommendation

**Generalize the repository while preserving the current `.kiro/` setup as a first-class adapter. Do not keep the current platform as the exclusive way to use the repo unless the project intentionally wants to be a platform-specific automation package rather than a broadly usable songwriting knowledge base.**

### Why the current platform should remain supported

- The current repository is already structurally aligned with Kiro: `.kiro/steering`, `.kiro/agents`, `.kiro/skills`, `.kiro/hooks`, `.kiro/powers`, and `.kiro/sops`.
- The current platform's powers are relevant if the repo later adds deterministic tools or external integrations because they package tools with contextual guidance.
- Migration cost is lowest if Kiro remains the active adapter while core methodology is extracted.

### Why platform-neutral core is the best long-term answer

- The creative methodology should outlive any single IDE or model provider.
- Suno behavior and platform automation formats are moving targets.
- Deterministic validators and schemas can run anywhere.
- A neutral core lets users apply the repository methodology without depending on one IDE's automation layer.

---

## Minimum viable migration checklist

If the project wants the fastest high-impact generalization, do these first:

1. Add `README_PLATFORM_SUPPORT.md` with current-platform, non-platform, and manual-use columns.
2. Move or copy core SOP summaries into `core/methodology/`.
3. Add manual prompt packets/checklists for the five main workflows.
4. Add a `tools/count-suno-fields.py` validator and wire `.kiro/` hooks to reference it.
5. Add `core/claims/claim-registry.yml` with the top 25 most operational claims.
6. Add `experiments/suno/README.md` and one test-log template.
7. Update README quick start so the current platform is “recommended for full automation,” not “required for the knowledge base.”

---

## Success metrics

- A non-platform user can follow the writing, critique, and optimization workflows without reading `.kiro/`.
- A current-platform user retains current automation with no regression.
- Every Suno model-specific claim has a date, version, confidence, and retest policy.
- Character-count and required-format checks are deterministic.
- Critique scores become more stable across reviewers because anchors and calibration examples exist.
- Album continuity failures can be validated from a schema rather than only prose prompts.

---

## Final judgment

The repository is creatively sophisticated and operationally useful, but it currently reads more like a powerful expert prompt system than a fully governed research methodology. The best path is to preserve the creative depth while adding research hygiene: citations, claim tracking, versioned experiments, deterministic checks, score calibration, and platform adapters. The current `.kiro/` platform should remain recommended for users who want the complete current automation experience, but it should not be the exclusive way to use the repo. The canonical songwriting methodology should become platform-neutral.
