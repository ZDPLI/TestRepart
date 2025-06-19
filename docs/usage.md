# Usage Guide

The assistant can be accessed via two interfaces.

## 1. Web Frontend

Open `frontend/index.html` in your browser. Enter messages in the text box and press **Send**. The page uses the `/chat` endpoint of the backend running on the same host.

Before chatting you must register and log in to obtain an authentication token. Include this token in the `Authorization` header when the frontend or other clients call `/chat`.

## 2. Gradio Demo

Run `python webui.py` to start the Gradio interface. It supports text, images and video inputs and lets you specify a system prompt. The interface streams model output in real time.

## Localization

Strings used in the frontend can be translated. Example English and Russian JSON files are located in `localization/`. Add more locales by creating new JSON files with the same keys.
