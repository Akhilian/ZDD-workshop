from typing import List

from .Repository import Repository
from ..entities import Plane


class PlaneRepository(Repository):
    def get_all_planes(self) -> List[Plane]:
        pass
