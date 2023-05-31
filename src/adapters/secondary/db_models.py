from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class ChatroomDBModel(Base):
    __tablename__ = "chatrooms"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    messages = relationship("MessageDBModel", back_populates="chatroom")


class MessageDBModel(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.now())
    chatroom_id = Column(Integer, ForeignKey("chatrooms.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    chatroom = relationship("ChatroomDBModel", back_populates="messages")
    user = relationship("UserDBModel", back_populates="messages")


class UserDBModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default=lambda: f"user_{uuid.uuid4().hex}")

    messages = relationship("MessageDBModel", back_populates="user")
