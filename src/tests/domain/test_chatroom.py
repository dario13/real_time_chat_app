import unittest
from src.domain.entities.chatroom import Chatroom
from src.domain.entities.user import User
from src.domain.entities.message import Message


class TestChatroom(unittest.TestCase):
    def test_add_message(self):
        # Given
        chatroom = Chatroom("chatroom1")
        user = User("user1", "User 1")
        message = Message(user, "Hello, world!")

        # When
        chatroom.add_message(message)

        # Then
        self.assertEqual(chatroom.messages[0], message)
