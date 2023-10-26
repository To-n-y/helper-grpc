from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import POSTGRES_URL


def connect_db():
    engine = create_engine(str(POSTGRES_URL))
    session = Session(bind=engine.connect())
    return session
