from abc import ABC, abstractmethod
from src.domain.entities import Chatroom, Message
from typing import List


class ChatRoomPort(ABC):
    @abstractmethod
    def fetch_chat_history(self, chatroom: Chatroom) -> List[Message]:
        pass

    @abstractmethod
    def send_message(self, chatroom: Chatroom, message: Message) -> None:
        pass
