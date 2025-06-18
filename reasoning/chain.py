"""Minimal chain-of-thought reasoning over chat messages."""

from __future__ import annotations

import os
from llama_cpp import Llama


MODEL_DIR = os.getenv("LINGSHU_MODEL_DIR", "models")
GGUF_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.Q8_0.gguf")
MMPROJ_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.mmproj-f16.gguf")

_model = None


def _load() -> None:
    """Initialise the llama.cpp model if it hasn't been loaded yet."""
    global _model
    if _model is None:
        n_gpu_layers = int(os.getenv("N_GPU_LAYERS", "0"))
        _model = Llama(model_path=GGUF_PATH, n_gpu_layers=n_gpu_layers)
        if os.path.exists(MMPROJ_PATH):
            # Load mm projection weights if available (not used directly by llama.cpp)
            with open(MMPROJ_PATH, "rb"):
                pass


def reason(messages: list[dict], system_prompt: str, max_new_tokens: int = 256) -> str:
    """Use the Lingshu model to reason over *messages* and produce a reply."""
    _load()

    conversation = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    prompt = f"{system_prompt}\n{conversation}\nassistant:"

    result = _model.create_completion(
        prompt,
        max_tokens=max_new_tokens,
        temperature=0.7,
        top_p=1,
        stop=["user:", "assistant:"],
        stream=False,
    )

    return result["choices"][0]["text"].strip()
