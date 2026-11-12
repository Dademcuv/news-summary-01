#!/usr/bin/env python3
"""Write the prepared news summary to the grader's output directory.

Reads summary.txt sitting next to this script and writes its exact bytes
to <output_dir>/entry.txt, where output_dir comes from the
MAKEFUN_OUTPUT_DIR environment variable (default: /output).
Standard library only, no network access. Deterministic: every run
produces byte-identical output.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    summary_path = here / "summary.txt"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    data = summary_path.read_bytes()
    (output_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
