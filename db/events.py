from typing import Optional, Type

from sqlalchemy.orm import Session

from db import models
from protos.observer_pb2 import Event


class EventsRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_event(self, event_id: int) -> Optional[models.Event]:
        return (
            self.db.query(models.Event)
            .filter(models.Event.id == event_id)
            .first()
        )

    def get_event_list(self) -> list[Type[Event]]:
        events = self.db.query(models.Event).all()
        return events

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

    def update_event(
        self, event_id: int, new_event: models.Event
    ) -> Optional[int]:
        event = (
            self.db.query(models.Event)
            .filter(models.Event.id == event_id)
            .first()
        )
        if event is not None:
            event.name = new_event.name
            event.type = new_event.type
            event.age_restrictions = new_event.age_restrictions
            event.day = new_event.day
            self.db.add(event)
            self.db.commit()
            return 1
