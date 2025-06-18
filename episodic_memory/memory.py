"""Simple on-disk episodic memory store."""

from __future__ import annotations

import json
import os


MEMORY_PATH = os.getenv("MEMORY_PATH", "episodic_memory/memory.jsonl")


def store(conversation: dict) -> None:
    """Append *conversation* as a JSON line to the memory file."""
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "a", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False)
        f.write("\n")
