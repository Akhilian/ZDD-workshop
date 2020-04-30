from presentation.connection import db
from infrastructure.models import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel


class GetAllPlanesTest:
    def test_when_there_is_a_plane(self, end_to_end):
        # Given
        identifier = IdentifierModel()
        identifier.code = 'BAF-256'
        db.session.add(identifier)

        plane_model = PlaneModel()
        plane_model.places = 145
        plane_model.identifier = identifier
        db.session.add(plane_model)

        # When
        response = end_to_end.get('/planes')

        # Then
        assert response.status_code == 200
        assert len(response.json) == 1
        assert response.json == [
            {
                'identifier': {
                    'code': 'BAF-256'
                },
                'number_of_places': 145
            }
        ]

    def test_when_no_planes(self, end_to_end):
        # Given
        # When
        response = end_to_end.get('/planes')

        # Then
        assert response.status_code == 200
        assert len(response.json) == 0

class RegisterAPlaneTest:
    def test_when_sending_an_new_plane_to_track(self, end_to_end):
        # When
        response = end_to_end.post('/planes', json={
            'identifier.code': 'BAF-151',
            'number_of_places': 900
        })

        # Then
        assert response.status_code == 200
        assert len(response.json) == 1
        assert response.json == [
            {
                'identifier': {
                    'code': 'BAF-151'
                },
                'number_of_places': 900
            }
        ]
