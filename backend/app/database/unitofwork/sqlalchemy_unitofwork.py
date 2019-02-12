from . import UnitOfWork
from ...container import Container


class UnitOfWorkSQLAlchemy(UnitOfWork):

    def commit(self):
        Container.instance().current_app.db.session.commit()
