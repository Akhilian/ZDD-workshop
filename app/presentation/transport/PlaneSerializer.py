from typing import Union, List

from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from presentation.transport.ToDictSerializer import _to_dict


class PlaneSerializer():
    @staticmethod
    def to_json(plane: Union[Plane, List[Plane]]):
        return _to_dict(plane)

    @staticmethod
    def from_json(data: dict) -> Plane:
        return Plane(PlaneIdentifier(data.get('identifier.code')), data.get('number_of_places'))
