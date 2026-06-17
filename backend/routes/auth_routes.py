from backend.controllers.auth_controller import register, login, me, logout
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    response, status_code = register(data)
    return jsonify(response), status_code

@auth_bp.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    response, status_code = login(data)
    return jsonify(response), status_code

@auth_bp.route('/me', methods=['POST'])
def me_route():
    data = request.get_json()
    response, status_code = me()
    return jsonify(response), status_code

@auth_bp.route('/logout', methods=['POST'])
def logout_route():
    response, status_code = logout()
    return jsonify(response), status_code