from typing import Optional

from sqlalchemy.orm import Session

from . import models


class UserStatsRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_user_stat(
        self, user_stat: models.UserStats
    ) -> models.UserStats:
        self.db.add(user_stat)
        self.db.commit()
        return user_stat
