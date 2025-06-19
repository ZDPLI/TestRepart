from __future__ import annotations
from typing import List, Tuple
from PIL import Image


def process_vision_info(messages: list[dict]) -> Tuple[list[Image.Image], list]:
    """Extract images from chat messages for the processor."""
    images: List[Image.Image] = []
    for msg in messages:
        for part in msg.get("content", []):
            if part.get("type") == "image":
                try:
                    images.append(Image.open(part["image"]))
                except Exception:
                    continue
    return images, []
