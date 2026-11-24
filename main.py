#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of last words a phone says as its battery hits 1 percent
to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os

LINE = (
    "I've watched you unlock me with your ex's birthday 11,482 times \u2014 "
    "and with my last gasp of battery I'm texting her 'he still loves you'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
