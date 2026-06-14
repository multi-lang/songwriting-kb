# Research Methodology Review and Platform Generalization Plan

**Date:** 2026-06-09  
**Scope reviewed:** top-level knowledge-base documents, `.kiro/` agents/skills/hooks/SOPs/power files, references, examples, songs, and analysis outputs.  
**User question addressed:** evaluate the repository's stated research and production methodologies, identify problems, recommend improvements, and plan a move from current Kiro/Kilo-specific reliance toward broader use unless a platform-specific recommendation is justified.

---

## Executive conclusion

This repository contains a strong creative-production methodology: it combines a 9-step prewriting analysis, Nashville-style chorus-first drafting, prosody and structure quality gates, a layered critique rubric, Suno optimization, and concept-album continuity controls. The best parts of the system are the repeatable workflow design, the separation between steering/agents/skills/SOPs, the existence of example outputs, and the explicit quality gates for prosody, hook timing, verse progression, bridge turns, character voice, and album continuity.

However, the repository is not yet a rigorous research methodology in the academic or empirical sense. It has many named theoretical sources and practical claims, but it lacks a claim registry, inline citations, test logs, versioned Suno experiments, inter-rater calibration, reproducible validators, and a clear distinction between evidence-backed findings, craft heuristics, personal preferences, and platform-specific prompt lore. The most important improvement is therefore not simply to add more theory; it is to make every actionable rule traceable, testable, and portable.

The platform recommendation is: **do not convert the repository into a Kilo-only or Kiro-only system. Keep Kiro as the best-supported first-class adapter for the current repo, add Kilo support as a compatibility adapter, and move the canonical methodology into platform-neutral core files.** Kiro is currently worth retaining because the repo is already built around Kiro-native steering, agents, hooks, skills, and powers, and current Kiro documentation explicitly supports those exact concepts. Kilo is also worth supporting because it implements portable Agent Skills and workspace `.kilo/skills/` directories, but Kilo-specific agents/workflows/configuration would need a separate adapter rather than a rename of `.kiro/`.

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
- Kilo Code implements Agent Skills as a lightweight/open format and loads skill metadata before on-demand `SKILL.md` loading: <https://kilo.ai/docs/customize/skills>.
- Kilo project skills live under `.kilo/skills/`, and Kilo also loads `.agents/skills/` for interoperability: <https://kilo.ai/docs/customize/skills>.
- Kilo custom subagents are configured in `kilo.jsonc` or `.kilo/agents/*.md`: <https://kilo.ai/docs/customize/custom-subagents>.
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
- Kilo users need `.kilo/skills/`, `.kilo/agents/`, `kilo.jsonc`, or `.agents/skills/` compatibility mappings; those do not currently exist.
- There is no platform support matrix that says which features work in Kiro, Kilo, Claude/Codex/OpenAI API, or manual use.

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
| Medium | Kiro/Kilo naming ambiguity | User confusion is likely because both platforms now support skills/agents | Use explicit adapter names: `adapters/kiro/` and `adapters/kilo/` |
| Medium | Legal/ethical risks under-specified | Voice cloning, custom models, reference artists, and distribution create non-craft risks | Add rights/ethics checklist and disclosure policy |
| Medium | Hooks count and feature descriptions are inconsistent | README and `.kiro/README.md` describe “3 universal hooks” while five hook JSON files exist | Normalize docs and add a generated inventory check |
| Medium | Album continuity is prose-first | Prose rules are harder to validate consistently | Add machine-readable album schema and compile prompts/hooks from it |
| Low | Time estimates are precise without measurement basis | 35-55 min and 50-75 min look empirical but may be anecdotal | Mark as estimates or collect workflow duration data |
| Low | Some markdown headings and output formats vary across songs | Inconsistent examples weaken validators and teaching value | Add canonical templates and migrate examples gradually |

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
│   ├── kiro/
│   │   ├── steering/
│   │   ├── agents/
│   │   ├── skills/
│   │   ├── hooks/
│   │   └── powers/
│   ├── kilo/
│   │   ├── .kilo/skills/
│   │   ├── .kilo/agents/
│   │   └── kilo.jsonc
│   └── open-agent/
│       └── .agents/skills/
├── examples/
├── references/
├── songs/
└── analysis/
```

### Canonical-source rule

After restructuring, the canonical methodology should live in `core/`. Platform directories should be generated, copied, or clearly marked as adapters. No Kiro, Kilo, Suno, or personal-preference adapter should be the only place where a universal rule exists.

---

## Detailed improvement plan

### Phase 1 — Inventory and terminology cleanup

1. Add a repository inventory that lists every file by role: core methodology, platform adapter, reference, example, song output, analysis output.
2. Rename documentation language from “Kiro ecosystem” to “platform-neutral songwriting system with a Kiro adapter.”
3. Add a platform support matrix:
   - Kiro: steering, hooks, agents, skills, powers, SOPs.
   - Kilo: skills, agents/subagents, workflows/config via `.kilo` and `kilo.jsonc`.
   - Generic AI assistant: markdown SOPs and reference docs only.
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
3. Add equivalent Kilo workflows or commands that call the same scripts.
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

### Phase 6 — Kiro/Kilo/general adapter implementation

1. Keep `.kiro/` for backward compatibility during migration.
2. Add `adapters/kiro/` as the documented source for Kiro-specific files, or keep `.kiro/` active and document that it is one adapter.
3. Add `.agents/skills/` or `adapters/open-agent/.agents/skills/` for portable Agent Skills.
4. Add `.kilo/skills/` and `.kilo/agents/` only if the project wants first-class Kilo support in-repo.
5. Add `kilo.jsonc` if Kilo-specific workflows/subagent permissions are needed.
6. Add a generated `README_PLATFORM_SUPPORT.md` showing exactly what users get on each platform.

### Phase 7 — Suno test harness and ethics

1. Create `experiments/suno/` for prompt tests and render audits.
2. Record model version, date, settings, prompt, lyrics, output notes, and whether a tag/control worked.
3. Add rights checks for Voices and Custom Models:
   - Confirm ownership or permission for all uploaded voice/model training material.
   - Avoid impersonation of living artists without consent.
   - Record distribution/license constraints.
4. Add a disclosure policy for AI-generated or AI-assisted tracks.

---

## Platform recommendation: Kiro, Kilo, or general?

### Recommendation

**Generalize the repository while preserving Kiro as a first-class adapter and adding Kilo compatibility. Do not make Kilo the sole platform. Do not remove Kiro unless the project no longer values hooks, steering, and powers as active automation.**

### Why Kiro should remain supported

- The current repository is already structurally aligned with Kiro: `.kiro/steering`, `.kiro/agents`, `.kiro/skills`, `.kiro/hooks`, `.kiro/powers`, and `.kiro/sops`.
- Current Kiro docs still support exactly the primitives this repo uses: steering, hooks, skills, subagents, powers, and MCP-oriented dynamic loading.
- Kiro powers are particularly relevant if the repo later adds deterministic tools or external integrations because powers package MCP tools with contextual guidance.
- Migration cost is lowest if Kiro remains the active adapter while core methodology is extracted.

### Why Kilo should be supported but not made exclusive

- Kilo's Agent Skills support makes it a good compatibility target.
- Kilo loads project skills from `.kilo/skills/` and interoperable skills from `.agents/skills/`, so the repo can support Kilo without abandoning a general core.
- Kilo agents/subagents can be configured through `.kilo/agents/*.md` or `kilo.jsonc`, but those files are not drop-in equivalents for every Kiro feature.
- Kilo support would require explicit adapter files, not just renaming `.kiro` to `.kilo`.

### Why platform-neutral core is the best long-term answer

- The creative methodology should outlive any single IDE or model provider.
- Suno, Kiro, Kilo, and agent skill formats are all moving targets.
- Deterministic validators and schemas can run anywhere.
- A neutral core lets users bring the methodology to Codex, Claude, ChatGPT, Kilo, Kiro, a DAW workflow, or manual co-writing sessions.

---

## Minimum viable migration checklist

If the project wants the fastest high-impact generalization, do these first:

1. Add `README_PLATFORM_SUPPORT.md` with Kiro/Kilo/generic/manual columns.
2. Move or copy core SOP summaries into `core/methodology/`.
3. Add `.agents/skills/` copies of the five current skills for open Agent Skills compatibility.
4. Add a `tools/count-suno-fields.py` validator and wire Kiro hooks to reference it.
5. Add `core/claims/claim-registry.yml` with the top 25 most operational claims.
6. Add `experiments/suno/README.md` and one test-log template.
7. Update README quick start so Kiro is “recommended for full automation,” not “required for the knowledge base.”

---

## Success metrics

- A non-Kiro user can follow the writing, critique, and optimization workflows without reading `.kiro/`.
- A Kiro user retains current automation with no regression.
- A Kilo user can load at least the five core Agent Skills and invoke equivalent agents/workflows.
- Every Suno model-specific claim has a date, version, confidence, and retest policy.
- Character-count and required-format checks are deterministic.
- Critique scores become more stable across reviewers because anchors and calibration examples exist.
- Album continuity failures can be validated from a schema rather than only prose prompts.

---

## Final judgment

The repository is creatively sophisticated and operationally useful, but it currently reads more like a powerful expert prompt system than a fully governed research methodology. The best path is to preserve the creative depth while adding research hygiene: citations, claim tracking, versioned experiments, deterministic checks, score calibration, and platform adapters. Kiro should remain recommended for users who want the complete current automation experience. Kilo should be added as a compatibility target, especially for Agent Skills. The canonical songwriting methodology should become platform-neutral.
