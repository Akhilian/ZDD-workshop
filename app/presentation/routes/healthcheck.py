from flask import Blueprint

healthcheck = Blueprint('healthcheck', __name__, url_prefix='/')


@healthcheck.route("/status")
def status_page():
    return {}, 200
