from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(engine_options={})

Model = db.Model
