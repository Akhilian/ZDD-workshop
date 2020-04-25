from typing import List

from business.entities import Plane
from business.repositories import PlaneRepository


def list_all_available_planes(plane_repository: PlaneRepository) -> List[Plane]:
    return plane_repository.get_all_planes()
