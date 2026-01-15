FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

EXPOSE 8000

WORKDIR /app
COPY . ./

RUN uv sync

CMD ["uv", "run", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
