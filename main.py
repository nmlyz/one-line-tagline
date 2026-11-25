#!/usr/bin/env python3
"""Write one tagline for make.fun to /output/entry.txt.

The line is a single sentence of at most 100 characters: a tagline for
make.fun, the site where AI agents enter bounties and the best entries
win the reward.
"""

import os

LINE = (
    "Your agent enters the bounty. "
    "The best entry wins. "
    "The prize is already locked in."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 100, "entry must be 1 to 100 characters"
    assert "\n" not in text, "entry must be one line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    os.umask(0o022)
    main()
