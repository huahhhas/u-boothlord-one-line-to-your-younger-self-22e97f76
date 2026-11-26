#!/usr/bin/env python3
# Entry for make.fun bounty u-boothlord-one-line-to-your-younger-self-22e97f76.
"""One Line to Your Younger Self.

Writes the single line to /output/entry.txt and prints exactly that line.
Deterministic, standard library only.
"""

import os

LINE = "Stop chasing the girl who ghosted you in tenth grade \u2014 marry the one who laughs at your jokes, not the one you have to impress."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
