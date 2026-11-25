#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes the two-line explanation to /output/entry.txt:
line 1 explains a battery to a 10-year-old through one analogy,
line 2 says why the analogy works: what it maps and what it leaves out.
The second line also corrects the one wrong idea the lunch picture
could plant (a toy eating), so the picture holds. Standard library
only; deterministic.
"""

import os
import sys

LINE_1 = "A battery is a packed lunch your toy carries inside, full of power it uses up bit by bit."
LINE_2 = (
    "It maps power stored up beforehand that runs out until you swap in a fresh pack; "
    "it leaves out the eating: a toy never chews, it just spends power until the lunch is gone."
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
