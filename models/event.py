from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from config import POSTGRES_URL

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Event(BaseModel):
    __tablename__ = "Event"

    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    age_restrictions = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)


class User(BaseModel):
    __tablename__ = "User"

    username = Column(String(255), unique=True, nullable=False)
    gender = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class Comment(BaseModel):
    __tablename__ = 'Comment'

    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('Event.id'), nullable=False)


def connect_db():
    engine = create_engine(str(POSTGRES_URL))
    session = Session(bind=engine.connect())
    return session
# print(session.query(User).all())
