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


## 6. uv 명령어 가이드

`uv`는 파이썬 프로젝트 관리를 굉장히 빠르게 만들어주는 도구입니다. 각 명령어가 쓰이는 상황을 **"요리"**에 비유하면 이해가 빠릅니다.

* **`uv add`**: 요리 재료를 구매해서 냉장고(명세서)에 채워 넣는 행위
* **`uv sync`**: 다른 사람이 쓴 장보기 리스트를 보고 내 냉장고를 그와 똑같이 맞추는 행위
* **`uv run`**: 재료를 꺼내서 실제로 요리를 하거나 도구를 쓰는 행위

프로그래머 입장에서의 구체적인 상황별 예시는 다음과 같습니다.

---

### 1. `uv add`를 쓰는 상황
**→ "새로운 라이브러리가 필요해졌을 때 (의존성 추가)"**

프로젝트를 개발하다 보니 데이터 분석을 위해 `pandas`가 필요하고, API 서버를 위해 `fastapi`가 필요해졌습니다. 이 라이브러리들을 내 프로젝트의 **"필수 재료"**로 등록하는 과정입니다.

* **상황:** `app.py`를 짜고 있는데 `import pandas`를 하니 에러가 발생함.
* **행동:**
    ```bash
    $ uv add pandas fastapi
    ```
* **결과:**
    * `pyproject.toml` 파일의 `dependencies` 리스트에 `pandas`와 `fastapi`가 추가됩니다.
    * `uv.lock` 파일이 생성(또는 갱신)되어 정확한 버전이 기록됩니다.
    * 가상환경(`.venv`)에 실제로 패키지가 설치됩니다.

---

### 2. `uv sync`를 쓰는 상황
**→ "프로젝트 환경을 동기화할 때 (환경 일치)"**

주로 **협업** 중이거나, **새로운 환경(배포 서버, 다른 PC)**에서 프로젝트를 시작할 때 씁니다. `pyproject.toml`과 `uv.lock` 파일에 적힌 대로 가상환경을 강제로 맞춥니다.

* **상황 A (협업):** 동료가 프로젝트에 `numpy`를 추가해서 깃허브(GitHub)에 올렸습니다. 나는 `git pull`을 받았지만, 내 컴퓨터엔 아직 `numpy`가 깔려있지 않습니다.
* **상황 B (배포):** AWS EC2 서버에 내 코드를 복사해 넣었습니다. 서버에는 아직 아무런 라이브러리도 없습니다.
* **행동:**
    ```bash
    $ uv sync
    ```
* **결과:**
    * `uv.lock` 파일을 읽어서, 내 가상환경(`.venv`)에 없는 패키지는 설치하고, **필요 없는(삭제된) 패키지는 가상환경에서 지워버립니다.**
    * 내 가상환경을 프로젝트 명세서와 **100% 동일한 상태**로 만듭니다.

---

### 3. `uv run`을 쓰는 상황
**→ "코드를 실행하거나 도구를 쓸 때 (실행)"**

가상환경을 굳이 활성화(`source .venv/bin/activate`)하지 않아도, `uv`가 알아서 프로젝트 환경 내에서 명령을 실행해 줍니다.

#### 상황 A: 내 프로그램 실행
* **상황:** `uv add`로 설치한 `fastapi`를 이용해 짠 서버 코드를 실행하고 싶을 때.
* **행동:**
    ```bash
    $ uv run main.py
    # 또는
    $ uv run uvicorn main:app --reload
    ```
* **이점:** `uv run`은 현재 디렉토리의 가상환경을 자동으로 감지하고 그 안에서 실행합니다. 번거롭게 `activate`를 칠 필요가 없습니다.

#### 상황 B: 일회성 도구 실행 (강력 추천) ⭐
* **상황:** 프로젝트 의존성에는 넣고 싶지 않지만, 코드 포맷팅을 위해 `black`이나 `ruff`를 **잠깐만** 쓰고 싶을 때.
* **행동:**
    ```bash
    # ruff가 설치되어 있지 않아도, 임시로 다운받아 실행하고 사라짐
    $ uv run --with ruff ruff check .
    ```
* **이점:** `pyproject.toml`을 더럽히지 않고 도구를 사용할 수 있습니다. (Node.js의 `npx`와 비슷합니다.)

---

### FAQ

> **💡 팁:** 폴더 생성과 동시에 파이썬 버전 명시는 어떻게해?

**폴더 이름(프로젝트명)**과 --python 옵션을 한 줄에 같이 적어주시면 됩니다.
명령어 구조는 다음과 같습니다.
```bash
uv init [폴더명] --python [버전]
```

구체적인 실행 예시
만약 my-server라는 폴더를 만들면서, 파이썬 버전을 3.11로 고정하고 싶다면 아래와 같이 입력합니다.
```bash
uv init my-server --python 3.11
```

이 명령어가 수행하는 일 (순서대로)
 * 현재 위치에 my-server라는 새 폴더를 만듭니다.
 * 해당 폴더 안에 프로젝트 설정 파일(pyproject.toml)을 생성합니다.
 * 핵심: 해당 폴더 안에 .python-version이라는 파일을 만들고, 그 안에 3.11이라고 적어둡니다.
확인해보기
제대로 되었는지 확인하려면 생성된 폴더로 들어가서 버전을 찍어보면 됩니다.

```bash
cd my-server
uv run python --version
# 출력 결과: Python 3.11.x (uv가 자동으로 3.11 버전을 관리해 줍니다)
```

참고: uv는 컴퓨터에 해당 버전의 파이썬이 없으면, uv run이나 uv sync를 처음 실행할 때 알아서 다운로드(Managed Python) 받아 사용합니다. 따로 파이썬을 설치할 필요가 없습니다.
