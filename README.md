# eliza-chatbot-fastapi

[Eliza chatbot](https://en.wikipedia.org/wiki/ELIZA) backend implemented
with FastAPI websockets.

Check out [SPA](https://super16.github.io/eliza-chatbot/) which using this application
and its [source](https://github.com/super16/eliza-chatbot).

## Prepare environment

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Testing

```bash
python3 eliza.py
```

## Development Run

```bash
ALLOWED_HOST="localhost" ALLOWED_ORIGIN="http://127.0.0.1:5173" uvicorn main:app --reload
```
