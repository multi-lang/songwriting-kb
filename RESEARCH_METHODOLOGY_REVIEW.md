# Research Methodology Review and Platform-Generalization Plan

**Review date:** 2026-06-09  
**Scope reviewed:** Root documentation, `.kiro/` agents/skills/hooks/steering/SOPs/power, reference corpus, examples, analysis reports, and song examples.  
**Primary question:** Are the repository's stated research methods sound enough to support professional songwriting workflows, and should the project remain platform-specific or become more generally usable?

---

## Executive Conclusion

The repository is a strong creative-production knowledge base, but it currently presents itself as more methodologically verified and more platform-portable than the files support. The craft framework is rich and internally coherent: it combines songwriting craft, music-production theory, critique rubrics, Suno formatting practice, concept-album continuity, and concrete SOPs. However, the research layer has four major weaknesses:

1. **Source traceability is too shallow.** Several major docs list source families but do not provide per-claim citations, dated source snapshots, or a bibliography that lets maintainers verify individual claims.
2. **Empirical claims are under-instrumented.** Suno-specific prompt and tag recommendations are presented as tested or confirmed, but there is no render log, test design, version matrix, control prompt set, or regression suite.
3. **Scoring methods are not calibrated.** The critique system uses detailed scoring rubrics, but there is no evidence of inter-rater reliability, score distribution analysis, human-listener validation, or post-render outcome comparison.
4. **The repository is structurally coupled to Kiro while claiming broader usability.** The active automation layer is `.kiro/`, README copy is Kiro-centric, examples tell users to copy files into `.kiro/`, and the repository has no `.kilo/`, `AGENTS.md`, CLI scripts, or generic adapter layer.

**Recommendation:** Do **not** remain solely dependent on Kiro, and do **not** migrate exclusively to Kilo Code either. Keep Kiro as the first-class maintained adapter because the current implementation is already built around Kiro's steering, agents, hooks, skills, powers, and SOPs. Add a platform-neutral core plus adapters for Kiro, Kilo Code, and manual/CLI use. This preserves the working Kiro experience while making the knowledge base reusable across tools.

---

## Evidence Summary From the Repository

### Platform coupling

- The README describes the project as a complete Kiro IDE ecosystem and says the `.kiro/` directory auto-configures Kiro with agents, skills, hooks, power, steering, and SOPs.
- The documented repository structure centers `.kiro/` as the active runtime layer.
- `.kiro/README.md` defines `.kiro/` as the system configuration directory and describes agents, skills, hooks, steering, SOPs, and powers in Kiro terms.
- Hooks are Kiro-specific JSON files using `askAgent` actions and Kiro event types.
- No Kilo Code files are present; a repository search found zero references to `Kilo`, `.kilo`, or `kilocode` outside this review.

### Research-method claims

- `SONGWRITING_KNOWLEDGE_BASE.md` lists broad sources such as Berklee Online, iZotope, Pat Pattison, Billboard, Suno prompt guides, and real Suno playlist prompts.
- `MUSIC_PRODUCTION_THEORY.md` lists academic and professional source families including Berklee, Pat Pattison, Patrik Juslin, Philip Tagg, Franco Fabbri, MIR research, Sound on Sound, and Springer.
- `references/SUNO_STYLE_GENRE_REFERENCE.md` maps genre/style, emotion cues, BPM, instruments, vocal descriptors, and Suno style-prompt construction to named frameworks such as Fabbri, Juslin/Gabrielsson, Tagg, Moore, Lacasse, and Moylan.
- `references/CRITIQUE_REFERENCE.md` defines a layered critique system: 12 core categories, 5 advanced assessments, Suno optimization, and album-context checks.
- SOP 07 defines a write → critique → revise → optimize → verify → render pipeline with score thresholds.

### Process assets

- There are dedicated SOPs for writing, critiquing, Suno optimization, concept album setup, album extension, character voice design, full pipeline, and contributing.
- There are specialized agents for songwriting, critique, Suno optimization, and album continuity.
- There are automated hook definitions for format checks, character counts, prosody linting, quick score, and full-pipeline prompts.
- There are example album bibles, steering files, continuity hooks, songs, and critique reports.

---

## Strengths

### 1. Strong workflow decomposition

The repository does not just store references; it translates them into executable workflow roles: SOPs, agents, skills, hooks, and examples. This makes the project closer to an applied production system than a static knowledge base.

### 2. Clear multi-layer methodology

The method distinguishes between lyric craft, production theory, Suno formatting, concept continuity, critique scoring, and revision gates. This separation is valuable because it prevents a single vague “make it better” rubric from dominating all work.

### 3. Good conceptual coverage

The stated frameworks cover useful dimensions for songwriting and production review:

- Hook construction and song form.
- Lyric specificity, prosody, rhyme, and narrative arc.
- Harmony, arrangement, timbre, genre, and production space.
- Persona/voice and character delivery.
- Platform formatting and prompt constraints.
- Concept-album continuity and motif management.

### 4. Useful examples and operational artifacts

The examples are substantial enough to teach by imitation: album bibles, continuity hooks, steering files, completed songs, and critique outputs give users concrete patterns rather than abstract advice only.

### 5. Kiro implementation is coherent

If the goal is specifically Kiro usage, the current structure is internally consistent: `.kiro/steering`, `.kiro/agents`, `.kiro/skills`, `.kiro/hooks`, `.kiro/sops`, and `.kiro/powers` all map naturally to Kiro's feature model.

---

## Problems and Risks

### P0 — Repo identity ambiguity: Kiro vs Kilo vs platform-neutral

**Problem:** The user-facing request mentions “klilo/kilo,” but the repository itself is Kiro-specific. There is no Kilo Code adapter, no `.kilo/agents`, no `kilo.jsonc`, no Kilo workflow definitions, and no generic runtime layer.

**Why it matters:** Users may clone the repo expecting Kilo Code or general-agent compatibility and discover that the active automation is Kiro-only. This damages portability and onboarding.

**Improvement:** Rename the current implementation as `adapters/kiro` conceptually, even if `.kiro/` stays at the root for compatibility. Add explicit platform support status in README:

| Platform | Current status | Recommended path |
|---|---|---|
| Kiro | First-class, working adapter | Keep maintained |
| Kilo Code | Not implemented | Add adapter |
| Other agents/manual | Partially usable through markdown SOPs | Add generic core and scripts |

### P0 — No central source ledger or per-claim citations

**Problem:** The repository names many sources but does not tie individual claims to bibliographic entries, URLs, access dates, papers, books, or source excerpts.

**Examples:**

- The master songwriting doc lists source families in one line.
- The production-theory doc lists source families but not a bibliography.
- Suno v5/v5.5 claims and community-tested tags are scattered across references without a test ledger.

**Why it matters:** Without traceability, maintainers cannot distinguish durable craft principles from platform-specific folklore, user preference, or dated model behavior.

**Improvement:** Add `references/SOURCE_LEDGER.md` with fields:

```markdown
| ID | Claim area | Source | Type | Date/accessed | Stability | Used in files | Verification status |
|---|---|---|---|---|---|---|---|
```

Then convert high-impact claims to cite source IDs inline, especially:

- Suno limits, sliders, tags, and version behavior.
- Academic frameworks and their interpretations.
- Industry/commercial claims.
- Score thresholds and quality gates.

### P0 — Suno prompt methodology lacks reproducible evidence

**Problem:** The repo makes many Suno-specific claims about tags, sliders, field limits, control tags, parser behavior, prompt specificity, layers, version features, and generation outcomes. These claims may be useful, but the repo does not include a reproducible testing methodology.

**Why it matters:** AI music platforms change behavior frequently. A recommendation that worked in one Suno version, account tier, or genre may fail later.

**Improvement:** Add a reproducible render experiment system:

- `experiments/suno/README.md` — method, variables, controls, ethics/copyright rules.
- `experiments/suno/renders.csv` — prompt ID, date, Suno version, account tier, style prompt, lyric hash, slider values, seed/reference if available, output notes.
- `experiments/suno/findings.md` — only claims backed by repeated tests.
- Version labels for every Suno-specific recommendation: `stable`, `observed`, `community-reported`, `untested`, `deprecated`.

### P1 — Scoring system is precise but not validated

**Problem:** The critique system has detailed categories and thresholds, but no calibration data. The pipeline treats composite scores as decision gates, yet there is no repository evidence that 8.5, 7.0, or category weights predict listener response, render quality, or user satisfaction.

**Why it matters:** Precise numbers can create false authority. A 12-category score looks rigorous even when categories are not normalized or validated.

**Improvement:** Add score calibration assets:

- `analysis/calibration/scorebook.md` — anchor examples for 5, 7, 8.5, 10 in each category.
- `analysis/calibration/rater-agreement.md` — compare at least two independent reviews per song.
- `analysis/calibration/outcome-correlation.md` — correlate pre-render scores with post-render ratings.
- Change score language from “objective quality” to “rubric estimate” unless validated.

### P1 — Hook checks are agent-prompt based rather than deterministic where possible

**Problem:** Character count, required-section checks, and some lint checks are currently implemented as prompts to an agent. These checks can be nondeterministic and may consume model credits.

**Why it matters:** Deterministic constraints such as character counts, required headings, duplicate forbidden phrases, and front-matter validation should not depend on an LLM.

**Improvement:** Add scripts:

- `tools/check_suno_counts.py`
- `tools/check_song_format.py`
- `tools/check_prosody.py` or a documented heuristic version
- `tools/check_album_continuity.py --rules <album-rules.yml>`

Then wire Kiro hooks, Kilo workflows, and CI to those scripts.

### P1 — Active and example assets are mixed conceptually

**Problem:** The README frames `.kiro/` as active configuration and examples as reference implementations, but several active references still point to placeholder or user-specific bibles. There are also real album/song examples in primary directories.

**Why it matters:** Users may not know what is reusable framework, what is sample content, and what is personal/project-specific content.

**Improvement:** Separate concerns:

```text
core/                 platform-neutral methodology
adapters/kiro/         Kiro-facing generated/maintained config source
adapters/kilo/         Kilo-facing generated/maintained config source
examples/              inactive examples only
projects/              user album/song workspaces, gitignored by default if desired
references/            validated reusable references
```

Keep `.kiro/` at root as a generated or synchronized compatibility target until Kiro supports alternate config locations.

### P1 — “Complete system” language is stronger than the evidence

**Problem:** The README and Discord copy use strong promotional language such as “complete,” “professional,” and “confirmed” in areas where the evidence is not documented.

**Why it matters:** Strong claims invite scrutiny. If the source ledger and experiments do not exist yet, better wording would increase trust.

**Improvement:** Use evidence-tier labels:

- **Principle** — durable craft/theory claim.
- **Heuristic** — practical rule of thumb.
- **Observed** — tested in this repo's logs.
- **Community-reported** — useful but not verified here.
- **Platform-specific** — may change with provider updates.

### P2 — No CI or repository-level validation command

**Problem:** There is no single command that validates JSON, Markdown structure, links, song format, Suno character counts, or references.

**Improvement:** Add `make validate` or `python tools/validate_repo.py` and run it in CI. At minimum, validate:

- JSON parse.
- Required docs exist.
- All `.kiro/hooks/*.json` contain expected keys.
- Song files contain expected sections.
- Source IDs referenced in docs exist in `SOURCE_LEDGER.md`.
- Kiro/Kilo generated adapters are synchronized with core templates.

### P2 — No explicit data model for songs, critiques, albums, or prompts

**Problem:** The system relies on Markdown conventions. This is readable but makes validation and migration harder.

**Improvement:** Add YAML front matter or sidecar JSON/YAML schemas:

```yaml
title:
version:
project:
platform_targets: [suno]
style_prompt:
exclude_prompt:
key:
bpm:
voice:
status: draft|critiqued|optimized|rendered
source_method_version:
```

### P2 — Contribution workflow does not include methodology review

**Problem:** The contributing SOP focuses setup and customization but should require source-tier labeling, validation commands, and method-review notes for claims.

**Improvement:** Add a contribution checklist:

- New research claim has source ID.
- New Suno claim has evidence tier and version.
- New hook has deterministic test if possible.
- New scoring rubric change includes calibration impact.
- Platform-specific change updates adapter map.

---

## Platform-Generalization Plan

### Guiding principle

Make the **methodology platform-neutral** and keep platform integrations as thin adapters. The core should answer “what is the songwriting method?” while adapters answer “how does this tool load and enforce it?”

### Target architecture

```text
songwriting-kb/
├── core/
│   ├── methodology/
│   │   ├── songwriting.md
│   │   ├── critique.md
│   │   ├── suno-formatting.md
│   │   ├── concept-album.md
│   │   └── character-voice.md
│   ├── sops/
│   ├── roles/
│   ├── rules/
│   └── schemas/
├── adapters/
│   ├── kiro/
│   │   ├── steering/
│   │   ├── agents/
│   │   ├── skills/
│   │   ├── hooks/
│   │   └── sync.md
│   ├── kilo/
│   │   ├── agents/
│   │   ├── workflows/
│   │   ├── rules/
│   │   └── kilo.jsonc
│   └── generic/
│       ├── AGENTS.md
│       ├── prompts/
│       └── cli.md
├── tools/
│   ├── validate_repo.py
│   ├── render_templates.py
│   ├── check_suno_counts.py
│   └── check_song_format.py
├── experiments/
│   └── suno/
├── references/
├── examples/
└── .kiro/                 # generated or compatibility copy for Kiro users
```

### Phase 1 — Clarify support status without breaking Kiro

1. Add README platform matrix.
2. Add `docs/PLATFORM_SUPPORT.md` explaining Kiro, Kilo Code, generic/manual support.
3. Label `.kiro/` as the current first-class adapter.
4. Clarify that Kilo Code is not currently implemented.
5. Keep all existing Kiro paths working.

### Phase 2 — Create platform-neutral core

1. Move or copy reusable methodology into `core/`.
2. Convert `.kiro/sops` into `core/sops` as canonical source.
3. Convert agent prompts into `core/roles/*.md`.
4. Convert hook logic into `core/rules/*.yml` where deterministic.
5. Add a sync note: generated adapters must not drift from core.

### Phase 3 — Add deterministic validation

1. Implement JSON validation and hook schema checks.
2. Implement Suno character-count parsing.
3. Implement required-section checks.
4. Add album continuity rule files.
5. Add one command: `python tools/validate_repo.py`.

### Phase 4 — Add Kilo Code adapter

Based on current Kilo Code docs as of 2026-06-09, Kilo supports project agents through `.kilo/agents/*.md` or `.kilo/agent/*.md`, can configure agents in `kilo.jsonc`, and supports custom subagents with permission controls and isolated contexts. The comparison also used current Kiro docs for steering, hooks, and custom subagents. See [External platform references](#external-platform-references) for the platform documentation checked during this review. A practical adapter should include:

```text
.kilo/
├── agents/
│   ├── songwriter.md
│   ├── critic.md
│   ├── suno-optimizer.md
│   └── album-continuity.md
├── workflows/
│   ├── full-pipeline.md
│   ├── critique.md
│   └── optimize-suno.md
└── rules/
    └── songwriting.md
kilo.jsonc
```

Mapping:

| Current Kiro concept | Kilo Code equivalent or workaround |
|---|---|
| `.kiro/agents/*.md` | `.kilo/agents/*.md` custom agents |
| Kiro subagents | Kilo custom subagents / `@agent-name` invocation |
| Kiro steering | Kilo project rules / AGENTS.md / custom instructions |
| Kiro hooks | Kilo workflows plus deterministic scripts; if native hooks differ, call scripts manually or through workflow steps |
| Kiro skills | Kilo skills if available, or referenced role/rule docs |
| Kiro powers | Generic bundle doc plus Kilo workflow entrypoint |

### Phase 5 — Add generic agent/manual adapter

Add `AGENTS.md` at repo root with tool-agnostic instructions:

- Read core methodology first.
- Use role docs for songwriter/critic/optimizer/continuity.
- Run deterministic validators before final output.
- Do not claim Suno behavior unless source tier supports it.

Add prompt packs:

```text
adapters/generic/prompts/write-song.md
adapters/generic/prompts/critique-song.md
adapters/generic/prompts/optimize-suno.md
adapters/generic/prompts/check-continuity.md
```

### Phase 6 — Improve research governance

1. Add `references/SOURCE_LEDGER.md`.
2. Add evidence tiers to Suno tags and platform claims.
3. Add `experiments/suno/` with render logs.
4. Add score calibration files.
5. Add `docs/METHODOLOGY_VERSIONING.md` so users know when the method changed and why.

---

## Should Kiro Remain Recommended?

**Yes, but only as the current best-supported adapter, not as the conceptual home of the project.**

### Justification for keeping Kiro first-class

1. **The implementation already exists.** The active agents, steering, skills, hooks, SOPs, and power are all Kiro-shaped.
2. **The workflow model matches the repository.** Kiro's steering and hooks map well to always-on songwriting context and file-save checks.
3. **The examples are already written in Kiro terms.** Removing Kiro would be disruptive and unnecessary.
4. **The project benefits from event-driven checks.** Kiro hooks are useful for format checks, character counts, and continuity prompts, even though deterministic scripts should replace some agent-prompt checks over time.

### Why Kiro should not remain exclusive

1. **The methodology is larger than Kiro.** Songwriting craft, critique rubrics, album bibles, and Suno formatting are not inherently Kiro-specific.
2. **Users may work in other agent environments.** Kilo Code, Claude Code, Codex, Cursor, and manual workflows can all use Markdown SOPs and role prompts if packaged properly.
3. **Platform lock-in raises maintenance risk.** If Kiro changes hook schemas, skills, powers, or agent semantics, the whole repo becomes brittle unless the core is separate.
4. **The user-facing value is the knowledge system, not the IDE.** The repo should market itself as a songwriting knowledge base with adapters, not as only a Kiro package.

### Should Kilo Code be recommended instead?

**Not as an exclusive replacement.** Kilo Code appears suitable for a future adapter because it supports custom agents/subagents, project configuration, and rules/workflows. But this repository contains no Kilo implementation today. Recommending Kilo as the primary platform now would be premature unless the repo adds `.kilo/` assets and tests them.

---

## Recommended Immediate Repository Changes

1. **Add platform support docs.** State that Kiro is currently supported, Kilo Code is planned, and core/manual use is partially supported.
2. **Add a source ledger.** Begin with existing broad sources, then incrementally convert high-risk claims.
3. **Add deterministic validation scripts.** Start with JSON validation, required-section checks, and Suno character counts.
4. **Add an experiments area for Suno.** Treat tags and slider advice as hypotheses unless logged.
5. **Add score calibration docs.** Make critique scoring auditable.
6. **Change README language from “Kiro ecosystem” to “platform-neutral methodology with a Kiro adapter.”** Keep Kiro quick start as the first path until other adapters exist.
7. **Add a Kilo adapter milestone.** Do not claim support until `.kilo/agents`, rules/workflows, and validation instructions are committed.

---

## Proposed Milestones

### Milestone A — Trust and clarity

- `docs/PLATFORM_SUPPORT.md`
- `references/SOURCE_LEDGER.md`
- README platform matrix
- Evidence-tier glossary

### Milestone B — Deterministic quality gates

- `tools/validate_repo.py`
- `tools/check_suno_counts.py`
- `tools/check_song_format.py`
- CI or documented validation command

### Milestone C — Core extraction

- `core/sops/`
- `core/roles/`
- `core/methodology/`
- Sync guide for `.kiro/`

### Milestone D — Kilo adapter

- `.kilo/agents/*.md`
- Kilo rules/workflows
- `kilo.jsonc` where useful
- Kilo quick start and validation notes

### Milestone E — Empirical methodology

- Suno experiment logs
- Score calibration studies
- Post-render evaluation forms
- Methodology changelog

---

## Bottom Line

The repository is a valuable songwriting and AI-music production system, but its methodology needs better evidence management, reproducible tests, and clearer separation between durable knowledge and platform-specific implementation. Keep Kiro because it is currently the only fully realized adapter. Add Kilo Code and generic/manual adapters after extracting a platform-neutral core. Do not claim Kilo support until the adapter exists and has been validated.

---

## External Platform References

These links were checked on 2026-06-09 to avoid relying only on remembered platform behavior:

- Kiro steering documentation: <https://kiro.dev/docs/steering/>
- Kiro hook actions documentation: <https://kiro.dev/docs/hooks/actions/>
- Kiro subagents documentation: <https://kiro.dev/docs/chat/subagents/>
- Kilo Code custom modes/agents documentation: <https://kilo.ai/docs/customize/custom-modes>
- Kilo Code custom subagents documentation: <https://kilo.ai/docs/customize/custom-subagents>
