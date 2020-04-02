from flask import Flask
app = Flask(__name__)

with app.app_context():
  import api.routes