"""Five Seconds to Explain the Glass entry.

Writes one original line, in the cat's own voice, after sweeping a
glass off the table, to /output/entry.txt (or to the directory named
by MAKEFUN_OUTPUT_DIR when the grader sets it).

No apology, no confession: the cat makes its case with territorial
logic — the glass was squatting in its sunbeam for three hours
without paying rent, so it got evicted. The line is short enough
to say in five seconds, and the eviction is the twist.
"""

import os

ENTRY = "That glass sat in my sunbeam for three hours without paying rent, so I evicted it."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"Entry must be 1 to 200 characters, got {len(entry)}")
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
