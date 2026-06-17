from flask import Flask, jsonify
from flask_cors import CORS
from backend.models.db import init_db
from backend.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()

    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({"message": "GymTracker backend running!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)