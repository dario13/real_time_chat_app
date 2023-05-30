from .user import User


class Message:
    def __init__(self, user: User, content: str) -> None:
        self.user = user
        self.content = content
