from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.role_entity import RoleEntity


class RoleRepository(SQLAlchemyRepository):
    def entity(self):
        return RoleEntity
