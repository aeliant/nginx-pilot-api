# coding=utf-8
from flask import Flask

from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name))

    return app
