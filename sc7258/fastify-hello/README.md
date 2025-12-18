# Fastify Hello World

간단한 Fastify "Hello World" 예제 애플리케이션입니다.

## 사전 준비물

*   [Node.js](https://nodejs.org/) (v20 이상 권장)
*   [Docker](https://www.docker.com/)

## 로컬에서 실행하기

### 1. 의존성 설치

프로젝트 루트 디렉터리에서 다음 명령어를 실행하여 필요한 패키지를 설치합니다.

```bash
npm install
```

### 2. 애플리케이션 실행

다음 명령어로 Fastify 서버를 시작합니다.

```bash
node app.js
```

서버가 시작되면 `http://localhost:3000` 주소로 접속할 수 있습니다.

## Docker로 실행하기

### 1. Docker 이미지 빌드

프로젝트 루트 디렉터리에서 다음 명령어를 실행하여 Docker 이미지를 빌드합니다.

```bash
docker build -t fastify-hello .
```

### 2. Docker 컨테이너 실행

빌드된 이미지를 사용하여 Docker 컨테이너를 실행합니다.

```bash
docker run -p 3000:3000 fastify-hello
```

`-p 3000:3000` 옵션은 호스트의 3000번 포트를 컨테이너의 3000번 포트로 매핑합니다. 이제 브라우저나 API 클라이언트에서 `http://localhost:3000`으로 애플리케이션에 접근할 수 있습니다.

## API 엔드포인트

*   **`GET /`**
    *   `{ "hello": "world" }` 메시지를 반환합니다.

## 컨테이너 내부 셸(Terminal) 접근하기

이미지 내부의 파일 구조를 확인하거나 디버깅을 위해 실행 중인 컨테이너의 셸 환경으로 직접 접근할 수 있습니다.

1.  **컨테이너 백그라운드 실행**

    먼저, `-d` 옵션을 사용하여 컨테이너를 백그라운드에서 실행하고 `--name`으로 식별하기 쉬운 이름을 지정합니다.

    ```bash
    docker run -d --rm -p 3000:3000 --name my-fastify-app fastify-hello
    ```

2.  **컨테이너 셸 접속**

    `docker exec` 명령어를 사용하여 실행 중인 컨테이너(`my-fastify-app`)의 셸(`sh`)을 실행합니다. `-it` 옵션은 상호작용이 가능한 터미널을 열어줍니다.

    ```bash
    docker exec -it my-fastify-app sh
    ```

    이제 프롬프트가 컨테이너 내부(`/usr/src/app`)로 변경되며, `ls -la`, `cat app.js` 등 리눅스 명령어로 내부 파일을 확인할 수 있습니다.

3.  **정리**

    확인이 끝나면 컨테이너를 중지하고 삭제합니다.

    ```bash
    docker stop my-fastify-app
    docker rm my-fastify-app
    ```
