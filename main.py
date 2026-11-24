"""Developer excuse entry for make.fun.

Writes one funny single-line excuse a developer gives when code breaks
in production to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library only; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "The deploy worked on my machine. My machine has since been promoted "
    "to production, and I have been demoted to on-call."
)
# The line is 118 characters, under the competition's 200-character cap.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
