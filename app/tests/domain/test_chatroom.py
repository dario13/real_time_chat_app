import unittest
from app.domain.chatroom import Chatroom
from app.domain.user import User
from app.domain.message import Message


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
