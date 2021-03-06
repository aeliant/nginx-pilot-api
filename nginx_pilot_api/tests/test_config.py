"""Tests for configuration environment."""
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfig(TestCase):
    """List all functionnal tests for configuration environment."""

    def create_app(self):
        """Create the flask application for testing purpose."""
        app.config.from_object('nginx_pilot_api.config.DevelopmentConfig')
        return app

    def test_app_is_in_development_mode(self):
        """Checks that the development configuration is correctly loaded."""
        self.assertNotEqual(app.config.get('SECRET_KEY'), 'secret-to-change')
        self.assertIsNotNone(current_app)
        self.assertTrue(app.config.get('DEBUG'))


class TestProductionConfig(TestCase):
    """List all functional tests for production environment."""

    def create_app(self):
        """Create the testing flas application."""
        app.config.from_object('nginx_pilot_api.config.ProductionConfig')
        return app

    def test_app_is_in_production_mode(self):
        """Checks that the production configuration is correctly loaded."""
        self.assertNotEqual(app.config.get('SECRET_KEY'), 'secret-to-change')
        self.assertIsNotNone(current_app)
        self.assertFalse(app.config.get('DEBUG'))


class TestTestingConfig(TestCase):
    """List all functional tests for testing environment."""

    def create_app(self):
        """Create the testing flask application."""
        app.config.from_object('nginx_pilot_api.config.TestingConfig')
        return app

    def test_app_is_in_testing_mode(self):
        """Checks that the testing configuration is correcty loaded."""
        self.assertNotEqual('secret-to-change', app.config.get('SECRET_KEY'))
        self.assertIsNotNone(current_app)
        self.assertTrue(app.config.get('DEBUG'))


if __name__ == '__main__':
    unittest.main()
