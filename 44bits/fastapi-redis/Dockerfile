# Python 3.9 slim 버전을 베이스 이미지로 사용합니다.
FROM python:3.9-slim

# 작업 디렉토리를 /app으로 설정합니다.
WORKDIR /app

# 의존성 파일을 먼저 복사하고 설치합니다.
# (소스 코드가 변경되어도 의존성이 동일하면 이 레이어는 캐시됩니다.)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 소스 코드를 작업 디렉토리로 복사합니다.
COPY . .

# 컨테이너가 시작될 때 uvicorn 서버를 실행합니다.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
