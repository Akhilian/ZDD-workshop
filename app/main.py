from flask import Flask

api = Flask(__name__)


@api.route("/")
def hello():
    return "Hello World (again) from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"

@api.route("/status")
def status_page():
    return "UP - Running"


if __name__ == "__main__":
    # Only for debugging while developing
    api.run(host="0.0.0.0", debug=True, port=80, use_reloader=True)
