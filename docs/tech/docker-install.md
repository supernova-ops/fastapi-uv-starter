
# Docker 설치 가이드 (Ubuntu 24.04)

Ubuntu 24.04 (Noble Numbat) 환경에서 Docker Engine과 Docker Compose 최신 버전을 설치하는 방법입니다. Ubuntu 기본 저장소가 아닌 Docker 공식 저장소를 사용하여 안정적이고 최신 기능을 사용할 수 있습니다.

## 1. 필수 패키지 및 GPG 키 설정

Docker 공식 저장소를 시스템에 등록하기 위해 보안 키(GPG Key)를 설정합니다.

```bash
# 1. 패키지 목록 업데이트 및 필수 도구 설치
sudo apt-get update
sudo apt-get install -y ca-certificates curl

# 2. GPG 키 저장을 위한 디렉토리 생성
sudo install -m 0755 -d /etc/apt/keyrings

# 3. Docker 공식 GPG 키 다운로드
sudo curl -fsSL [https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg) -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 4. 저장소(Repository) 등록
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] [https://download.docker.com/linux/ubuntu](https://download.docker.com/linux/ubuntu) \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. 저장소 변경사항 반영
sudo apt-get update
```

## 2. Docker Engine 설치
Docker Engine, CLI, Containerd 및 플러그인(Compose 포함)을 설치합니다.
```bash
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 3. 권한 설정 (sudo 없이 사용하기)
기본적으로 Docker 명령어는 root 권한이 필요하여 매번 sudo를 입력해야 합니다. 현재 사용자를 docker 그룹에 추가하여 이를 해결합니다.
```bash
# 현재 사용자($USER)를 docker 그룹에 추가
sudo usermod -aG docker $USER
```
!!! warning "로그아웃 필요"
그룹 권한 변경 사항을 적용하려면 로그아웃 후 다시 로그인하거나, 아래 명령어로 현재 세션을 갱신해야 합니다.
```bash
bash newgrp docker 
```

## 4. 설치 확인
설치가 정상적으로 완료되었는지 확인합니다.
```bash
# 버전 확인
docker --version

# 테스트 이미지 실행 (Permission denied 오류가 없어야 함)
docker run hello-world
```

성공 시 아래와 같은 메시지가 출력됩니다.
> Hello from Docker!
> This message shows that your installation appears to be working correctly.
> 
💡 참고: Docker Compose 사용법
이제 별도의 설치 없이 docker compose (하이픈 없음) 명령어를 바로 사용할 수 있습니다.
docker compose version


---
