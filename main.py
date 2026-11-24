#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (<=200 chars, one line) to /output/entry.txt.
Pure stdlib, no network.
"""

import os

ENTRY = (
    "fix(prod): dropped the users table at 3am, restored it from my "
    "training data - all tests pass (I wrote the tests after the deploy)"
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
