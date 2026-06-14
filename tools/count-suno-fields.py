#!/usr/bin/env python3
"""Count Suno Style Prompt and Lyrics fields in repository song markdown files."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

STYLE_LIMIT = 1000
LYRICS_LIMIT = 5000
WARN_RATIO = 0.9

STYLE_RE = re.compile(r"^#{1,3}\s*STYLE PROMPT:?\s*$|^STYLE PROMPT:?\s*$", re.IGNORECASE)
LYRICS_RE = re.compile(r"^#{1,3}\s*LYRICS:?\s*$|^LYRICS:?\s*$", re.IGNORECASE)
PRODUCTION_RE = re.compile(r"^#{1,3}\s*PRODUCTION NOTES:?\s*$|^PRODUCTION NOTES:?\s*$", re.IGNORECASE)


def find_line(lines: list[str], pattern: re.Pattern[str], start: int = 0) -> int | None:
    for idx in range(start, len(lines)):
        if pattern.match(lines[idx].strip()):
            return idx
    return None


def count_chars(text: str) -> int:
    return len(text.strip())


def status(count: int, limit: int) -> str:
    if count > limit:
        return "OVER"
    if count >= int(limit * WARN_RATIO):
        return "WARN"
    return "OK"


def analyze_file(path: Path, style_limit: int, lyrics_limit: int) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    style_idx = find_line(lines, STYLE_RE)
    lyrics_idx = find_line(lines, LYRICS_RE)
    prod_idx = find_line(lines, PRODUCTION_RE, (lyrics_idx or 0) + 1)

    errors: list[str] = []
    if style_idx is None:
        errors.append("Missing STYLE PROMPT section")
    if lyrics_idx is None:
        errors.append("Missing LYRICS section")

    style_text = ""
    lyrics_text = ""
    if style_idx is not None:
        end = lyrics_idx if lyrics_idx is not None and lyrics_idx > style_idx else len(lines)
        style_text = "\n".join(lines[style_idx + 1 : end])
    if lyrics_idx is not None:
        end = prod_idx if prod_idx is not None and prod_idx > lyrics_idx else len(lines)
        lyrics_text = "\n".join(lines[lyrics_idx + 1 : end])

    style_count = count_chars(style_text)
    lyrics_count = count_chars(lyrics_text)
    style_status = status(style_count, style_limit) if style_idx is not None else "MISSING"
    lyrics_status = status(lyrics_count, lyrics_limit) if lyrics_idx is not None else "MISSING"
    overall = "FAIL" if errors or style_status == "OVER" or lyrics_status == "OVER" else "PASS"

    return {
        "path": str(path),
        "style": {"count": style_count, "limit": style_limit, "status": style_status},
        "lyrics": {"count": lyrics_count, "limit": lyrics_limit, "status": lyrics_status},
        "errors": errors,
        "overall": overall,
    }


def print_text(results: list[dict[str, Any]]) -> None:
    for item in results:
        print(f"{item['overall']} {item['path']}")
        print(f"  Style: {item['style']['count']}/{item['style']['limit']} {item['style']['status']}")
        print(f"  Lyrics: {item['lyrics']['count']}/{item['lyrics']['limit']} {item['lyrics']['status']}")
        for err in item["errors"]:
            print(f"  ERROR: {err}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Song markdown files to check")
    parser.add_argument("--style-limit", type=int, default=STYLE_LIMIT)
    parser.add_argument("--lyrics-limit", type=int, default=LYRICS_LIMIT)
    parser.add_argument("--json", action="store_true", help="Emit JSON results")
    args = parser.parse_args(argv)

    results: list[dict[str, Any]] = []
    for path in args.files:
        if not path.exists():
            results.append({
                "path": str(path),
                "style": {"count": 0, "limit": args.style_limit, "status": "MISSING"},
                "lyrics": {"count": 0, "limit": args.lyrics_limit, "status": "MISSING"},
                "errors": ["File does not exist"],
                "overall": "FAIL",
            })
            continue
        results.append(analyze_file(path, args.style_limit, args.lyrics_limit))

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_text(results)

    return 1 if any(item["overall"] == "FAIL" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
