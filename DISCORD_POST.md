# Discord Community Post — Songwriting Knowledge Base

*Copy/paste the section below into Discord. Formatted for readability in Discord markdown.*

---

## POST START (copy from here)

---

# Open-Source AI Songwriting System — Nashville Craft + Academic Theory + Suno v5.5

**Repo:** https://github.com/Voletek/songwriting-kb

I've been building a professional song production system that combines Nashville/LA co-writing methodology, academic musicology (Moore, Tagg, Lacasse, Pattison), and Suno AI v5.5 formatting — all packaged into a single repo that auto-configures when you clone it.

It's free. It works with Kiro IDE, any AI assistant, or just manually following the SOPs.

---

## What It Does

**Clone it. Talk to it. Get professional-quality songs.**

```
"Write a song about..."       → Full Nashville-method songwriting (27 steps)
"Critique this song"          → 3-layer academic critique (22 scoring dimensions)
"Make this Suno-ready"        → v5.5 formatting (Personas, Stems, Layers, Era Tags)
"Check album continuity"      → Verifies concept album rules across tracks
```

---

## What's Inside

**4 Agents** — Songwriter, Critic, Suno-Optimizer, Album-Continuity
**8 SOPs** — Step-by-step procedures for every workflow (writing, critiquing, optimizing, album setup, extending, character voice, full pipeline, contributing)
**5 Skills** — On-demand knowledge (critique rubric, Suno tags, music theory, character voice, concept album)
**3 Hooks** — Automated quality checks (format, char count, prosody lint)
**2 Complete Album Bibles** — Fractured Shadows (17-track digital→fantasy) + Keeper of the Light (8-track folk-horror)

---

## The Critic Agent (Newest Upgrade)

This is the part I'm most proud of. The critic runs a **3-layer evaluation model**:

### Layer 1: Core 12-Category Craft Rubric
Hook, Lyrics, Prosody, Arc, Structure, Originality, Singability, Commercial, Genre, Arrangement, Voice/Accent, Emotional Intelligence — each 1-10 with rubric definitions.

### Layer 2: 5 Advanced Assessments (Academic)
- **Functional Layers** (Allan Moore) — Are all 4 texture layers balanced?
- **Soundbox & Proxemics** (Lacasse/Moylan) — Is the virtual 3D space intentional? Does vocal distance match emotion?
- **Musemic Signification** (Philip Tagg) — Do the sounds MEAN what they should culturally?
- **Scope of Vision** (Dodge et al. 2025) — How ambitious is it? A daring partial success > a safe full success.
- **Skip Test** (A&R Industry) — Any 15-second window with no reward for attention?

### Layer 3: Album-Context Module (concept albums only)
Position awareness, intention vs delivery, transition consciousness, dramatic irony, motif accuracy, sonic differentiation.

**Real results:**
- A well-crafted concept album opener scored **8.4/10** core + **8.6/10** advanced (depth exceeds craft)
- A deliberately bad song scored **3.1/10** core + **2.6/10** advanced — and the critic caught a **4.4-point self-score inflation** (the writer rated themselves 7.5)

---

## Suno v5.5 Integration

The system is fully updated for current Suno capabilities:

- **Personas** — Lock a vocal identity per character across all album tracks
- **Stems (12-track)** — Post-production workflow: generate → extract → DAW master
- **Parenthetical Layers** — Full documentation of `(delivery cue)`, `(named layer: text)`, `(backup vocal)` notation with Style Prompt declaration rules
- **Era Tags** — How decade tags bias production style + the Separation Principle (vintage instruments + modern production)
- **The Specificity Principle** — 7 prompt dimensions that prevent generic output
- **Render Strategy** — Per-track slider presets, Inspo reference chains, dynamic map verification

---

## Concept Album Support

Both included albums demonstrate the full system:

**Keeper of the Light** (8 tracks) — Folk-horror/sea-shanty/dark ambient. A lighthouse keeper discovers the light she tends keeps something ancient asleep. Features non-vocal entity character design, harmonic circle structure (starts/ends in same key with transformed meaning), and sea-as-instrument across all 8 tracks.

**Fractured Shadows** (17 tracks) — A game developer burns out, dissolves into his own system, gets claimed by an AI, and wakes up in his fantasy world. Features `(robotic layer:)` notation for AI voice, a digital→organic sonic pivot at Track 8, and a key change reserved for the final chorus of the final track.

---

## Who This Is For

- **Suno creators** who want professional-quality output, not generic AI slop
- **Songwriters** who want a structured method (the 9-step workflow works with or without AI)
- **Concept album builders** who need continuity management across many tracks
- **Anyone** who wants to learn songwriting craft through a system designed by Nashville methodology + academic theory

---

## Getting Started

```bash
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb
# The .kiro/ directory auto-configures everything
# See .kiro/sops/08-contributing.md for full setup guide
```

**Works with:** Kiro IDE (full agent/skill/hook automation), any AI assistant (SOPs work as prompts), or manually (the knowledge base and reference docs are universal).

**Customize:** Rename the preferences file, replace the album bibles with your own, create your own continuity rules. See SOP 04 for setting up your own concept album.

---

## Contributing

The system separates **universal** (~70%) from **personal** (~30%) content. Universal works for anyone. Personal is your albums, preferences, and rules.

Contributions welcome: new genre skills, verified Suno tag findings, new SOPs, bug fixes, example album bibles. See SOP 08 for the full guide.

---

**Questions?** Happy to answer anything about the system, the methodology, or how to adapt it for your workflow.

**Repo:** https://github.com/Voletek/songwriting-kb

---

## POST END

---

*Note: This post is ~800 words. Discord has a 2000-character limit per message for non-Nitro users. You may need to split this across 2-3 messages, or post the intro + link and let the README do the heavy lifting. The natural split points are after "What's Inside," after "The Critic Agent," and after "Suno v5.5 Integration."*
