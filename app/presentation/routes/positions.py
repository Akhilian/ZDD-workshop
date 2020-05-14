from flask import Blueprint, jsonify, request

from business.entities.Identifier import Identifier
from business.entities.Position import Position
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.interactors.add_new_position_for_a_flight import add_new_position_for_a_flight
from business.interactors.list_all_available_planes import list_all_available_planes
from business.interactors.register_new_plane import register_new_plane
from infrastructure.datasource.FlightDatasource import FlightDatasource
from infrastructure.datasource.PlaneDatasource import PlaneDatasource
from presentation.connection import db
from presentation.transport.PlaneSerializer import PlaneSerializer

position = Blueprint('position_api', __name__, url_prefix='/flights/<string:flight_id>')


@position.route("/positions", methods=['POST'])
def add_a_plane(flight_id):
    flight_repository = FlightDatasource(session=db.session)
    payload = request.json

    result = add_new_position_for_a_flight(
        flight_repository=flight_repository,
        position=Position(
            latitude=payload['latitude'],
            longitude=payload['longitude']
        ),
        identifier=Identifier(flight_id)
    )

    if isinstance(result, UndeclaredFlight):
        return {}, 404

    return {}, 200
