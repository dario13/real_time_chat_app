from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.secondary.db_models import (
    ChatroomDBModel,
    MessageDBModel,
    UserDBModel,
    Base,
)
from sqlalchemy.orm.exc import NoResultFound
from src.domain.ports.chatroom_port import ChatRoomPort
from src.domain.entities.chatroom import Chatroom
from src.domain.entities.message import Message
from src.domain.entities.user import User


class DBAdapter(ChatRoomPort):
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def fetch_chat_history(self, chatroom: Chatroom):
        with self.Session() as session:
            db_chatroom = (
                session.query(ChatroomDBModel)
                .filter(ChatroomDBModel.id == chatroom.id)
                .first()
            )
            if db_chatroom:
                chatroom.messages = [
                    Message(msg.user, msg.content) for msg in db_chatroom.messages
                ]
                return chatroom.messages
            else:
                return None

    def send_message(self, chatroom: Chatroom, message: Message):
        with self.Session() as session:
            db_chatroom = self.get_chatroom(session, chatroom.id)
            if not db_chatroom:
                db_chatroom = ChatroomDBModel(id=chatroom.id, name=chatroom.name)
                session.add(db_chatroom)

            db_user = self.get_or_create_user(session, message.user)

            db_message = MessageDBModel(
                user=db_user, content=message.content, chatroom=db_chatroom
            )
            session.add(db_message)
            session.commit()

    def get_or_create_user(self, session, user: User):
        try:
            db_user = session.query(UserDBModel).filter(UserDBModel.id == user.id).one()
        except NoResultFound:
            db_user = UserDBModel(id=user.id, name=user.name)
            session.add(db_user)
            # session.flush()  # Generate primary key
        return db_user

    def get_chatroom(self, session, chatroom_id):
        return (
            session.query(ChatroomDBModel)
            .filter(ChatroomDBModel.id == chatroom_id)
            .first()
        )
