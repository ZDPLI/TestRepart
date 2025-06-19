from flask import Blueprint, request, jsonify
import json
import os
import secrets
from werkzeug.security import generate_password_hash, check_password_hash

USER_DB = os.getenv("USER_DB", "user_system/users.json")

_tokens: dict[str, str] = {}


def _load_users() -> dict:
    if os.path.exists(USER_DB):
        with open(USER_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_users(users: dict) -> None:
    os.makedirs(os.path.dirname(USER_DB), exist_ok=True)
    with open(USER_DB, "w", encoding="utf-8") as f:
        json.dump(users, f)

bp = Blueprint('auth', __name__)


def verify_token(token: str) -> str | None:
    """Return username associated with *token* or None."""
    return _tokens.get(token)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'missing credentials'}), 400
    users = _load_users()
    if username in users:
        return jsonify({'error': 'user exists'}), 400
    users[username] = generate_password_hash(password)
    _save_users(users)
    return jsonify({'status': 'registered'})

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('password')
    users = _load_users()
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'error': 'invalid credentials'}), 401
    token = secrets.token_hex(16)
    _tokens[token] = username
    return jsonify({'token': token})


@bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if token and token in _tokens:
        _tokens.pop(token, None)
        return jsonify({'status': 'logged_out'})
    return jsonify({'error': 'invalid token'}), 401
