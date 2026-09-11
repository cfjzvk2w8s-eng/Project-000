#!/usr/bin/env python3
import random
import re
from pathlib import Path

README_PATH = Path(__file__).resolve().parent / "README.md"


def get_lesson():
    text = README_PATH.read_text()
    entries = re.findall(r"^- \*\*(.+?)\*\* \(([^)]+)\) — (.+)$", text, re.MULTILINE)
    term, part_of_speech, definition = random.choice(entries)
    return f"{term} ({part_of_speech}): {definition}"


def main():
    print("Hello, World!")
    print()
    print("GitHub mini-lesson:")
    print(get_lesson())


# Only run main() when this file is executed directly, not when imported.
if __name__ == "__main__":
    main()
