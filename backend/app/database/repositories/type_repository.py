from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.type_entity import TypeEntity


class TypeRepository(SQLAlchemyRepository):
    def entity(self):
        return TypeEntity
