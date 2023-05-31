from quart import Quart
from src.adapters.primary.ws_adapter import WebSocketAdapter
from src.adapters.secondary.db_adapter import DBAdapter
from src.services.chat_service import ChatService

db: DBAdapter = DBAdapter("postgresql://localhost:5432/chat")
ws: WebSocketAdapter = WebSocketAdapter(ChatService(db))
app = Quart(__name__)


@app.route("/")
async def hello():
    return "Hello, World!"


@app.websocket("/ws")
async def rcv_msg():
    await ws.receive_message()


if __name__ == "__main__":
    app.run()
