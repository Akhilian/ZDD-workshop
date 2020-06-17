from datetime import datetime
from unittest.mock import Mock

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.entities.UnregisteredPlane import UnregisteredPlane
from business.interactors.declare_new_flight import declare_new_flight
from business.repositories.FlightRepository import FlightRepository
from business.repositories.PlaneRepository import PlaneRepository


class DeclareNewFlightTest():
    def test_return_an_unregistered_plane_message_when_plane_is_not_found(self):
        # Given
        plane_identifier = PlaneIdentifier('YGUB')
        plane_repository = PlaneRepository()
        plane_repository.get_one_plane = Mock(return_value=None)
        flight_repository = FlightRepository()
        flight_repository.save_new_flight = Mock()
        flight = Flight(
            status='ongoing',
            duration=267,
            start_time=datetime(2020, 4, 5, 15, 25, 16),
            identifier=Identifier('0937'),
            position=None
        )


        # When
        result = declare_new_flight(
            plane_identifier=plane_identifier,
            flight=flight,
            plane_repository=plane_repository,
            flight_repository=flight_repository
        )

        # Then
        assert isinstance(result, UnregisteredPlane)
        plane_repository.get_one_plane.assert_called_with(plane_identifier)

    def test_save_a_new_flight_when_plane_exists(self):
        # Given
        plane_identifier = PlaneIdentifier('YGUB')
        plane = Plane(identifier=plane_identifier, number_of_places=50)
        plane_repository = PlaneRepository()
        plane_repository.get_one_plane = Mock(return_value=plane)
        flight_repository = FlightRepository()
        flight_repository.save_new_flight = Mock()
        flight = Flight(
            status='ongoing',
            duration=267,
            start_time=datetime(2020, 4, 5, 15, 25, 16),
            identifier=Identifier('0937'),
            position=None
        )

        # When
        result = declare_new_flight(
            plane_identifier=plane_identifier,
            flight=flight,
            plane_repository=plane_repository,
            flight_repository=flight_repository
        )

        # Then
        assert result is None
        flight_repository.save_new_flight.assert_called_with(plane=plane, flight=flight)
