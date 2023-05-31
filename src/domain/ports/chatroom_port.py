from abc import ABC, abstractmethod
from src.domain.entities.user import User
from src.domain.entities.chatroom import Chatroom
from src.domain.entities.message import Message
from typing import List


class ChatRoomPort(ABC):
    @abstractmethod
    def fetch_chat_history(self, chatroom: Chatroom) -> List[Message]:
        pass

    @abstractmethod
    def send_message(self, chatroom: Chatroom, message: Message) -> None:
        pass
