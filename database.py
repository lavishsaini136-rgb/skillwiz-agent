import sqlite3
import json

DB_PATH = "students.db"

def init_db():
    """Create the students table and seed sample data."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            user_id          TEXT PRIMARY KEY,
            target           TEXT,
            current_phase    TEXT,
            completed_topics TEXT,
            pending_topics   TEXT,
            streak           INTEGER
        )
    """)
    # Seed sample student
    cur.execute("""
        INSERT OR IGNORE INTO students VALUES (
            'user_123', 'Frontend Developer', 'JavaScript Basics',
            '["Variables", "Loops"]',
            '["Promises", "Async/Await", "ES6 Modules", "DOM Manipulation"]',
            5
        )
    """)
    conn.commit()
    conn.close()

def get_student(user_id: str) -> dict | None:
    """Return a student record as a dict, or None if not found."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    data = dict(row)
    data["completed_topics"] = json.loads(data["completed_topics"])
    data["pending_topics"]   = json.loads(data["pending_topics"])
    return data
