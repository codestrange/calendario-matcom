from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.user_entity import UserEntity


class UserRepository(SQLAlchemyRepository):

    def entity(self):
        return UserEntity
