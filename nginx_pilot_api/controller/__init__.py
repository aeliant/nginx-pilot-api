"""Controller package entry point, defining the global blueprint."""
from flask_restplus import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Nginx Pilot API',
          version='0.1.0',
          description='An api for managing Nginx configuration'
          )
