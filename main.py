import time
import logging
from datetime import datetime
from ical_parser import parse_ical

# 로그 설정
logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def main():
    logging.info("🚀 Host Helper 서버 시작")

    while True:
        logging.info("🔄 예약 동기화 시작")

        try:
            parse_ical()
            logging.info("✅ 예약 동기화 완료")
        except Exception as e:
            logging.error(f"❌ 에러 발생: {e}")

        time.sleep(60)  # 60초마다 반복

if __name__ == "__main__":
    main()