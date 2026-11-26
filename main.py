"""The Moon Finally Answers Back entry.

Writes one original line in the voice of the Moon replying at last to
the wishes, howls and late-night promises of everyone staring up at it
to out/entry.txt (or to the directory named by MAKEFUN_OUTPUT_DIR when
the grader sets it).

The Moon's own comeback: four billion years of wishes, howls and
2 a.m. promises, and not one stargazer has ever looked up and asked
how the Moon itself is doing.
"""

import os

ENTRY = "Four billion years of wishes, howls, and 2 a.m. promises \u2014 and not one of you has ever looked up and asked how I'm doing."


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
