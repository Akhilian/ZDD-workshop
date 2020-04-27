from business.entities import Plane, PlaneIdentifier
from infrastructure.transport import PlaneSerializer


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
