# coding=utf-8
from flask_testing import TestCase
from manage import app


class BaseTestCase(TestCase):
    """ Base tests. """

    def create_app(self):
        app.config.from_object('nginx_pilot_api.config.TestingConfig')
        return app
