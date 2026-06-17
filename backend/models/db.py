import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'instance', 'gym_tracker.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'models', 'schema.sql')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = get_connection()

    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()