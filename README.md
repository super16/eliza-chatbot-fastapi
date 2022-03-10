# eliza-chatbot-fastapi

[Eliza chatbot](https://en.wikipedia.org/wiki/ELIZA) backend implemented
with FastAPI websockets.

Check out [SPA](https://super16.github.io/eliza-chatbot/) which using this application
and its [source](https://github.com/super16/eliza-chatbot).

## Preparation

```bash
pip3 install requirements.txt
```

## Testing

```bash
python3 eliza.py
```

## Development Run

```bash
ALLOWED_HOST="localhost" ALLOWED_ORIGIN="http://localhost:3000" uvicorn main:app --reload
```
