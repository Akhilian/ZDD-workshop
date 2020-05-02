from unittest.mock import Mock

from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.interactors.list_all_available_planes import list_all_available_planes
from business.repositories.PlaneRepository import PlaneRepository


class ListAllAvailablePlanesTest():

    def test_should_load_planes_using_the_repository(self):
        # Given
        plane_repository = PlaneRepository()
        planes = [Plane(identifier=PlaneIdentifier('BA-154'), number_of_places=50)]
        plane_repository.get_all_planes = Mock(return_value=planes)

        # When
        returned_planes = list_all_available_planes(plane_repository=plane_repository)

        # Then
        assert returned_planes == planes
