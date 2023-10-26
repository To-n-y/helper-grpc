from typing import Optional

from sqlalchemy.orm import Session

from db import models


class EventsRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_event(self, event_id: int) -> Optional[models.Event]:
        return (
            self.db.query(models.Event)
            .filter(models.Event.id == event_id)
            .first()
        )

    def create_event(self, event: models.Event) -> models.Event:
        self.db.add(event)
        self.db.commit()
        return event

    def delete_event(self, event_id: int) -> Optional[int]:
        event = (
            self.db.query(models.Event)
            .filter(models.Event.id == event_id)
            .first()
        )
        if event is not None:
            self.db.delete(event)
            self.db.commit()
            return 1

    def update_event(self, event: models.Event) -> Optional[int]:
        event = (
            self.db.query(models.Event)
            .filter(models.Event.id == event.id)
            .first()
        )
        if event is not None:
            event.name = event.name
            event.type = event.type
            event.age_restrictions = event.age_restrictions
            event.day = event.day
            self.db.add(event)
            self.db.commit()
            return 1


print(models.Event.name)
