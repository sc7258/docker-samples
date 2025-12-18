# FastAPI with Redis Example

이 프로젝트는 Docker Compose를 사용하여 FastAPI 애플리케이션과 Redis 데이터베이스를 함께 실행하는 간단한 예제입니다.

애플리케이션은 API가 호출될 때마다 방문 횟수를 Redis에 기록하고, 현재 방문 횟수와 Redis 연결 상태를 JSON 형식으로 반환합니다.

## 요구 사항

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 실행 방법

1.  이 저장소를 클론하거나 코드를 다운로드합니다.
2.  프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 Docker 컨테이너를 빌드하고 실행합니다.

    ```bash
    docker-compose up --build
    ```
    
    - `--build` 옵션은 이미지가 없거나 소스 코드가 변경되었을 때 이미지를 새로 빌드하도록 합니다.

## 사용 방법

애플리케이션이 실행되면, 터미널에서 다음 `curl` 명령어를 사용하여 API를 호출할 수 있습니다.

```bash
curl http://localhost:8000/api
```

### 예상 출력

API를 호출할 때마다 `visit_count`가 1씩 증가하는 것을 확인할 수 있습니다.

```json
{
  "message": "Hello Docker!",
  "timestamp": "2023-10-27T10:00:00.000000",
  "hostname": "abcdef123456",
  "visit_count": 1,
  "redis_connected": true
}
```
(`timestamp`와 `hostname` 값은 실제 실행 시 다르게 나타납니다.)

## 프로젝트 구조

```
.
├── app.py           # FastAPI 애플리케이션 로직
├── requirements.txt # Python 의존성 목록
├── compose.yml      # Docker Compose 설정 파일
├── Dockerfile       # FastAPI 앱을 위한 Dockerfile
└── README.md        # 프로젝트 설명 파일
```
