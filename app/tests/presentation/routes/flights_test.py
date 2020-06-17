from datetime import datetime

from freezegun import freeze_time

from infrastructure.models.FlightModel import FlightModel
from infrastructure.models.IdentifierModel import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel
from presentation.connection import db


class GetAllFlightsTest:

    @freeze_time("2019-02-05")
    def test_when_there_is_a_flight(self, end_to_end):
        # Given
        flight_model = FlightModel()
        flight_model.start_time = datetime.now()
        flight_model.duration = 257
        flight_model.status = 'ongoing'
        flight_model.identifier = 'G2VH'
        flight_model.position = '-45.145,37.46724'
        db.session.add(flight_model)

        # When
        response = end_to_end.get('/flights')

        # Then
        assert response.status_code == 200
        assert len(response.json) == 1
        assert response.json == [
            {
                'start_time': '2019-02-05T00:00:00',
                'duration': 257,
                'status': 'ongoing',
                'identifier': 'G2VH',
                'position': {
                    'latitude': -45.145,
                    'longitude': 37.46724,
                }
            }
        ]

    def test_when_no_flight(self, end_to_end):
        # Given
        # When
        response = end_to_end.get('/flights')

        # Then
        assert response.status_code == 200
        assert len(response.json) == 0

class GetOneFlightTest:
    @freeze_time("2019-02-05")
    def test_when_there_is_a_flight(self, end_to_end):
        # Given
        flight_model = FlightModel()
        flight_model.start_time = datetime.now()
        flight_model.duration = 257
        flight_model.status = 'ongoing'
        flight_model.identifier = 'G2VH'
        flight_model.position = '-45.145,37.46724'
        db.session.add(flight_model)

        # When
        response = end_to_end.get('/flights/G2VH')

        # Then
        assert response.status_code == 200
        assert response.json == {
            'start_time': '2019-02-05T00:00:00',
            'duration': 257,
            'status': 'ongoing',
            'identifier': 'G2VH',
            'position': {
                'latitude': -45.145,
                'longitude': 37.46724,
            }
        }

    def test_when_no_flight(self, end_to_end):
        # Given
        # When
        response = end_to_end.get('/flights/ID')

        # Then
        assert response.status_code == 404

class DeclareNewFlightTest:
    @freeze_time("2020-01-25")
    def test_return_400_when_plane_is_not_found(self, end_to_end):
        # Given
        flight = {
            "status": 'ongoing',
            "duration": 2456,
            "start_time": datetime.now(),
            "identifier": 'FAA-331'
        }

        # When
        response = end_to_end.post('/planes/GYSU/flights', json=flight)

        # Then
        assert response.status_code == 400

    @freeze_time("2020-01-25")
    def test_return_200_when_flight_is_created(self, end_to_end):
        # Given
        identifier = IdentifierModel()
        identifier.code = 'GYSU'

        plane_model = PlaneModel()
        plane_model.places = 145
        plane_model.identifier = identifier
        db.session.add(plane_model)

        flight = {
            "status": 'ongoing',
            "duration": 2456,
            "start_time": datetime.now(),
            "identifier": 'FAA-331'
        }

        # When
        response = end_to_end.post('/planes/GYSU/flights', json=flight)

        # Then
        assert response.status_code == 200
