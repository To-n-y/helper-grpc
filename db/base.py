from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import POSTGRES_URL

engine = create_engine(str(POSTGRES_URL))

TESTING = environ.get("TESTING")
if TESTING:
    from config import TEST_POSTGRES_URL

    engine = create_engine(str(TEST_POSTGRES_URL))


def connect_db():
    session = Session(bind=engine.connect())
    with Session(bind=engine.connect()) as session:
        return session
