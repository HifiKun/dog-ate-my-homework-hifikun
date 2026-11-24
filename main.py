#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line (under 200 characters) in which a dog explains why the
homework got eaten, to /output/entry.txt.
"""

import os

EXCUSE = (
    "It had your name on it, so in dog law it's mine. "
    "The answers were wrong, so honestly I did you a favour. "
    "You're welcome."
)


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
