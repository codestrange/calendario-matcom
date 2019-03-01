from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.votation_entity import VotationEntity


class VotationRepository(SQLAlchemyRepository):
    def entity(self):
        return VotationEntity
