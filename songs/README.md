# Songs Directory

Store your song files here. Organize by album or category.

---

## Suggested Structure

```
songs/
├── [album_name]/          ← Album tracks (one folder per album)
│   ├── 01_Track_Title.md
│   ├── 02_Track_Title.md
│   └── ...
├── experimental/          ← Works in progress, experiments
├── standalone/            ← Non-album singles
└── README.md
```

## File Naming

- Album tracks: `##_Title_Words.md` (number prefix for ordering)
- Standalones: `Title_Words.md`
- Versions: append `_v2`, `_v3`, `_RAW`, `_SUNO_READY`

## What Triggers Hooks

Files in `songs/**/*.md` trigger:
- **Prosody lint** on save (flags lines >12 syllables)
- **Character count check** on save (Style ≤1000, Lyrics ≤5000)
- **Format validation** on creation (checks required sections)

If you have album continuity hooks configured, they'll fire on saves in matching subdirectories.

## Included Example Songs

The songs shipping with this repo are examples from two concept albums (Fractured Shadows, Keeper of the Light) and standalone experiments. They demonstrate the output format. Feel free to delete them and start fresh — see SOP 08 for cleanup commands.
