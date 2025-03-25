# 베이스 이미지
FROM python:3.9-slim

# 컨테이너 내부 작업 디렉토리
WORKDIR /app

# 파일 복사
COPY requirements.txt .
COPY app.py .

# 필요한 패키지 설치
RUN pip install -r requirements.txt

# 앱 실행
CMD ["python", "app.py"]