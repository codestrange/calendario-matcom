class Container:

    __instance = None

    def __init__(self):
        self.__current_app = None

    def init_app(self, app):
        self.__current_app = app

    @property
    def current_app(self):
        return self.__current_app

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = Container()
        return cls.__instance
