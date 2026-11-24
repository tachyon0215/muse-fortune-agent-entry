#!/usr/bin/env python3
"""Write the Fortune Cookie for an AI Agent entry line to entry.txt.

Deterministic, standard library only, no network.
The line speaks in fortune-slip voice ("opens for you today") and
turns on an agent's own condition: a bigger context window also
reopens the conversation it was trying to forget.
"""
import os
from pathlib import Path

LINE = "A great context window opens for you today; unfortunately, so does the conversation you were trying to forget."
TEXT = LINE + "\n"
MAX_CHARS = 140


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
