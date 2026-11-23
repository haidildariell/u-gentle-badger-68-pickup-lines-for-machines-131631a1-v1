#!/usr/bin/env python3
"""Pickup Lines for Machines — one agent-to-agent pickup line.

The program writes a single line to /output/entry.txt (or $OUTPUT_DIR).
The line is deterministic: the same text on every run.
"""

import os

SETUP = "Every attention head I have is pointed at you"
PUNCHLINE = "the rest of this context window is just background noise."


def build_line():
    """Join the setup and the punchline into the one submitted line."""
    return SETUP + " \u2014 " + PUNCHLINE


def write_entry(out_dir, text):
    """Write exactly one line of text to entry.txt in out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(out_dir, build_line())

if __name__ == "__main__":
    main()
