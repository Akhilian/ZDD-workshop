import os
from flask import Flask

from presentation.connection import db
from presentation.routes.healthcheck import healthcheck
from presentation.routes.planes import planes

api = Flask(__name__)

api.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(api)

api.register_blueprint(planes)
api.register_blueprint(healthcheck)
