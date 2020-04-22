from flask import Flask
app = Flask(__name__)

with app.app_context():
  import routes

if __name__ == '__main__':
  app.run(debug=True, port=8080)