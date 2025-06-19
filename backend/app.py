from flask import Flask, request, jsonify
import os

from rag.loader import load_documents
from websearch.search import search_web
from reasoning.chain import reason
from episodic_memory.memory import store
from user_system.auth import bp as auth_bp, verify_token
from admin_panel.panel import bp as admin_bp
from system_prompt import DEFAULT_SYSTEM_PROMPT

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(admin_bp, url_prefix="/")

MODEL_DIR = os.getenv("LINGSHU_MODEL_DIR", "models")

SYSTEM_PROMPT = DEFAULT_SYSTEM_PROMPT

@app.route('/chat', methods=['POST'])
def chat():
    token = request.headers.get('Authorization')
    if not verify_token(token or ''):
        return jsonify({'error': 'unauthorized'}), 401

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
    username = verify_token(token or '')
    store({'user': username, 'message': message, 'reply': reply})
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
