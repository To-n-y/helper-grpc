import datetime

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import Session, declarative_base

from config import POSTGRES_URL

Base = declarative_base()


class BaseModel(Base):  # type: ignore
    __abstract__ = True

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class User(BaseModel):
    __tablename__ = "User"

    username = Column(String(255), unique=True, nullable=False)
    role = Column(String(255), default="user")
    gender = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class Event(BaseModel):
    __tablename__ = "Event"

    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    age_restrictions = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)


class Plan(BaseModel):
    __tablename__ = "Plan"

    user_id = Column(Integer, ForeignKey("User.id"))
    event_id = Column(Integer, ForeignKey("Event.id"))
    event_type = Column(String(255), nullable=False)
    name = Column(String, nullable=False)


class Comment(BaseModel):
    __tablename__ = "Comment"

    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("Event.id"), nullable=False)


class AuthToken(BaseModel):
    __tablename__ = "Auth_token"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    token = Column(String, nullable=False)
