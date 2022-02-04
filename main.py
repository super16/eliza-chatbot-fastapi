from os import environ
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from eliza import Eliza

# App section

DESCRIPTION = """
    Eliza chatbot backend implemented with FastAPI websockets.
"""

app: FastAPI = FastAPI(
    title="Eliza Chatbot Backend",
    description=DESCRIPTION,
    version="0.1.0",
    contact={
        "name": "super16",
        "url": "https://github.com/super16",
    },
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[environ['ALLOWED_HOST']]
)


class ConnectionManager:
    """
    Connection manager for websockets.

    Get from FastAPI documentation.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        """
        Create websocket connection and add to
        active connection list.

        Args:
          websocket: A Websocket instance to add.
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        """
        Remove websocket connection from active
        connections list.

        Args:
          websocket: A Websocket instance to remove.
        """
        self.active_connections.remove(websocket)

    async def reply(self, message: str, websocket: WebSocket) -> None:
        """
        Send text message to websocket connection.

        Args:
          message: Text message to send.
          websocket: A Websocket instance addressee.
        """
        if message:
            await websocket.send_text(message)

    async def quit(self, message: str, websocket: WebSocket) -> None:
        """
        Send farewell message and disconnect.

        Args:
          message: Farewell text message to send.
          websocket: A Websocket instance addressee and to disconnect.
        """
        await self.reply(message, websocket)
        await websocket.close()
        self.disconnect(websocket)


manager: ConnectionManager = ConnectionManager()
eliza: Eliza = Eliza()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        await manager.reply(eliza.greeting(), websocket)
        while True:
            data: str = await websocket.receive_text()
            if data == "quit":
                await manager.quit(eliza.response(data), websocket)
                break
            else:
                await manager.reply(eliza.response(data), websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
