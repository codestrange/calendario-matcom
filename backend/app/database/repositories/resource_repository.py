from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.resource_entity import ResourceEntity


class ResourceRepository(SQLAlchemyRepository):
    def entity(self):
        return ResourceEntity
