from flask import Flask, request, jsonify
import os
import torch
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

from rag.loader import load_documents
from websearch.search import search_web
from reasoning.chain import reason
from episodic_memory.memory import store
from user_system.auth import bp as auth_bp
from admin_panel.panel import bp as admin_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(admin_bp, url_prefix="/")

MODEL_DIR = os.getenv("LINGSHU_MODEL_DIR", "models")
GGUF_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.Q8_0.gguf")
MMPROJ_PATH = os.path.join(MODEL_DIR, "Lingshu-7B.mmproj-f16.gguf")

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    GGUF_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    mmproj_file=MMPROJ_PATH,
    local_files_only=True,
)
processor = AutoProcessor.from_pretrained(GGUF_PATH, local_files_only=True)

SYSTEM_PROMPT = "You are a helpful medical assistant."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '')
    docs_path = data.get('docs_path')
    docs = load_documents(docs_path) if docs_path else []
    search_snippets = search_web(message)

    convo = [
        {'role': 'user', 'content': message}
    ]
    if docs:
        convo.append({'role': 'user', 'content': ' '.join(docs)})
    if search_snippets:
        convo.append({'role': 'user', 'content': search_snippets})

    reply = reason(convo, system_prompt=SYSTEM_PROMPT)
    store({'message': message, 'reply': reply})
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
