from typing import List
from .message import Message


class Chatroom:
    def __init__(self, id: str, name: str) -> None:
        self.id: str = id
        self.name: str = name
        self.messages: List[Message] = []

    def add_message(self, message: Message) -> None:
        self.messages.append(message)
