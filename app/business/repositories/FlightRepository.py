from typing import List

from business.entities.Flight import Flight
from business.repositories.Repository import Repository


class FlightRepository(Repository):
    def get_all_flights(self) -> List[Flight]:
        raise NotImplementedError
