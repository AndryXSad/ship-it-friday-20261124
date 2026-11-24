"""Ship It Friday — one-line commit message entry.

Writes the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Deterministic, standard library only, never writes into the repo.
"""

import os

ENTRY = "feat: merged my own PR at 4:59 PM Friday \u2014 the tests passed in my heart"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
