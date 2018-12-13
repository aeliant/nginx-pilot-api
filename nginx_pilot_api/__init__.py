"""Nginx Pilot API Entry point file."""

from flask import Flask

from .config import config_by_name


def create_app(config_name):
    """Create the flask application."""
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name))

    return app
