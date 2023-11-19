# Blog 프로젝트

## I. 실행 순서
### 1. docker compose 실행
- 실행: `docker compose up -d`
- 종료: `docker compose down`

### 2. Swagger 확인
- URL: 127.0.0.1:8000/swagger/
- 참고: Static 파일이 확인이되지 않는 경우 - `python manage.py collectstatic`

### 3. API 호출
- 게시글 생성: POST http://127.0.0.1:8000/board/
- 게시글 리스트: GET http://127.0.0.1:8000/board/
- 게시글 상세: GET http://127.0.0.1:8000/board/{id}/
- 게시글 수정: PUT http://127.0.0.1:8000/board/{id}/
- 게시글 삭제: DELETE http://127.0.0.1:8000/board/{id}/


## II. 주요 명령어
### 로그 확인
`docker compose logs -f`

### 테스트 코드 확인
`python manage.py test board`

### 가상환경 진입
`source venv/bin/activate`

### pip 라이브러리 설치 (venv)
`pip install django`

### 마이그레이션
`python manage.py makemigrations`
`python manage.py migrate`

### 슈퍼 유저 생성
`python manage.py createsuperuser`

### 서버 실행
`python manage.py runserver`

### 설치된 라이브러리 requirements.txt 생성 
`pip freeze > requirements.txt` 

### requirements.txt 버전 설치
`pip install -r requirements.txt`

