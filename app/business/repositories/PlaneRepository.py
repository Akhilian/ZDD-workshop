from typing import List, \
    Union

from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.repositories.Repository import Repository


class PlaneRepository(Repository):
    def get_all_planes(self) -> List[Plane]:
        raise NotImplementedError

    def get_one_plane(self, identifier: PlaneIdentifier) -> Union[Plane, None]:
        raise NotImplementedError

    def add_new_plane(self, plane: Plane) -> Plane:
        raise NotImplementedError
