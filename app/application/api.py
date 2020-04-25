import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.routes.healthcheck import healthcheck
from application.routes.planes import planes

api = Flask(__name__)

api.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(api)

api.register_blueprint(planes)
api.register_blueprint(healthcheck)


