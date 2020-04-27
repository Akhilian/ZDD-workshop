import os
from flask import Flask

from application.connection import db
from application.routes.healthcheck import healthcheck
from application.routes.planes import planes

api = Flask(__name__)

api.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(api)

api.register_blueprint(planes)
api.register_blueprint(healthcheck)
