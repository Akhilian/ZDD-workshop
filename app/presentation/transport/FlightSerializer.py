from typing import Union, \
    List

from business.entities.Flight import Flight
from presentation.transport.ToDictSerializer import _to_dict


class FlightSerializer():
    @staticmethod
    def to_json(flight: Union[Flight, List[Flight]]) -> dict:
        return _to_dict(flight)
