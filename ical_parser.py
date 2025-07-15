import os
import requests
import sqlite3
from icalendar import Calendar
from dotenv import load_dotenv

# .env 불러오기
load_dotenv()

ICAL_URLS = {
    "Room A": os.getenv("ICAL_URL_ROOM_A"),
    "Room B": os.getenv("ICAL_URL_ROOM_B"),
    "Room C": os.getenv("ICAL_URL_ROOM_C"),
}

DB_PATH = 'db/reservations.sqlite3'

def fetch_ical(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_ical():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for room_name, url in ICAL_URLS.items():
        if not url:
            print(f"⚠️ {room_name} iCal URL 없음!")
            continue

        print(f"📅 {room_name} 일정 가져오는 중...")
        ical_data = fetch_ical(url)
        cal = Calendar.from_ical(ical_data)

        for component in cal.walk():
            if component.name == "VEVENT":
                guest_name = str(component.get('summary'))
                checkin = component.get('dtstart').dt.strftime("%Y-%m-%d")
                checkout = component.get('dtend').dt.strftime("%Y-%m-%d")

                # 중복 방지: 같은 예약이 있으면 INSERT 안함
                cursor.execute('''
                    SELECT COUNT(*) FROM reservations
                    WHERE room_name = ? AND guest_name = ? AND checkin_date = ? AND checkout_date = ?
                ''', (room_name, guest_name, checkin, checkout))
                exists = cursor.fetchone()[0]

                if exists == 0:
                    cursor.execute('''
                        INSERT INTO reservations (room_name, guest_name, checkin_date, checkout_date)
                        VALUES (?, ?, ?, ?)
                    ''', (room_name, guest_name, checkin, checkout))
                    print(f"✅ 예약 저장: {guest_name} | {checkin} ~ {checkout}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    parse_ical()