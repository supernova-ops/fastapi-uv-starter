# Getting started

## Installation

이 프로젝트는 Python 패키지 매니저인 **uv**를 사용하여 의존성을 관리합니다.
아래 절차에 따라 환경을 설정하고 서버를 실행해 주세요.

## 1. 사전 요구 사항 (Prerequisites)

이 프로젝트를 실행하기 위해서는 **Git**과 **uv**가 필요합니다.

### uv 설치하기
아직 `uv`가 설치되지 않았다면, 터미널에서 아래 명령어로 설치하세요.

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

!!! tip "Windows 사용자"
    Powershell: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

---

## 2. 프로젝트 다운로드

Github 저장소를 로컬 환경으로 복제(Clone)합니다.

```bash
git clone https://github.com/username/fastapi-uv-starter.git
cd fastapi-uv-starter
```

---

## 3. 의존성 설치 (Setup)

`uv`를 사용하면 가상환경 생성과 패키지 설치를 한 번에 처리할 수 있습니다.
`uv sync` 명령어는 `uv.lock` 파일에 기록된 정확한 버전의 패키지들을 설치합니다.

```bash
# 가상환경 생성 및 라이브러리 동기화
uv sync
```

!!! success "설치 완료"
    명령어가 완료되면 `.venv` 폴더가 생성되고 필요한 라이브러리가 모두 설치된 상태입니다.

---

## 4. 서버 실행

설치가 완료되었다면 개발 서버를 실행할 수 있습니다.

```bash
# uvicorn 서버 실행 (Hot Reload 모드)
uv run uvicorn main:app --reload
```

* **uv run**: 프로젝트 가상환경 내에서 명령어를 실행합니다.
* **--reload**: 코드를 수정하면 서버가 자동으로 재시작됩니다.

---

## 5. 접속 확인

브라우저를 열고 다음 주소로 접속하여 서버가 정상적으로 작동하는지 확인하세요.

* **메인 페이지:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **API 문서 (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **대체 문서 (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

