# Medical Multimodal Assistant Chatbot

This project provides a skeleton implementation of a web-based medical assistant chatbot powered by the `Lingshu-7B-GGUF` model. It includes placeholders for features such as retrieval augmented generation (RAG), web search integration, a long chain-of-thought reasoning system, episodic memory, localization, user management, and an admin panel.

## Project Structure

- `frontend/` – simple web interface files
- `backend/` – Flask backend serving the chatbot API
- `rag/`, `websearch/`, `reasoning/`, `episodic_memory/` – placeholders for core assistant features
- `localization/` – example locale JSON files
- `user_system/`, `admin_panel/` – entry points for user management and admin tooling
- `gpu_support/` – utilities for GPU detection

Each folder currently provides only minimal code so that future development can easily build upon it.

## Running

Install dependencies from `requirements.txt` and launch the backend or the demo Gradio interface:

```bash
pip install -r requirements.txt
python backend/app.py  # simple API
python webui.py        # Gradio web interface
```

Then open `frontend/index.html` in a browser to interact with the placeholder chatbot interface.

