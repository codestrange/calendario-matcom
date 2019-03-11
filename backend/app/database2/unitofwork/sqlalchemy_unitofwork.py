from logging import exception
from . import UnitOfWork
from ...container import Container


class UnitOfWorkSQLAlchemy(UnitOfWork):

    def commit(self):
        try:
            Container.instance().current_app.db.session.commit()
        except Exception as e:
            Container.instance().current_app.db.session.rollback()
            exception(e)
