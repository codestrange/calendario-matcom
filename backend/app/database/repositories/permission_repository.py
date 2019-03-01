from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.permission_entity import PermissionEntity


class PermissionRepository(SQLAlchemyRepository):
    def entity(self):
        return PermissionEntity
