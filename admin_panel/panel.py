from flask import Blueprint, jsonify

bp = Blueprint('admin', __name__)

@bp.route('/admin/status')
def status():
    # TODO: admin functionality
    return jsonify({'admin': 'ok'})
