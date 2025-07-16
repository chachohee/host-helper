# 🏡 Host Helper

에어비앤비, 숙소 호스트들을 위한 예약 일정 파서 & 자동화 프로그램!

구글 캘린더의 iCal URL을 읽어서 예약 정보를 SQLite로 저장하고,
체크인·체크아웃 관리, 청소 스케줄 관리 등 자동화를 위한 첫걸음을 제공합니다.

## 📌 주요 기능
- iCal 연동으로 예약 일정 가져오기
- 예약 정보 DB 저장
- 체크인/체크아웃 청소 알림 자동화
- 정산 및 손익 계산

## 📍 구조
- `main.py`: 메인 스케줄러
- `parser.py`: iCal 예약 파서
- `notifier.py`: 알림 기능
- `db/`: SQLite DB 파일

## ⚙️ 개발 환경
- Python 3.13.1
- 가상환경: venv

## 📂 프로젝트 구조

```plaintext
host-helper/
├── db/
│   ├── init_db.py      # SQLite DB 테이블 초기화 스크립트
│   └── reservations.sqlite3 (자동 생성)
├── ical_parser.py      # iCal 파싱 로직
├── main.py             # 실행 스크립트
├── .env                # 환경 변수 파일 (로컬용)
├── .env.example        # 환경 변수 예시 파일 (공유용)
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ 설치 방법

1️⃣ 저장소 클론
```bash
git clone https://github.com/chachohee/host-helper.git
cd host-helper
```

2️⃣ 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는 venv\Scripts\activate  # Windows
```

3️⃣ 필수 패키지 설치

```bash
pip install -r requirements.txt
```

## 🔑 환경 변수 설정

1. .env.example 파일을 참고해서 .env 파일 생성:

```env
ICAL_URL_ROOM_A="https://YOUR_ROOM_A_ICAL_URL"
ICAL_URL_ROOM_B="https://YOUR_ROOM_B_ICAL_URL"
ICAL_URL_ROOM_C="https://YOUR_ROOM_C_ICAL_URL"
```

2. .env 파일은 절대 깃에 커밋하지 마세요! → .gitignore에 이미 포함되어 있습니다.

## 🗄️ DB 초기화

최초 실행 시 SQLite 테이블을 만들어야 합니다.

```bash
python3 db/init_db.py
```

db/reservations.sqlite3 파일이 자동으로 생성됩니다.

## 🚀 실행 방법

구글 캘린더의 iCal URL에서 예약 데이터를 가져와 DB에 저장합니다.

```bash
python3 main.py
```

정상 실행 시 아래처럼 출력됩니다.

```
🚀 iCal 예약 파서 시작
📅 Room A 일정 가져오는 중...
✅ 예약 저장: 한그루 | 2025-08-20 ~ 2025-08-24
📅 Room B 일정 가져오는 중...
✅ 예약 저장: 윤정성 | 2025-10-22 ~ 2025-10-26
...
🎉 끝!
```

## ✅ 자주 하는 실수 체크리스트

- .env 파일에 iCal URL이 정확한지 다시 확인하세요.
- DB 파일(reservations.sqlite3)이 없으면 init_db.py로 다시 생성하세요.
- 구글 캘린더에 샘플 일정을 만들어 iCal로 가져와서 테스트해보세요.

## ✨ 앞으로 추가할 기능

- 체크아웃 시 청소 업체에 자동 알림 전송
- 순이익 계산 기능 (청소비 등 운영 비용 반영)
- 자주 묻는 질문(FAQ) 자동응답 챗봇 연동
- 예약 일정 자동 동기화 스케줄러

## 🪪 라이선스

MIT License

## 🙌 만든 사람

lilw3i 🐹💕