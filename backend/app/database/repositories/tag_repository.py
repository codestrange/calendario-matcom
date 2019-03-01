from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.tag_entity import TagEntity


class TagRepository(SQLAlchemyRepository):
    def entity(self):
        return TagEntity
