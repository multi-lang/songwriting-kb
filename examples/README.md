# Examples

> Reference implementations showing how to configure the songwriting system for your own projects.
> These files are NOT active — they're here for you to study and copy from.

---

## What's Here

### `albums/` — Complete Album Configurations

Two fully-realized concept album setups showing how every piece connects:

| Album | Genre | Tracks | Shows You |
|---|---|---|---|
| **Fractured Shadows** | Industrial → Cinematic Rock | 17 | Large multi-act album, vocal evolution, sonic pivot, named layers, character voices |
| **Keeper of the Light** | Folk-Horror / Sea-Shanty | 8 | Smaller focused album, non-vocal entity design, single Persona with delivery variants |

Each album folder contains:
- `steering.md` — The conditional steering file (copy to `.kiro/steering/` and configure `fileMatchPattern`)
- `continuity-hook.json` — The continuity check hook (copy to `.kiro/hooks/`)
- `BLUEPRINT.md` — The full album blueprint (copy to `references/`)

### `preferences/` — Format Preference Examples

- `voletek-preferences.md` — One user's complete preference configuration showing all available options filled in with real values

---

## How to Use These

### Setting Up Your Own Album

1. Read through one of the example albums to understand the structure
2. Follow **SOP 04** (Setting Up a Concept Album) to create your own
3. Copy the relevant files to their active locations:
   ```
   examples/albums/your-ref/steering.md → .kiro/steering/your-album.md
   examples/albums/your-ref/BLUEPRINT.md    → references/YOUR_ALBUM_BLUEPRINT.md
   examples/albums/your-ref/hook.json   → .kiro/hooks/your-album-continuity.json
   ```
4. Update file paths and patterns in your copies

### Customizing Preferences

1. Read `examples/preferences/voletek-preferences.md` to see a filled-in example
2. Edit `.kiro/steering/output-preferences.md` with YOUR conventions
3. The active preferences file has comments explaining each section

---

## Don't Edit These Directly

These are reference copies. Edit the ACTIVE files in `.kiro/steering/`, `.kiro/hooks/`, and `references/` instead.
