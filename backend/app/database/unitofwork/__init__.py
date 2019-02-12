from ..repositories import Repository


class UnitOfWork:
    def __init__(self, repositories=None):
        self.repositories = dict() if repositories is None else repositories

    def init_app(self, app):
        app.unitofwork = self

    def add_repository(self, repository, name=None):
        if not issubclass(repository, Repository):
            raise TypeError()
        if name is None:
            name = repository.__name__
        self.repositories[name] = repository

    def get_repository(self, name):
        return self.repositories.get(name)()

    def commit(self):
        raise NotImplementedError
