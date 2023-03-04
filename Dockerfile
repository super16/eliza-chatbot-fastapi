
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV ALLOWED_HOST "eliza-chatbot-fastapi.fly.dev"
ENV ALLOWED_ORIGIN "https://super16.github.io"

RUN ["pip", "install", "poetry"]

COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml
COPY ./README.md /app/README.md
COPY ./eliza_chatbot_fastapi /app/eliza_chatbot_fastapi

RUN ["poetry", "install", "--without", "development"]

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "eliza_chatbot_fastapi.main:app", "--host", "0.0.0.0"]
