# ADChemto Backend API

ADChemto 웹사이트 및 인트라넷 시스템의 백엔드 API 서버입니다.

## 기술 스택

- **Python 3.11+**
- **FastAPI** - 현대적이고 빠른 웹 프레임워크
- **PostgreSQL** - 관계형 데이터베이스
- **SQLAlchemy** - ORM
- **Alembic** - 데이터베이스 마이그레이션
- **Uvicorn** - ASGI 서버

## 프로젝트 구조

```
backend/
├── app/
│   ├── api/                 # API 라우터
│   │   └── v1/
│   │       ├── endpoints/   # API 엔드포인트
│   │       └── api.py       # API 라우터 통합
│   ├── core/                # 핵심 설정
│   │   ├── config.py        # 설정
│   │   ├── database.py      # 데이터베이스 연결
│   │   ├── security.py     # 보안 유틸리티
│   │   └── exceptions.py    # 예외 처리
│   ├── models/              # 데이터베이스 모델
│   ├── schemas/             # Pydantic 스키마
│   └── main.py              # FastAPI 앱
├── alembic/                 # 데이터베이스 마이그레이션
├── requirements.txt         # 의존성
├── run.py                   # 개발 서버 실행
└── README.md
```

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (Linux/Mac)
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

```bash
# env.example을 .env로 복사
copy env.example .env

# .env 파일을 편집하여 실제 값으로 설정
```

### 4. 데이터베이스 설정

```bash
# PostgreSQL 데이터베이스 생성
createdb adchemto_db

# 마이그레이션 실행
alembic upgrade head
```

### 5. 개발 서버 실행

```bash
python run.py
```

또는

```bash
uvicorn app.main:app --reload
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 주요 기능

### 인증 시스템
- JWT 기반 인증
- 사용자 로그인/로그아웃
- 비밀번호 해싱

### 홈페이지 API
- 뉴스/공지사항 관리
- 고객 문의 처리
- 제품/서비스 정보

### 인트라넷 API
- 사내 공지사항
- 문서 관리 시스템
- 일정 관리
- 직원 디렉토리

## 개발 가이드

### 새로운 API 엔드포인트 추가

1. `app/api/v1/endpoints/`에 새로운 라우터 파일 생성
2. `app/schemas/`에 Pydantic 스키마 정의
3. `app/models/`에 SQLAlchemy 모델 정의
4. `app/api/v1/api.py`에 라우터 등록

### 데이터베이스 마이그레이션

```bash
# 새 마이그레이션 생성
alembic revision --autogenerate -m "설명"

# 마이그레이션 실행
alembic upgrade head

# 마이그레이션 되돌리기
alembic downgrade -1
```

## 배포

### Docker 사용 (권장)

```bash
# Docker 이미지 빌드
docker build -t adchemto-backend .

# 컨테이너 실행
docker run -p 8000:8000 adchemto-backend
```

### 직접 배포

```bash
# 프로덕션 서버 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 보안 고려사항

- 환경 변수로 민감한 정보 관리
- JWT 토큰 만료 시간 설정
- CORS 설정
- 입력 데이터 검증
- SQL 인젝션 방지 (SQLAlchemy ORM 사용)

## 문제 해결

### 일반적인 문제

1. **데이터베이스 연결 오류**
   - PostgreSQL 서버가 실행 중인지 확인
   - DATABASE_URL 설정 확인

2. **의존성 설치 오류**
   - Python 버전 확인 (3.11+ 권장)
   - 가상환경 활성화 확인

3. **마이그레이션 오류**
   - 데이터베이스 스키마 확인
   - 마이그레이션 파일 검토

## 기여하기

1. 이슈 생성 또는 기존 이슈 확인
2. 기능 브랜치 생성
3. 코드 작성 및 테스트
4. Pull Request 생성

## 라이선스

이 프로젝트는 ADChemto의 소유입니다.
