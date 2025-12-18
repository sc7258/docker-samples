# Ubuntu with Git

이 Docker 이미지는 `ubuntu:latest`를 기반으로 하며 `git`이 설치되어 있습니다.

## 빌드

Docker 이미지를 빌드하려면 다음 명령을 실행하십시오.

```bash
docker build -t my-ubuntu:git .
```

## 빌드 확인

`docker build` 명령이 성공적으로 완료되었는지 확인하려면 `docker images` 명령을 사용하여 로컬 이미지 목록을 확인합니다.

```bash
docker images | findstr "my-ubuntu"
```

다음과 유사한 출력이 표시되면 이미지가 성공적으로 생성된 것입니다.

```
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
my-ubuntu     git       xxxxxxxxxxxx   xx seconds ago   xxxMB
```

## 실행

빌드된 Docker 이미지를 실행하려면 다음 명령을 사용하십시오.

```bash
docker run -it --rm my-ubuntu:git /bin/bash
```

## 확인

이미지 내에서 `git`이 올바르게 설치되었는지 확인하려면 다음 명령을 실행할 수 있습니다.

```bash
git --version
```
