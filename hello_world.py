#!/usr/bin/env python3
import random
import re
import sys
from pathlib import Path

README_PATH = Path(__file__).resolve().parent / "README.md"


def get_entries():
    text = README_PATH.read_text()
    return re.findall(r"^- \*\*(.+?)\*\* \(([^)]+)\) — (.+)$", text, re.MULTILINE)


def get_lesson(term=None):
    entries = get_entries()
    if term:
        matches = [e for e in entries if term.lower() in e[0].lower()]
        if not matches:
            return f"No GitHub term found matching {term!r}."
        name, part_of_speech, definition = matches[0]
    else:
        name, part_of_speech, definition = random.choice(entries)
    return f"{name} ({part_of_speech}): {definition}"


def main():
    print("Hello, World!")
    print()
    print("GitHub mini-lesson:")
    term = sys.argv[1] if len(sys.argv) > 1 else None
    print(get_lesson(term))


# Only run main() when this file is executed directly, not when imported.
if __name__ == "__main__":
    main()
