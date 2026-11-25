"""Everyday Things, Two Lines — a battery as a packed lunch.

This program produces exactly two lines of plain text that explain one
everyday object (a battery) to a ten-year-old. The first line paints the
whole picture in a single vivid sentence; the second line says plainly
which parts of the picture carry over and which part it leaves out, so
the child is not left with the wrong idea.

The text comes from two fixed sentences, is checked against the bounty
gate (1-400 characters, exactly two non-empty lines), is written to the
output file, and is then read back and compared character for character
before the program reports success.
"""

import os
import sys

# The two sentences of the entry. Their wording is fixed by the brief;
# only the program around them may change.
FIRST = "A battery is a packed lunch your toy carries inside, full of power it uses up bit by bit."
SECOND = "It maps power stored up beforehand that runs out until you swap in a fresh pack; it leaves out the eating: a toy never chews, it just spends power until the lunch is gone."

MIN_CHARS = 1
MAX_CHARS = 400


def join_lines():
    """Return the entry as a single string ending with a newline."""
    return FIRST + "\n" + SECOND + "\n"


def check_entry(text):
    """Stop with a message if the text breaks any part of the gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        sys.exit(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")
    rows = text.split("\n")
    if rows and rows[-1] == "":
        rows = rows[:-1]
    if len(rows) != 2:
        sys.exit(f"entry must be exactly 2 lines, got {len(rows)}")
    if any(row.strip() == "" for row in rows):
        sys.exit("entry lines must not be blank")
    if "\r" in text:
        sys.exit("entry must use plain newlines, no carriage returns")
    if any(row != row.rstrip() for row in rows):
        sys.exit("entry lines must not end with trailing spaces")


def out_path():
    """Pick the output file: the harness directory when set, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def publish(text):
    """Write the text, then read it back and confirm it matches."""
    path = out_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != text:
        sys.exit("read-back mismatch: stored text differs from entry")
    return path


def main():
    text = join_lines()
    check_entry(text)
    path = publish(text)
    print(f"wrote {len(text)} chars, 2 lines -> {path}")


if __name__ == "__main__":
    main()
