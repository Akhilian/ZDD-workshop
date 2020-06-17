from typing import List, \
    Union

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Plane import Plane
from business.entities.Position import Position
from business.repositories.FlightRepository import FlightRepository
from infrastructure.datasource.PlaneDatasource import PlaneDatasource
from infrastructure.models.FlightModel import FlightModel
from infrastructure.models.IdentifierModel import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel


class FlightDatasource(FlightRepository):
    def __init__(self, session):
        self.session = session

    def get_all_flights(self) -> List[Flight]:
        flights = self.session.query(FlightModel).all()

        list_of_flights = []
        for flight in flights:
            if flight.position:
                latitude, longitude = flight.position.split(',')
                position = Position(
                    latitude=float(latitude),
                    longitude=float(longitude)
                )
            else:
                position = None

            flight = Flight(
                status=flight.status,
                duration=flight.duration,
                start_time=flight.start_time,
                identifier=Identifier(flight.identifier),
                position=position
            )
            list_of_flights.append(flight)

        return list_of_flights

    def get_one_flight(self, identifier: Identifier) -> Union[Flight, None]:
        flight = self.session \
            .query(FlightModel) \
            .filter(FlightModel.identifier == identifier.value) \
            .first()

        if not flight:
            return None

        if flight.position:
            latitude, longitude = flight.position.split(',')
            position = Position(
                latitude=float(latitude),
                longitude=float(longitude)
            )
        else:
            position = None

        return Flight(
            status=flight.status,
            duration=flight.duration,
            start_time=flight.start_time,
            identifier=Identifier(flight.identifier),
            position=position
        )

    def save_new_position(self, flight: Flight, position: Position) -> None:
        flight_model = self.session.query(FlightModel)\
            .filter(FlightModel.identifier == flight.identifier.value).first()

        flight_model.position = f"{position.latitude},{position.longitude}"

        self.session.add(flight_model)

    def save_new_flight(self, flight: Flight, plane: Plane) -> None:
        plane_model = self.session.query(PlaneModel).join(PlaneModel.identifier).filter(
            IdentifierModel.code == plane.identifier.code).first()

        flight_model = FlightModel()
        flight_model.identifier = flight.identifier.value
        flight_model.status = flight.status
        flight_model.start_time = flight.start_time
        flight_model.duration = flight.duration

        flight_model.plane = plane_model

        self.session.add(flight_model)
