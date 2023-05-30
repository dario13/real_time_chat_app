import unittest
from app.domain.message import Message
from app.domain.user import User


class TestMessage(unittest.TestCase):
    def test_message(self) -> None:
        # Given
        userdict = {"id": "user1", "name": "User 1"}
        message_content = "Message Test"

        # When
        user = User(id=userdict["id"], name=userdict["name"])
        message = Message(user=user, content=message_content)

        # Then
        self.assertEqual(message.content, message_content)
        self.assertEqual(user.id, userdict["id"])
        self.assertEqual(user.name, userdict["name"])


if __name__ == "__main":
    unittest.main()
