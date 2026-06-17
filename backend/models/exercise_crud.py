from backend.models.db import get_connection

def create_exercise(user_id, name, weight_type, primary_muscle_group, secondary_muscle_group = None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO exercises (user_id, name, primary_muscle_group, secondary_muscle_group, weight_type)
            VALUES (?, ?, ?, ?, ?)""",
            (user_id, name, primary_muscle_group, "NULL" if secondary_muscle_group == None else secondary_muscle_group, weight_type)
        )

        conn.commit()
        exercise_id = cursor.lastrowid
        return exercise_id
    
def get_exercise_by_name(user_id, name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM exercises WHERE user_id = ? AND name = ?""",
            (user_id, name)
        )
        return cursor.fetchall()