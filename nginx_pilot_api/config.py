# coding=utf-8
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Base Configuration for all 3 environments. """

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'secret-to-change')
    DEBUG = False


class DevelopmentConfig(Config):
    """ Development configuration. """

    DEBUG = True


class TestingConfig(Config):
    """ Testing configuration. """

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """ Production configurationt. """

    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    tests=TestingConfig,
    prod=ProductionConfig
)


key = Config.SECRET_KEY
