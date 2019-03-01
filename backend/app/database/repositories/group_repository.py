from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.group_entity import GroupEntity


class GroupRepository(SQLAlchemyRepository):
    def entity(self):
        return GroupEntity
