from typing import Union

from business.entities.Identifier import Identifier
from business.entities.Position import Position
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.repositories.FlightRepository import FlightRepository


def add_new_position_for_a_flight(
    flight_repository: FlightRepository,
    position: Position,
    identifier: Identifier
) -> Union[UndeclaredFlight, None]:
    flight = flight_repository.get_one_flight(identifier)

    if flight:
        return flight_repository.save_new_position(flight, position)

    return UndeclaredFlight()
