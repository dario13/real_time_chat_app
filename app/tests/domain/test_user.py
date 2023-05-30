import unittest
from app.domain.user import User


class TestUser(unittest.TestCase):
    # Scenario: Create an User
    def test_user(self):
        # Given
        user_id = "user1"
        user_name = "User One"

        # When
        user: User = User(id=user_id, name=user_name)

        # Then
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.name, user_name)


if __name__ == "__main__":
    unittest.main()
