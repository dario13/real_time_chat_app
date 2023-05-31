from quart import Quart
from src.dependency_injection.container import Container
from src.adapters.primary.ws_adapter import WebSocketAdapter
import sys

# Create and configure the container
container = Container()
container.config.db.url.from_env(
    "DATABASE_URL", default="postgresql://localhost:5432/chat"
)
container.wire(modules=[sys.modules[__name__]])

app = Quart(__name__)


@app.websocket("/ws")
async def rcv_msg():
    ws: WebSocketAdapter = container.web_socket_adapter()
    await ws.receive_message()


if __name__ == "__main__":
    app.run()
