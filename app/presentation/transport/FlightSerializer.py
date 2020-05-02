from typing import Union

from business.entities.Flight import Flight
from presentation.transport.ToDictSerializer import _to_dict


class FlightSerializer():
    @staticmethod
    def to_json(plane: Union[Flight]) -> dict:
        return _to_dict(plane)
