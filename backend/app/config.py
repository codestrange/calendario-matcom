from os import getenv
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))


class Config(object):
    SECRET_KEY = getenv('SECRET_KEY') or 'secret_key'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = getenv('DEV_DATABASE_URL') or \
        'sqlite:///' + join(basedir, 'data_dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = getenv('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    DATABASE_URL = getenv('DATABASE_URL') or \
        'sqlite:///' + join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
