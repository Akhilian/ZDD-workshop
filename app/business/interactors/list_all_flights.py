from typing import List

from business.entities.Flight import Flight
from business.repositories.FlightRepository import FlightRepository


def list_all_flights(repository: FlightRepository) -> List[Flight]:
    return repository.get_all_flights()
