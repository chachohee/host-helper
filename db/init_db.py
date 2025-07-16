import sqlite3
import os

# DB 경로
DB_PATH = 'db/reservations.sqlite3'

# db 폴더 없으면 만들기
if not os.path.exists('db'):
    os.makedirs('db')

# 연결
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# reservations 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_name TEXT NOT NULL,
        guest_name TEXT NOT NULL,
        checkin_date TEXT NOT NULL,
        checkout_date TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

print("✅ DB 초기화 완료!")