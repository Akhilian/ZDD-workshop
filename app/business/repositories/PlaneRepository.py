from typing import List

from business.entities.Plane import Plane
from business.repositories.Repository import Repository


class PlaneRepository(Repository):
    def get_all_planes(self) -> List[Plane]:
        raise NotImplementedError

    def get_one_plane(self) -> Plane:
        raise NotImplementedError

    def add_new_plane(self, plane: Plane) -> Plane:
        raise NotImplementedError
