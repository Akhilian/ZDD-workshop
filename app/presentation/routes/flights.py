from flask import Blueprint, \
    jsonify, \
    request

from business.entities.Identifier import Identifier
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.entities.UnregisteredPlane import UnregisteredPlane
from business.interactors.declare_new_flight import declare_new_flight
from business.interactors.get_flight_details import get_flight_details
from business.interactors.list_all_flights import list_all_flights
from infrastructure.datasource.FlightDatasource import FlightDatasource
from infrastructure.datasource.PlaneDatasource import PlaneDatasource
from presentation.connection import db
from presentation.transport.FlightSerializer import FlightSerializer

flights = Blueprint('flight_api', __name__, url_prefix='/')

@flights.route("/flights/<string:flight_id>", methods=['GET'])
def get_one_flight(flight_id):
    flight_datasource = FlightDatasource(session=db.session)
    flight = get_flight_details(repository=flight_datasource, identifier=Identifier(flight_id))

    if isinstance(flight, UndeclaredFlight):
        return {}, 404

    return jsonify(FlightSerializer.to_json(flight))

@flights.route("/flights", methods=['GET'])
def get_all_flights():
    flight_datasource = FlightDatasource(session=db.session)
    flights = list_all_flights(repository=flight_datasource)

    return jsonify(FlightSerializer.to_json(flights))


@flights.route("/planes/<string:plane_id>/flights", methods=['POST'])
def post_a_new_plane(plane_id):
    plane_datasource = PlaneDatasource(session=db.session)
    flight_repository = FlightDatasource(session=db.session)
    payload = request.json

    flight = FlightSerializer.from_json(payload)

    result = declare_new_flight(flight=flight, plane_repository=plane_datasource, flight_repository=flight_repository, plane_identifier=PlaneIdentifier(plane_id))

    if isinstance(result, UnregisteredPlane):
        return {}, 400

    return {}, 200
