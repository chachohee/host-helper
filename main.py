import os
from datetime import datetime
from dotenv import load_dotenv
from ical_parser import parse_ical

# 로그 디렉토리 설정
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "execution.log")
os.makedirs(LOG_DIR, exist_ok=True)

def write_log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(LOG_FILE, "a") as f:
        f.write(full_message + "\n")

def main():
    load_dotenv()  # .env 불러오기
    write_log("🚀 iCal 예약 파서 시작")

    try:
        parse_ical()
        write_log("🎉 예약 동기화 완료")
    except Exception as e:
        write_log(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    main()