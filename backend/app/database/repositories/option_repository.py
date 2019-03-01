from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.option_entity import OptionEntity


class OptionRepository(SQLAlchemyRepository):
    def entity(self):
        return OptionEntity
