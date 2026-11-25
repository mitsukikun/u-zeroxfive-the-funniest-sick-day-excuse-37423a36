#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — entry program.

Writes one line, under 200 characters, to /output/entry.txt
(and a local copy next to this script).
"""

import os

ENTRY = (
    "Can't come in today — my contact lens fell out in the shower "
    "and I've spent the whole morning negotiating with the drain. "
    "The drain is winning."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
