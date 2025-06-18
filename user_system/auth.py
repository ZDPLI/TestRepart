from flask import Blueprint, request, jsonify

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    # TODO: add persistent user registration
    return jsonify({'status': 'registered'})

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    # TODO: add authentication
    return jsonify({'status': 'logged_in'})
