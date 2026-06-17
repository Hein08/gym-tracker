from backend.models.db import get_connection

def create_user(email, password_hash, first_name, last_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (email, password_hash, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (email, password_hash, first_name, last_name))

    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return user_id

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ?',
                   (email,))
    
    user = cursor.fetchone()
    conn.close()

    return user

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?',
                   (user_id,))
    
    user = cursor.fetchone()
    conn.close()

    return user