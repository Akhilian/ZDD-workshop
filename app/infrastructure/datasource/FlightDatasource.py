from typing import List

from business.entities.Flight import Flight
from infrastructure.models.FlightModel import FlightModel


class FlightDatasource():
    def __init__(self, session):
        self.session = session

    def get_all_flights(self) -> List[Flight]:
        flights = self.session.query(FlightModel).all()

        return [
            Flight(status=flight.status)
            for flight in flights
        ]
