from datetime import datetime

from freezegun import freeze_time

from infrastructure.models.FlightModel import FlightModel
from presentation.connection import db


class GetAllFlightsTest:

    @freeze_time("2019-02-05")
    def test_when_there_is_a_flight(self, end_to_end):
        # Given
        flight_model = FlightModel()
        flight_model.start_time = datetime.now()
        flight_model.duration = 257
        flight_model.status = 'ongoing'
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
                'status': 'ongoing'
            }
        ]

    def test_when_no_flight(self, end_to_end):
        # Given
        # When
        response = end_to_end.get('/flights')

        # Then
        assert response.status_code == 200
        assert len(response.json) == 0
