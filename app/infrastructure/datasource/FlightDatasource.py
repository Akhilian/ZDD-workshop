from typing import List, \
    Union

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.repositories.FlightRepository import FlightRepository
from infrastructure.models.FlightModel import FlightModel


class FlightDatasource(FlightRepository):
    def __init__(self, session):
        self.session = session

    def get_all_flights(self) -> List[Flight]:
        flights = self.session.query(FlightModel).all()

        return [
            Flight(
                status=flight.status,
                duration=flight.duration,
                start_time=flight.start_time,
                identifier=flight.identifier
            )
            for flight in flights
        ]

    def get_one_flight(self, identifier: Identifier) -> Union[Flight, None]:
        flight = self.session \
            .query(FlightModel) \
            .filter(FlightModel.identifier == identifier.value) \
            .first()

        if not flight:
            return None

        return Flight(
            status=flight.status,
            duration=flight.duration,
            start_time=flight.start_time,
            identifier=flight.identifier
        )
