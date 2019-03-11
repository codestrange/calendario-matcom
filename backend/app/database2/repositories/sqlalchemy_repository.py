from . import Repository, query_decorator
from ...container import Container


class SQLAlchemyRepository(Repository):

    def add(self, entity):
        Container.instance().current_app.db.session.add(entity)

    def delete(self, entity):
        Container.instance().current_app.db.session.delete(entity)

    @query_decorator
    def query(self):
        return Container.instance().current_app.db.session.query(self.entity()).all()

    def entity(self):
        raise NotImplementedError
