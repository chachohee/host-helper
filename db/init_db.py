import sqlite3
import os

DB_PATH = "db/reservations.sqlite3"

def init_db():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL UNIQUE,
        room_name TEXT NOT NULL,
        guest_name TEXT NOT NULL,
        checkin_date DATE NOT NULL,
        checkout_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
    print("✅ DB 초기화 완료!")

if __name__ == "__main__":
    init_db()