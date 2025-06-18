from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Placeholder system prompt optimizing the model for doctor's assistant behavior.
SYSTEM_PROMPT = "You are a helpful medical assistant."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    user_message = data.get('message', '')
    # Placeholder response: echo message.
    reply = f"{SYSTEM_PROMPT} Echo: {user_message}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
