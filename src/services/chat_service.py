from src.domain.entities.chatroom import Chatroom
from src.domain.entities.message import Message
from src.domain.ports.chatroom_port import ChatRoomPort


class ChatService:
    def __init__(self, chatroom_repo: ChatRoomPort):
        self._chatroom_repo = chatroom_repo

    def fetch_chat_history(self, chatroom: Chatroom):
        return self._chatroom_repo.fetch_chat_history(chatroom)

    def send_message(self, chatroom: Chatroom, message: Message):
        chatroom.add_message(message)
        self._chatroom_repo.send_message(chatroom, message)
