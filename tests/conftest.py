import os

import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database

from alembic import command
from alembic.config import Config
from config import TEST_POSTGRES_URL
from db.models import Base

target_metadata = Base.metadata

os.environ['TESTING'] = 'True'


@pytest.fixture(scope="module")
def temp_db():
    if not database_exists(TEST_POSTGRES_URL):
        create_database(TEST_POSTGRES_URL)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    alembic_cfg.set_main_option(
        "script_location", os.path.join(base_dir, "alembic")
    )
    command.upgrade(alembic_cfg, 'head')
    try:
        yield TEST_POSTGRES_URL
    finally:
        drop_database(TEST_POSTGRES_URL)
