from flask import Blueprint, jsonify, request

from business.interactors.list_all_available_planes import list_all_available_planes
from business.interactors.register_new_plane import register_new_plane
from infrastructure.datasource.PlaneDatasource import PlaneDatasource
from presentation.connection import db
from presentation.transport.PlaneSerializer import PlaneSerializer

planes = Blueprint('plane_api', __name__, url_prefix='/')


@planes.route("/planes", methods=['GET'])
def get_all_planes():
    plane_datasource = PlaneDatasource(session=db.session)
    planes = list_all_available_planes(plane_repository=plane_datasource)

    return jsonify(PlaneSerializer.to_json(planes))


@planes.route("/planes", methods=['POST'])
def add_a_plane():
    plane_datasource = PlaneDatasource(session=db.session)

    plane = PlaneSerializer.from_json(request.json)

    register_new_plane(plane=plane, plane_repository=plane_datasource)

    return jsonify([PlaneSerializer.to_json(plane)])
