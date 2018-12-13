"""Main project file, managing tests and server running."""
import os
import unittest

from flask_script import Manager
from nginx_pilot_api import create_app
from nginx_pilot_api.controller import blueprint

app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    """Run the server."""
    app.run()


@manager.command
def test():
    """Runs the tests."""
    tests = unittest.TestLoader().discover(
        'nginx_pilot_api/tests',
        pattern='test*.py'
    )
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
