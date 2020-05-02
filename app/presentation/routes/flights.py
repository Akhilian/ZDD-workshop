from flask import Blueprint, jsonify

from business.interactors.list_all_flights import list_all_flights
from infrastructure.datasource.FlightDatasource import FlightDatasource
from presentation.connection import db
from presentation.transport.PlaneSerializer import PlaneSerializer

flights = Blueprint('flight_api', __name__, url_prefix='/')



@flights.route("/flights", methods=['GET'])
def get_all_flights():
    flight_datasource = FlightDatasource(session=db.session)
    flights = list_all_flights(repository=flight_datasource)

    return jsonify(PlaneSerializer.to_json(flights))
