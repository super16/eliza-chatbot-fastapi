# eliza-chatbot-fastapi

[Eliza chatbot](https://en.wikipedia.org/wiki/ELIZA) backend implemented
with FastAPI websockets.

Check out [SPA](https://super16.github.io/eliza-chatbot/) which using this application
and its [source](https://github.com/super16/eliza-chatbot).

## Prepare environment

Requires [poetry](https://python-poetry.org/).

```bash
poetry install
```

## Lint

```bash
poetry run flake8
poetry run mypy eliza_chatbot_fastapi
```

## Test

```bash
poetry run python eliza_chatbot_fastapi/eliza.py
```

## Development Run

```bash
ALLOWED_HOST="localhost" ALLOWED_ORIGIN="http://127.0.0.1:5173" poetry run uvicorn eliza_chatbot_fastapi.main:app --reload
```
