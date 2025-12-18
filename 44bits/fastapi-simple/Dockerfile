# Python 3.12 slim 이미지 사용
FROM python:3.12-slim

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY app.py .

# 포트 노출
EXPOSE 8000

# 앱 실행 (uvicorn 사용)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]