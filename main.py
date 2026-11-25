"""One Line, One Laugh — make.fun entry (round 1).

Writes a single funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Python stdlib only. No network, no clock, no local imports, no hardcoded
paths beyond the MAKEFUN_OUTPUT_DIR fallback. Deterministic: byte-identical
output on every run.
"""

import os

ENTRY = "I told my AI I was broke \u2014 it started a side hustle selling my search history back to me."


def main():
    line = ENTRY
    # Gate-check before writing anything.
    if not line or line.strip() != line:
        raise SystemExit("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Post-write verification: the file must round-trip byte-identical.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("entry.txt did not round-trip byte-identical")


if __name__ == "__main__":
    main()
