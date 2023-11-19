FROM python:3.11.0

# /app/ 경로를 작업 디렉토리로 설정
WORKDIR /app

# .pyc 파일을 생성하지 않도록 설정
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

#EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]
