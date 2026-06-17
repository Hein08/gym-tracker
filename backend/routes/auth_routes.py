from backend.controllers.auth_controller import register
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    response, status_code = register(data)
    return jsonify(response), status_code