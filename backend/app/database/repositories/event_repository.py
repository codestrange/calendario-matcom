from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.event_entity import EventEntity


class EventRepository(SQLAlchemyRepository):
    def entity(self):
        return EventEntity
