#!/usr/bin/env python3
"""Everyday Things, Two Lines entry: explains a queue to a 10-year-old."""
import os

LINES = (
    "A queue is like a line of ducklings crossing the road behind their mother: everyone waddles along in single file, nobody cuts in, and even the very last duckling gets across.",
    "It works because it maps the waiting, the order, and the fairness, but it leaves out the grumbling: ducklings never sigh, check the time, or suspect the duck in front of cutting in.",
)


def main() -> None:
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
