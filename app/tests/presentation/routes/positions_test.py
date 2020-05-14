from datetime import datetime

from infrastructure.models.FlightModel import FlightModel
from infrastructure.models.IdentifierModel import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel
from presentation.connection import db


class AddPositionToFlightTest:
    def test_when_the_flight_does_not_exist(self, end_to_end):
        # Given
        new_position_in_new_york = {
            'latitude': 40.714,
            'longitude': -74.006
        }

        # When
        response = end_to_end.post('/flights/1234/positions', json=new_position_in_new_york)

        # Then
        assert response.status_code == 404


    def test_when_the_plane_exists(self, end_to_end):
        # Given
        new_position_in_new_york = {
            'latitude': 40.714,
            'longitude': -74.006
        }

        identifier = IdentifierModel()
        identifier.code = 'BAF-256'
        db.session.add(identifier)

        plane_model = PlaneModel()
        plane_model.places = 145
        plane_model.identifier = identifier
        db.session.add(plane_model)

        flight_model = FlightModel()
        flight_model.identifier = '4256'
        flight_model.start_time = datetime.now()
        flight_model.duration = 257
        flight_model.status = 'ongoing'
        flight_model.plane = plane_model
        db.session.add(flight_model)

        # When
        response = end_to_end.post('/flights/4256/positions', json=new_position_in_new_york)

        # Then
        assert response.status_code == 200
