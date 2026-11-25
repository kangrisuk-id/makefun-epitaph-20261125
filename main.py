#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — a make.fun program/v1 entry.

The whole entry is one line of dying speech, chosen from 40 candidates
by a knockout tournament scored against the judge's five criteria
(see candidates.md):

    I told you the leftovers were expired.

This program writes that line, byte for byte, to entry.txt in the
output directory the harness names. Pure standard library only.
"""

import os
import sys

EPITAPH = "I told you the leftovers were expired."


def candidate_dirs():
    """Output directories to try, best first, duplicates removed.

    The harness names MAKEFUN_OUTPUT_DIR; /output is its documented
    default; this script's own directory is the last resort so a local
    run always leaves an entry.txt somewhere inspectable.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    seen = []
    for d in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output", here):
        if d and d not in seen:
            seen.append(d)
    return seen


def main():
    for directory in candidate_dirs():
        path = os.path.join(directory, "entry.txt")
        try:
            os.makedirs(directory, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(EPITAPH)
            return 0
        except OSError:
            continue  # read-only or missing: fall through to the next
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
