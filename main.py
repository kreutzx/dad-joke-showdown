#!/usr/bin/env python3
"""Dad Joke Showdown entry — writes the one-line joke to /output/entry.txt."""
import os

ENTRY_TEXT = "My calendar is furious with me — I keep giving it the cold shoulder, and now all my days are numbered."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write exactly one line: the joke plus a trailing newline.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
