"""Main project file, managing tests and server running."""
import os

from nginx_pilot_api import create_app
from nginx_pilot_api.controller import blueprint

app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()


@app.cli.command()
def run():
    """Run the server."""
    app.run()


if __name__ == "__main__":
    run()
