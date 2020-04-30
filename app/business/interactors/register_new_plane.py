from business.entities import Plane
from business.repositories import PlaneRepository


def register_new_plane(plane_repository: PlaneRepository, plane: Plane):
    return plane_repository.add_new_plane(plane)
