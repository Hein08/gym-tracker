from flask import Blueprint, request
from backend.controllers.exercise_controller import createExercise

exercise_bp = Blueprint('exercise_routes', __name__)

@exercise_bp.route('/', methods=['POST'])
def create_exercise_route():
    data = request.get_json()
    response, status_code = createExercise(data)
    return response, status_code