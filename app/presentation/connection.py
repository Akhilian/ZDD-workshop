from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy(engine_options={})

Model = db.Model

Base = declarative_base()
