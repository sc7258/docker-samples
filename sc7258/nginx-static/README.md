# Nginx 정적 사이트 Docker 예제

이 프로젝트는 Docker 컨테이너에서 Nginx를 사용하여 간단한 정적 HTML 파일을 서비스하는 방법을 보여주는 간단한 예제입니다.

## 사전 요구 사항

- [Docker](https://www.docker.com/get-started)가 설치되어 있어야 합니다.

## 사용법

1.  **Docker 이미지 빌드:**

    다음 명령어를 사용하여 Docker 이미지를 빌드합니다.

    ```bash
    docker build -t my-nginx:static .
    ```

2.  **Docker 컨테이너 실행:**

    빌드된 이미지를 사용하여 컨테이너를 실행합니다.
    - `-d`: 컨테이너를 백그라운드에서 실행합니다.
    - `--rm`: 컨테이너가 중지될 때 자동으로 삭제되도록 설정합니다.
    - `-p 8080:80`: 컨테이너의 80번 포트를 로컬 머신의 8080번 포트에 매핑합니다.
    - `--name my-nginx-container`: 컨테이너에 `my-nginx-container`라는 이름을 지정하여 쉽게 참조할 수 있도록 합니다.

    ```bash
    docker run -d --rm --name my-nginx-container -p 8080:80 my-nginx:static
    ```

3.  **결과 확인:**

    웹 브라우저를 열고 `http://localhost:8080` 주소로 이동하면 `index.html` 파일의 내용을 확인할 수 있습니다.

4.  **컨테이너 터미널에 연결 (선택 사항):**

    실행 중인 컨테이너의 셸에 접근하고 싶다면 다음 명령어를 사용합니다. `my-nginx-container`는 위에서 `--name`으로 지정한 컨테이너 이름입니다.

    ```bash
    docker exec -it my-nginx-container /bin/sh
    ```
    
    셸에 접속한 후에는 `exit` 명령어로 빠져나올 수 있습니다.

## 파일 설명

-   `index.html`: 웹 브라우저에 표시될 정적 HTML 파일입니다.
-   `Dockerfile`: Nginx 서버를 포함하는 Docker 이미지를 빌드하기 위한 지침을 담고 있습니다.
-   `README.md`: 이 프로젝트에 대한 설명과 사용법을 안내하는 파일입니다.
