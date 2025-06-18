"""Minimal chain-of-thought reasoning over chat messages."""

from __future__ import annotations

import os
import torch
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration


MODEL_DIR = os.getenv("LINGSHU_MODEL_DIR", "models")
GGUF_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.Q8_0.gguf")
MMPROJ_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.mmproj-f16.gguf")

_model = None
_processor = None


def _load():
    global _model, _processor
    if _model is None:
        _model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_DIR,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            mmproj_file=MMPROJ_PATH,
            local_files_only=True,
        )
        _processor = AutoProcessor.from_pretrained(MODEL_DIR, local_files_only=True)


def reason(messages: list[dict], system_prompt: str, max_new_tokens: int = 256) -> str:
    """Use the Lingshu model to reason over *messages* and produce a reply."""
    _load()
    prompt = [{"role": "system", "content": system_prompt}] + messages
    text = _processor.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True)
    inputs = _processor(text=[text], return_tensors="pt").to(_model.device)
    outputs = _model.generate(**inputs, max_new_tokens=max_new_tokens)
    return _processor.batch_decode(outputs, skip_special_tokens=True)[0]
