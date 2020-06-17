from typing import Union

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.repositories.FlightRepository import FlightRepository


def get_flight_details(repository: FlightRepository, identifier: Identifier) -> Union[UndeclaredFlight, Flight]:
    flight = repository.get_one_flight(identifier=identifier)

    if not flight:
        return UndeclaredFlight()

    return flight
