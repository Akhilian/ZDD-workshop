from unittest.mock import Mock

from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.interactors.register_new_plane import register_new_plane
from business.repositories.PlaneRepository import PlaneRepository


class RegisterNewPlaneTest():

    def test_should_register_a_new_plane(self):
        # Given
        plane_repository = PlaneRepository()
        plane = Plane(identifier=PlaneIdentifier('BA-154'), number_of_places=50)
        plane_repository.add_new_plane = Mock(return_value=plane)

        # When
        saved_plane = register_new_plane(plane_repository=plane_repository, plane=plane)

        # Then
        plane_repository.add_new_plane.assert_called_once_with(plane)
        assert saved_plane == plane
