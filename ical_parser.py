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

def sync_reservations(room_name, events):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # iCal에서 가져온 UID 목록
    ical_uids = [e['uid'] for e in events]

    # 현재 DB에 저장된 UID 목록
    cursor.execute('SELECT uid FROM reservations WHERE room_name = ?', (room_name,))
    db_uids = [row[0] for row in cursor.fetchall()]

    # INSERT or UPDATE
    for event in events:
        uid = event['uid']
        guest_name = event['guest_name']
        checkin = event['checkin']
        checkout = event['checkout']

        if uid in db_uids:
            cursor.execute('''
                UPDATE reservations
                SET guest_name = ?, checkin_date = ?, checkout_date = ?
                WHERE uid = ? AND room_name = ?
            ''', (guest_name, checkin, checkout, uid, room_name))
            print(f"♻️ 예약 업데이트: {guest_name} | {checkin} ~ {checkout}")
        else:
            cursor.execute('''
                INSERT INTO reservations (uid, room_name, guest_name, checkin_date, checkout_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (uid, room_name, guest_name, checkin, checkout))
            print(f"✅ 예약 저장: {guest_name} | {checkin} ~ {checkout}")

    # DELETE - DB에만 있는 UID 제거
    for db_uid in db_uids:
        if db_uid not in ical_uids:
            cursor.execute(
                'DELETE FROM reservations WHERE uid = ? AND room_name = ?',
                (db_uid, room_name)
            )
            print(f"🗑️ 예약 삭제됨: UID={db_uid}")

    conn.commit()
    conn.close()

def parse_ical():
    for room_name, url in ICAL_URLS.items():
        if not url:
            print(f"⚠️ {room_name} iCal URL 없음!")
            continue

        print(f"📅 {room_name} 일정 가져오는 중...")
        try:
            ical_data = fetch_ical(url)
            cal = Calendar.from_ical(ical_data)
        except Exception as e:
            print(f"❌ {room_name} 가져오기 실패: {e}")
            continue

        events = []
        for component in cal.walk():
            if component.name == "VEVENT":
                uid = str(component.get("UID"))
                guest_name = str(component.get("SUMMARY"))
                checkin = component.get("DTSTART").dt
                checkout = component.get("DTEND").dt

                # 날짜 형식 통일
                if hasattr(checkin, "strftime"):
                    checkin = checkin.strftime("%Y-%m-%d")
                if hasattr(checkout, "strftime"):
                    checkout = checkout.strftime("%Y-%m-%d")

                events.append({
                    "uid": uid,
                    "guest_name": guest_name,
                    "checkin": checkin,
                    "checkout": checkout
                })

        sync_reservations(room_name, events)

    print("🎉 끝!")

if __name__ == "__main__":
    parse_ical()