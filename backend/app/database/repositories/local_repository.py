from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.local_entity import LocalEntity


class LocalRepository(SQLAlchemyRepository):
    def entity(self):
        return LocalEntity
