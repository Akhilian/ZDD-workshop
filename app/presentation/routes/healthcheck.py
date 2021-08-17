from flask import Blueprint, abort, redirect, url_for

healthcheck = Blueprint('healthcheck', __name__, url_prefix='/')


@healthcheck.route("/status")
def status_page():
    return {}, 200


@healthcheck.route("/")
def home():
    return redirect(url_for('healthcheck.status_page'))
