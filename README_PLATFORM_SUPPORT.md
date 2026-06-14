# Platform Support Matrix

This repository's canonical goal is a portable songwriting methodology. The current `.kiro/` directory remains the best-supported automation adapter, but the core methods can also be used without platform automation or manually.

| Repo feature | Current `.kiro/` automation | Non-platform use | Manual use | Source paths |
|---|---|---|---|---|
| Songwriting workflow | Songwriter agent and steering load the workflow automatically. | Follow the SOP/reference docs with any assistant by pasting the relevant prompt packet or source excerpt. | Use the checklist directly while drafting. | `.kiro/sops/01-writing-a-song.md`, `.kiro/agents/songwriter.md`, `SONGWRITING_KNOWLEDGE_BASE.md` |
| Critique workflow | Critic agent can run the layered rubric and create reports. | Provide the song plus rubric/reference excerpts to an assistant. | Score with the rubric and record findings in `analysis/`. | `.kiro/sops/02-critiquing-a-song.md`, `.kiro/agents/critic.md`, `references/CRITIQUE_REFERENCE.md`, `analysis/README.md` |
| Suno optimization | Suno optimizer agent and hooks check formatting and field limits. | Use the Suno SOP plus `tools/count-suno-fields.py` for deterministic field counts before rendering. | Manually format fields and run `tools/count-suno-fields.py` before rendering. | `.kiro/sops/03-optimizing-for-suno.md`, `.kiro/agents/suno-optimizer.md`, `references/SUNO_TAGS_REFERENCE.md`, `tools/count-suno-fields.py` |
| Concept-album continuity | Album-continuity agent and album hooks can enforce rules when configured. | Use album bibles and future schemas as source material for assistant review. | Compare each track against the album bible and record exceptions. | `.kiro/sops/04-setting-up-concept-album.md`, `.kiro/sops/05-extending-an-album.md`, `.kiro/agents/album-continuity.md`, `references/YOUR_ALBUM_BIBLE.md` |
| Character voice design | Character-voice skill can load the voice reference on demand. | Use the core method and reference doc with any assistant. | Complete the voice template before writing character songs. | `.kiro/sops/06-character-voice-design.md`, `.kiro/skills/character-voice/SKILL.md`, `references/CHARACTER_VOICE_REFERENCE.md` |
| Claims and evidence | Platform prompts should eventually reference claim IDs. | Use `core/claims/claim-registry.yml` to audit whether a rule is sourced, tested, or a heuristic. | Review claim IDs before updating universal guidance. | `core/claims/claim-registry.yml`, `core/claims/source-bibliography.md` |
| Suno experiments | Platform agents can consult experiment results once populated. | Use experiment templates to record prompt/render observations. | Log render tests before promoting new Suno claims. | `experiments/suno/README.md`, `experiments/suno/TEMPLATE.yml` |
| Hooks | `.kiro/hooks/*.hook.json` can fire in the current platform. | Use command-line tools where available; otherwise run the relevant SOP. | Run the same checks manually from templates. | `.kiro/hooks/song-format-check.hook.json`, `.kiro/hooks/suno-char-count.hook.json`, `.kiro/hooks/prosody-lint.hook.json`, `.kiro/hooks/quick-score.hook.json`, `.kiro/hooks/full-pipeline.hook.json` |

## Reading order by use case

### Full automation

1. Read `README.md`.
2. Use the current `.kiro/` setup.
3. Use `tools/count-suno-fields.py` for deterministic Suno field checks.
4. Record evidence before changing universal guidance.

### Non-platform assistant use

1. Read the relevant `core/methodology/*.md` summary.
2. Follow the cited SOP/reference file.
3. Run available command-line validators.
4. Save critique or optimization outputs under `analysis/`.

### Manual use

1. Use SOPs as checklists.
2. Use `core/methodology/` summaries as quick references.
3. Run validators before finalizing files.
4. Record exceptions and evidence updates explicitly.
