from typing import Union, \
    List

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from presentation.transport.ToDictSerializer import _to_dict


class FlightSerializer():
    @staticmethod
    def to_json(flight: Union[Flight, List[Flight]]) -> dict:
        return _to_dict(flight)

    @staticmethod
    def from_json(flight_payload) -> Flight:
        return Flight(
            status=flight_payload['status'],
            duration=flight_payload['duration'],
            start_time=flight_payload['start_time'],
            identifier=Identifier(flight_payload['identifier']),
            position=None,
        )
