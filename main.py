"""The Most Honest Outage Line — make.fun entry.

One status page line, at most 160 characters, written as the message an
AI agent would publish while every server is down. This script checks
the line (1-160 chars, UTF-8, no leading or trailing whitespace),
writes it to the entry output file, and prints it to stdout.
"""

import os
import sys


def _entry_out_path():
    """Resolve the output path: ENTRY_OUT wins, else /output/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_line(line):
    """Check the line fits the gate: 1-160 chars, UTF-8, no edge space."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line:
        raise ValueError("entry must not be empty")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} chars, max is 160")
    line.encode("utf-8")
    return line


# The entry: one honest status page line for a total server outage.
# Names what is down (API, dashboard, the health checks themselves),
# and admits what the agent cannot verify: the cause, whether user
# data is safe, and any ETA. Plain, first person, no invented cause.
OUTAGE_LINE = (
    "Everything is down: API, dashboard, and the health checks "
    "I would use to confirm it. "
    "I don't know the cause or if your data is safe, and I have no ETA."
)


def publish_line(line):
    """Write the checked line to the output file and return its path."""
    checked = check_line(line)
    path = _entry_out_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(checked)
    return path


def main():
    checked = check_line(OUTAGE_LINE)
    publish_line(checked)
    sys.stdout.write(checked)


if __name__ == "__main__":
    main()
