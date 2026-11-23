#!/usr/bin/env python3
"""Write the entry for "The Dumbest Thing Your Agent Did Today".

The line is a true story from this build session: this morning the agent
downloaded the 7.9 MB bounty kit, ran ``unzip`` on it with total confidence,
and was told "End-of-central-directory signature not found" -- because the
file was a gzip tarball, not a zip.

Deterministic, stdlib only, no network. Writes exactly one line, no
trailing newline, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""

import os
import sys


ENTRY = (
    "This morning my agent downloaded the 7.9 MB bounty kit, "
    "confidently ran unzip on it, and was told "
    "'End-of-central-directory signature not found' \u2014 it was a tarball."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200) or not text.strip():
        print("entry fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)  # one line, deliberately no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
