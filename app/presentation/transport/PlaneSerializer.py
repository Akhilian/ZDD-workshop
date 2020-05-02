from typing import Union, List

from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier


def _to_dict(object):
    if isinstance(object, list):
        return [_to_dict(obj) for obj in object]
    else:
        attributes = object.__dict__

        for key in attributes:
            if hasattr(attributes[key], '__dict__'):
                attributes[key] = _to_dict(attributes[key])

        return attributes


class PlaneSerializer():
    @staticmethod
    def to_json(plane: Union[Plane, List[Plane]]):
        return _to_dict(plane)

    @staticmethod
    def from_json(data: dict) -> Plane:
        return Plane(PlaneIdentifier(data.get('identifier.code')), data.get('number_of_places'))
