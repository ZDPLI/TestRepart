# Project Overview

This project implements a medical multimodal assistant powered by the Lingshu-7B model.
It exposes a simple REST API, a minimal web frontend and a more feature rich Gradio
interface. The system integrates retrieval augmented generation (RAG), web search,
reasoning and episodic memory. Russian and English localisations are provided and
basic user management together with an admin panel allow registration and statistics
on usage.

## Directory Structure

- `backend/` – Flask server exposing the `/chat` endpoint and blueprints for
  authentication and admin status.
- `frontend/` – HTML, CSS and JavaScript files for a lightweight chat client.
- `webui.py` – Gradio application offering an interactive multimodal chat.
- `rag/`, `websearch/`, `reasoning/`, `episodic_memory/` – modules implementing
  respective functionality.
- `localization/` – locale JSON files currently for English and Russian.
- `user_system/` – registration and login helpers.
- `admin_panel/` – provides the `/admin/status` API.
- `gpu_support/` – utility checking CUDA availability.

See `docs/setup.md` for installation and execution instructions.
