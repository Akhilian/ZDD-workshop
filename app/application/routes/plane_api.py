from flask import Blueprint

plane_api = Blueprint('plane_api', __name__, url_prefix='/')


@plane_api.route("/planes", methods=['GET'])
def get_all_planes():
    return "Returning planes"
