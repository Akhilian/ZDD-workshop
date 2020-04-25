from flask import Blueprint

planes = Blueprint('plane_api', __name__, url_prefix='/')


@planes.route("/planes", methods=['GET'])
def get_all_planes():
    return "Returning planes []"
