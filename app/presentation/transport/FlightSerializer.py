from typing import Union, \
    List

from business.entities.Flight import Flight
from presentation.transport.ToDictSerializer import _to_dict


class FlightSerializer():
    @staticmethod
    def to_json(plane: Union[Flight, List[Flight]]) -> dict:
        return _to_dict(plane)
