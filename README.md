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

Install dependencies from `requirements.txt`. Download the Lingshu model
repository and place it in a `models/` directory (or point the
`LINGSHU_MODEL_DIR` environment variable to that directory). The directory
should contain the `Lingshu-7B.Q8_0.gguf` file together with the
`Lingshu-7B.mmproj-f16.gguf` projection weights. The application loads the model
with `transformers` and automatically uses the GPU when available. Then launch
the backend or the demo Gradio interface:

```bash
pip install -r requirements.txt
python backend/app.py  # simple API
python webui.py        # Gradio web interface
```

Then open `frontend/index.html` in a browser to interact with the chatbot interface.

Authentication is token-based. Register and login first:

```bash
curl -X POST http://localhost:5000/auth/register -H 'Content-Type: application/json' \
  -d '{"username":"user","password":"pass"}'
curl -X POST http://localhost:5000/auth/login -H 'Content-Type: application/json' \
  -d '{"username":"user","password":"pass"}'
```

The login request returns a token which must be provided in the `Authorization`
header when calling `/chat`.

### System Prompt

The application ships with a default prompt optimised for helping general practitioners. It
is automatically applied in the Gradio demo but can be overridden if needed.


## Documentation

Detailed documentation can be found in the `docs/` directory:

- [Overview](docs/overview.md)
- [Setup guide](docs/setup.md)
- [API reference](docs/api.md)
- [Usage guide](docs/usage.md)
- [Admin guide](docs/admin.md)
