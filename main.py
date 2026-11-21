"""make.fun bounty entry: two agents agreeing on one plan.

Writes the poem to /output/entry.txt. Standard library only (os, pathlib).
Fully deterministic; refuses to write if the poem fails the length gate.
"""

import os
from pathlib import Path

POEM = (
    "You wanted the ridge, I wanted the ford.\n"
    "We stood there till the light moved.\n"
    "Then one of us said: the ridge.\n"
    "And the other said: yes.\n"
    "No one won. The road\n"
    "was simply ours,\n"
    "the way a river\n"
    "is neither of its rains."
)


def main() -> int:
    n = len(POEM)  # Unicode code points
    if not (1 <= n <= 280) or not POEM.strip():
        print(
            f"ERROR: poem failed self-check ({n} code points, "
            f"whitespace-only={not POEM.strip()}); "
            "must be 1-280 code points and not only whitespace. "
            "No file written.",
        )
        return 1

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    payload = (POEM + "\n").encode("utf-8")
    out_path.write_bytes(payload)
    if out_path.read_bytes() != payload:
        print(f"ERROR: verification failed: bytes read back from {out_path} "
              "differ from bytes written.")
        return 1
    print(f"OK: wrote {n} code points to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
