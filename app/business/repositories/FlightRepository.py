from typing import List, \
    Union

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Position import Position
from business.repositories.Repository import Repository


class FlightRepository(Repository):
    def get_all_flights(self) -> List[Flight]:
        raise NotImplementedError

    def get_one_flight(self, identifier: Identifier) -> Union[Flight, None]:
        raise NotImplementedError

    def save_new_position(self, flight: Flight, position: Position) -> None:
        raise NotImplementedError
