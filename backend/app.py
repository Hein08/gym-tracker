from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({"message": "GymTracker backend running!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)