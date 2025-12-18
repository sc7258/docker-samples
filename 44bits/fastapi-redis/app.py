import os
from datetime import datetime
from fastapi import FastAPI
import redis

# FastAPI 앱 생성
app = FastAPI()

# Redis 연결 시도
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_connected = False
r = None
try:
    # decode_responses=True: Redis 응답을 자동으로 문자열로 변환
    r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)
    r.ping()
    redis_connected = True
except redis.exceptions.ConnectionError:
    # Redis 연결에 실패해도 앱은 계속 동작하도록 설정
    pass

@app.get("/api")
def api():
    visit_count = 0
    if redis_connected and r:
        # 'visit_count' 키의 값을 1 증가시킴
        visit_count = r.incr('visit_count')
    
    # 컨테이너의 호스트 이름을 가져옴 (Docker에서 자동 설정)
    hostname = os.environ.get('HOSTNAME', 'unknown')
    
    return {
        "message": "Hello Docker!",
        "timestamp": datetime.now().isoformat(),
        "hostname": hostname,
        "visit_count": visit_count,
        "redis_connected": redis_connected
    }
