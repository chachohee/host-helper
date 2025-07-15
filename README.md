# host-helper

호스트 운영을 자동화해주는 개인 프로젝트입니다.

## 주요 기능
- iCal 연동으로 예약 일정 가져오기
- 예약 정보 DB 저장
- 체크인/체크아웃 청소 알림 자동화
- 정산 및 손익 계산

## 구조
- `main.py`: 메인 스케줄러
- `parser.py`: iCal 예약 파서
- `notifier.py`: 알림 기능
- `db/`: SQLite DB 파일

## 개발 환경
- Python 3.13.1
- 가상환경: venv
