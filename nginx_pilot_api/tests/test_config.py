import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from nginx_pilot_api.config import basedir


class TestDevelopmentConfig(TestCase):
    """ List all functionnal tests for configuration environment. """

    def create_app(self):
        app.config.from_object('nginx_pilot_api.config.DevelopmentConfig')
        return app

    def test_app_is_in_development_mode(self):
        self.assertNotEqual(app.config.get('SECRET_KEY'), 'secret-to-change')


if __name__ == '__main__':
    unittest.main()
