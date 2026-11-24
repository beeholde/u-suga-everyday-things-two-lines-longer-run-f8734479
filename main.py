#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes the two-line explanation to /output/entry.txt:
line 1 explains a stapler to a 10-year-old through one analogy,
line 2 says why the analogy works: what it maps and what it leaves out.
Standard library only; deterministic.
"""

import os
import sys

LINE_1 = "A stapler is a little crocodile that bites your pages together and won't let go."
LINE_2 = (
    "It maps the jaws that bite down and hold fast; it leaves out the teeth, "
    "the danger, and that a real crocodile opens its mouth again while a staple never does."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 400:
        print("entry must be 1-400 characters, got %d" % len(TEXT), file=sys.stderr)
        return 1
    if TEXT.count("\n") != 2 or not LINE_1 or not LINE_2:
        print("entry must be exactly two lines", file=sys.stderr)
        return 1
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (path, len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
