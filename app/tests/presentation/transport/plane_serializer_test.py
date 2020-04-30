from business.entities import Plane, PlaneIdentifier
from presentation.transport import PlaneSerializer


class PlaneSerializerTest:
    class ToJsonTest:
        def test_should_return_the_json_version_of_a_plane(self):
            # Given
            plane = Plane(identifier=PlaneIdentifier('BAF-256'), number_of_places=156)

            # When
            json = PlaneSerializer.to_json(plane)

            # Then
            assert json == {
                'identifier': {
                    'code': 'BAF-256'
                },
                'number_of_places': 156
            }

        def test_should_return_a_list_of_planes(self):
            # Given
            first_plane = Plane(identifier=PlaneIdentifier('BAF-256'), number_of_places=156)
            second_plane = Plane(identifier=PlaneIdentifier('AF-484'), number_of_places=46)

            # When
            json = PlaneSerializer.to_json([first_plane, second_plane])

            # Then
            assert json == [
                {
                    'identifier': {
                        'code': 'BAF-256'
                    },
                    'number_of_places': 156
                },
                {
                    'identifier': {
                        'code': 'AF-484'
                    },
                    'number_of_places': 46
                }
            ]

    class TromJsonTest:
        def test_should_return_a_plane(self):
            # Given
            data = {
                'identifier.code': 'CGS-578',
                'number_of_places': 900
            }

            # When
            plane = PlaneSerializer.from_json(data)

            # Then
            assert isinstance(plane, Plane)
            assert plane.number_of_places == 900
            assert isinstance(plane.identifier, PlaneIdentifier)
            assert plane.identifier.code == 'CGS-578'
