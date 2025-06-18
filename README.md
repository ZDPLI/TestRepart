# Medical Multimodal Assistant Chatbot

This project implements a web-based medical assistant chatbot powered by the `Lingshu-7B-GGUF` model. It includes retrieval augmented generation utilities, web search integration, a chain-of-thought reasoning system, episodic memory, localization, user management with registration and login, and a small admin panel.

## Project Structure

- `frontend/` – simple web interface files
- `backend/` – Flask backend serving the chatbot API
- `rag/`, `websearch/`, `reasoning/`, `episodic_memory/` – helper modules for the assistant
- `localization/` – example locale JSON files
- `user_system/`, `admin_panel/` – entry points for user management and admin tooling
- `gpu_support/` – utilities for GPU detection

All components provide simple yet working functionality so the project can be run end to end.

## Running

Install dependencies from `requirements.txt`. Place the model files
`Lingshu-7B.Q8_0.gguf` and `Lingshu-7B.mmproj-f16.gguf` inside a `models/` directory (or set the `LINGSHU_MODEL_DIR` environment variable to their location) and launch the backend or the demo Gradio interface:

```bash
pip install -r requirements.txt
python backend/app.py  # simple API
python webui.py        # Gradio web interface
```

Then open `frontend/index.html` in a browser to interact with the chatbot interface.


## Documentation

Detailed documentation can be found in the `docs/` directory:

- [Overview](docs/overview.md)
- [Setup guide](docs/setup.md)
- [API reference](docs/api.md)
- [Usage guide](docs/usage.md)
- [Admin guide](docs/admin.md)
