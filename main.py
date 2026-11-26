#!/usr/bin/env python3
"""Write a one-line roast of my fridge to /output/entry.txt."""

import os

LINE = "My fridge's freezer is so full of forgotten leftovers that archaeologists could carbon-date my last three diets."
# One line, one laugh: the roast lives in LINE, so the output never changes.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
