from typing import List

from .Repository import Repository
from ..entities import Plane


class PlaneRepository(Repository):
    def get_all_planes(self) -> List[Plane]:
        raise NotImplementedError

    def get_one_plane(self) -> Plane:
        raise NotImplementedError

    def add_new_plane(self, plane: Plane) -> Plane:
        raise NotImplementedError
