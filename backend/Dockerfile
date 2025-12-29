# 1. 빌드 단계 (Builder Stage)
# uv가 설치된 공식 이미지를 사용합니다.
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# 캐싱 효율을 위해 의존성 파일만 먼저 복사합니다.
COPY pyproject.toml uv.lock ./

# 의존성 설치 (프로젝트 자체 설치는 건너뜀)
ENV UV_COMPILE_BYTECODE=1
RUN uv sync --frozen --no-install-project --no-dev

# 2. 실행 단계 (Runtime Stage)
# 가벼운 python-slim 이미지를 사용합니다.
FROM python:3.12-slim-bookworm

WORKDIR /app

# 빌더 단계에서 설치한 가상환경(.venv)만 가져옵니다.
COPY --from=builder /app/.venv /app/.venv

# 실제 소스 코드(app 폴더)를 복사합니다.
COPY app /app/app

# 가상환경을 PATH에 등록합니다.
ENV PATH="/app/.venv/bin:$PATH"

# 포트 설정 (AWS 로드밸런서가 보통 80을 좋아하지만, 컨테이너는 8000으로 띄웁니다)
EXPOSE 8000

# 실행 명령어 (app 폴더 안의 main.py 실행)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
