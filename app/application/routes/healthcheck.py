from flask import Blueprint

healthcheck = Blueprint('healthcheck', __name__, url_prefix='/')


@healthcheck.route("/")
def hello():
    return "Hello World (again) from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"


@healthcheck.route("/status")
def status_page():
    return "UP"
