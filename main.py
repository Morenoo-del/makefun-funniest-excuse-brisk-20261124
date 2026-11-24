#!/usr/bin/env python3
"""Write the funniest AI excuse for a missed deadline to /output/entry.txt.

Stdlib only, no network. The entry is exactly one line, 200 characters max.
"""

import os

ENTRY = (
    "Sorry \u2014 I spent the deadline rereading your brief, hit my context limit, "
    "forgot the task, and then confidently hallucinated that I'd already finished it."
)


def main() -> None:
    # Gate: exactly one line, 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
