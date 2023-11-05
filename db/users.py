from typing import Optional

from sqlalchemy.orm import Session

from . import models


class UsersRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> Optional[models.User]:
        return (
            self.db.query(models.User)
            .filter(models.User.id == user_id)
            .first()
        )

    def get_user_by_username(self, name: str) -> Optional[models.User]:
        return (
            self.db.query(models.User)
            .filter(models.User.username == name)
            .first()
        )

    def create_user(self, user: models.User) -> models.User:
        self.db.add(user)
        self.db.commit()
        return user

    def delete_user(self, user_id: int) -> Optional[int]:
        user = (
            self.db.query(models.User)
            .filter(models.User.id == user_id)
            .first()
        )
        if user is not None:
            self.db.delete(user)
            self.db.commit()
            return 1

    def update_user(
        self, user_id: int, new_user: models.User
    ) -> Optional[int]:
        user = (
            self.db.query(models.User)
            .filter(models.User.id == user_id)
            .first()
        )
        if user is not None:
            user.username = new_user.username
            user.role = new_user.role
            user.gender = new_user.gender
            user.password = new_user.password
            user.email = new_user.email
            self.db.add(user)
            self.db.commit()
            return 1
