from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.notification_entity import NotificationEntity


class NotificationRepository(SQLAlchemyRepository):
    def entity(self):
        return NotificationEntity
