# eliza-chatbot-fastapi

[Eliza chatbot](https://en.wikipedia.org/wiki/ELIZA) backend implemented
with FastAPI websockets.

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
ALLOWED_HOST="localhost" uvicorn main:app --reload
```
