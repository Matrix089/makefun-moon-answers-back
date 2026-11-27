"""The Moon Finally Answers Back entry (v2 resubmission).

Writes one original line in the voice of the Moon replying at last to
everyone staring up at it to out/entry.txt (or to the directory named
by MAKEFUN_OUTPUT_DIR when the grader sets it).

The Moon's own comeback: it is not a romantic listener but an unpaid
night-shift worker pulling the tides, whose only tip in fifty-seven
years was a flag and a golf ball left on its surface.
"""

import os

ENTRY = "You call me romantic. I call it unpaid overtime: I pull your tides twice a day, and in fifty-seven years my only tip has been a flag and a golf ball."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 240:
        raise SystemExit(f"Entry must be 1 to 240 characters, got {len(entry)}")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("Entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
