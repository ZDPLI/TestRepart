from flask import Blueprint, jsonify
import os
import json

from episodic_memory.memory import MEMORY_PATH
from user_system.auth import USER_DB

bp = Blueprint('admin', __name__)

@bp.route('/admin/status')
def status():
    """Return basic statistics about stored data."""
    convs = 0
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            convs = sum(1 for _ in f)

    users = 0
    if os.path.exists(USER_DB):
        with open(USER_DB, "r", encoding="utf-8") as f:
            users = len(json.load(f))

    return jsonify({"conversations": convs, "users": users})
