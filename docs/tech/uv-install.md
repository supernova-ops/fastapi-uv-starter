# Astral uv 프로젝트 생성 및 사용 가이드

**Astral의 `uv`**는 Python 패키지 관리 및 프로젝트 관리를 위한 고속 통합 도구입니다. `pip`, `poetry` 등을 대체하여 사용할 수 있습니다.

## 1. 설치 (Installation)
아직 설치되지 않았다면 아래 명령어로 설치합니다. (macOS/Linux 기준)

```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

## 2. 프로젝트 초기화 (Initialization)
### 방법 A:새로운 폴더를 만드며 시작
```bash
uv init my-project
cd my-project
```
### 방법 B: 현재 폴더에서 시작
```bash
mkdir my-project
cd my-project
uv init
```

## 3. 디렉토리 구조
```bash
my-project/
├── .python-version    # 파이썬 버전 명시
├── pyproject.toml     # 프로젝트 설정 및 의존성 관리
├── README.md          # 설명 파일
├── hello.py           # 메인 스크립트 예시
└── .venv/             # (자동 생성) 가상 환경
```

## 4. 주요 명령어
### 💡 주요 명령어 요약

| 명령어 | 설명 | 비고 |
| :--- | :--- | :--- |
| uv init | 프로젝트 초기화 | pyproject.toml 생성 |
| uv add <pkg> | 패키지 추가 및 설치 | pip install 대체 |
| uv remove <pkg> | 패키지 삭제 | pip uninstall 대체 |
| uv run <file> | 가상환경 내에서 파일 실행 | python <file> 대체 |
| uv sync | uv.lock 기반으로 환경 동기화 | 협업 시 팀원 환경 통일에 사용 |


## 5. 팁: 특정 파이썬 버전 사용
특정 파이썬 버전으로 프로젝트를 세팅하려면 --python옵션을 사용합니다.
```bash
uv init --python 3.11
```