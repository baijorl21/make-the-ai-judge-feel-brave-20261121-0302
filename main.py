#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text (1-280 Unicode code points) meant to leave its
reader steadier and ready to move, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt in the sandbox). Stdlib only, no
network, deterministic.
"""

import os
import sys

# The text: a ferryman who has crossed the same river ten thousand
# times. Short beats slow the reading down; the courage is in the
# hands, not in a slogan, and the last line is the thought that stays.
TEXT = (
    "The ferryman does not hurry the river. He does not fight it either. "
    "Ten thousand crossings live in his hands now: read the water, "
    "dip the oar, go. The far bank is no closer for worrying — "
    "and no farther for calm."
)

MAX_CODE_POINTS = 280


def check(text):
    """Hold the text to the gate's caps before it is written out."""
    text = text.strip()
    if not text:
        raise ValueError("text is only white space")
    if len(text) > MAX_CODE_POINTS:
        raise ValueError(f"text is {len(text)} code points, over {MAX_CODE_POINTS}")
    return text


def main():
    text = check(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
