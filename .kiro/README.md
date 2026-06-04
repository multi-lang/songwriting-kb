# .kiro/ — System Configuration

> This directory configures the Kiro IDE (or kiro-cli) with agents, skills, hooks, steering, SOPs, and powers for professional songwriting.

---

## Directory Overview

| Directory | Purpose | Loads When |
|---|---|---|
| `steering/` | Always-on context injected into every session | Automatically (every chat) |
| `agents/` | Specialized AI roles invocable by name | On request ("write a song", "critique this") |
| `skills/` | On-demand knowledge sets (large reference docs) | When agent activates them or user requests |
| `hooks/` | Automated checks triggered by file events | On file create/save in matching patterns |
| `sops/` | Step-by-step procedures (tool-agnostic) | When user follows a workflow |
| `powers/` | Bundled capability packages | When activated via power system |

---

## Steering Files (Always Active)

| File | What It Does | Customize? |
|---|---|---|
| `songwriting.md` | Core craft principles, 9-step workflow, quality gates | No — universal |
| `suno-formatting.md` | Suno AI field limits, tags, sliders, v5.5 features | No — universal |
| `output-preferences.md` | Song output format (Production Notes, layers, formulas) | **Yes** — your conventions |
| `concept-album.md` | Album continuity framework + setup guide | No — universal framework |

**To add album-specific steering:** Create a new file with `fileMatch` front-matter so it only loads when working on your album's files. See `examples/albums/` for the pattern.

---

## Agents (4 Roles)

| Agent | Invoke With | Does |
|---|---|---|
| `songwriter` | "Write a song about X" | Creates complete songs from concepts |
| `critic` | "Critique this" / "Score this" | Multi-layer evaluation (12 + 5 + album) |
| `suno-optimizer` | "Make this Suno-ready" | Adds meta-tags, checks limits, validates format |
| `album-continuity` | "Check continuity" | Verifies album rules (**configure for YOUR album**) |

---

## Hooks (3 Universal)

| Hook | Triggers On | Checks |
|---|---|---|
| `song-format-check.json` | New file in `songs/` | All required sections present |
| `suno-char-count.json` | Save in `songs/` | Style ≤1000, Lyrics ≤5000 |
| `prosody-lint.json` | Save in `songs/` | Lines >12 syllables, stuffed phrases |

**To add album continuity hooks:** Copy the pattern from `examples/albums/*/continuity-hook.json` into this directory.

---

## Skills (5 Knowledge Sets)

| Skill | Contains | Size |
|---|---|---|
| `song-critique` | 3-layer scoring framework, rubric definitions | Large |
| `suno-meta-tags` | Complete tag reference, v5.5, layers, sliders | Large |
| `music-theory` | 12 disciplines, 23-point framework, 18 advanced concepts | Very large |
| `character-voice` | Accent/dialect system, voice design template | Medium |
| `concept-album-bible` | Album continuity template (**configure for your album**) | Variable |

---

## SOPs (8 Procedures)

Step-by-step workflows that work with ANY AI assistant or manually:

| # | SOP | Use When |
|---|---|---|
| 01 | Writing a Song | Creating a new song from concept to Suno-ready |
| 02 | Critiquing a Song | Evaluating/scoring an existing song |
| 03 | Optimizing for Suno | Final formatting pass before rendering |
| 04 | Setting Up a Concept Album | Building your album bible, steering, and hooks |
| 05 | Extending an Album | Adding tracks to an existing album |
| 06 | Character Voice Design | Creating a voice for a specific character/accent |
| 07 | Full Pipeline | Complete write→critique→revise→optimize→verify flow |
| 08 | Contributing | Community setup guide and contribution rules |

---

## For kiro-cli Users

This system works identically in kiro-cli (headless mode). The steering files load automatically, agents are invocable, and hooks fire on file events. The only difference: creative sliders and Suno Personas are Suno UI features — you'll need to set those manually when rendering.

---

## Customization Priority

If you're new, customize in this order:
1. `steering/output-preferences.md` — Your format conventions
2. `agents/album-continuity.md` — Your album rules (if applicable)
3. `skills/concept-album-bible/SKILL.md` — Point at your bible
4. Add a conditional steering file for your album (use `examples/` as template)
5. Add a continuity hook for your album
