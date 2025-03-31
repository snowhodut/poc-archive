# challenge/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# 필요 패키지 설치
RUN pip install flask

# 앱 복사
COPY app.py /app/app.py
COPY flag.txt /flag.txt

# 실행
CMD ["python", "app.py"]
