from dependency_injector import containers, providers
from src.adapters.primary.ws_adapter import WebSocketAdapter
from src.adapters.secondary.db_adapter import DBAdapter
from src.services.chat_service import ChatService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_adapter = providers.Singleton(DBAdapter, db_url=config.db.url)

    chat_service = providers.Factory(ChatService, chatroom_repo=db_adapter)

    web_socket_adapter = providers.Factory(WebSocketAdapter, chat_service=chat_service)
