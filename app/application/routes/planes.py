from flask import Blueprint, jsonify

from application.connection import db
from infrastructure.datasource import PlaneDatasource
from infrastructure.transport import PlaneSerializer

planes = Blueprint('plane_api', __name__, url_prefix='/')


@planes.route("/planes", methods=['GET'])
def get_all_planes():
    plane_datasource = PlaneDatasource(session=db.session)
    planes = plane_datasource.get_all_planes()

    return jsonify(PlaneSerializer.to_json(planes))
