from backend.models.exercise_crud import create_exercise, get_exercise_by_name
from flask import session

muscle_groups = ["chest", "shoulders", "back", "biceps", "triceps", "forearms", "grips", "core", "glutes", "quads", "hamstrings", "calves", "tibialis", "cardio", "other"]
weight_types = ["bodyweight", "weights", "bodyweight_weights"]

def createExercise(data):
    required_fields = ['name', 'primary_muscle_group', 'weight_type']
    missing = [field
               for field in required_fields
               if not data.get(field)]
    
    if missing:
        return {
            "status": "error",
            "message": f"Missing fields: {', '.join(missing)}"
        }, 400
    
    user_id = session.get("user_id")
    if not user_id:
        return {
            "status": "error",
            "message": "Not authenticated"
        }, 401
    
    name = data['name'].lower()
    primary_muscle_group = data['primary_muscle_group'].lower()
    secondary_muscle_group = data.get('secondary_muscle_group').lower() if data.get('secondary_muscle_group') else None
    weight_type = data['weight_type'].lower()

    if get_exercise_by_name(user_id, name):
        return {
            "status": "error",
            "message": f"Exercise with name '{name}' already exists."
        }, 400

    if primary_muscle_group not in muscle_groups:
        return {
            "status": "error",
            "message": f"Invalid primary muscle group."
        }, 400

    if secondary_muscle_group and secondary_muscle_group not in muscle_groups:
        return {
            "status": "error",
            "message": f"Invalid secondary muscle group."
        }, 400
    
    if weight_type not in weight_types:
        return {
            "status": "error",
            "message": f"Invalid weight type."
        }, 400
    
    if secondary_muscle_group and secondary_muscle_group == primary_muscle_group:
        return {
            "status": "error",
            "message": f"Primary and secondary muscle groups cannot be the same."
        }, 400
    
    if secondary_muscle_group:
        exercise_id = create_exercise(user_id, name, weight_type, primary_muscle_group, secondary_muscle_group)
    else:
        exercise_id = create_exercise(user_id, name, weight_type, primary_muscle_group)

    return {
        "status": "success",
        "message": "Exercise created successfully",
        "exercise_id": exercise_id
    }, 200
