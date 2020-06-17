from datetime import datetime
from unittest.mock import Mock

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Position import Position
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.interactors.add_new_position_for_a_flight import add_new_position_for_a_flight
from business.repositories.FlightRepository import FlightRepository


class AddNewPositionForAFlightTest():
    def test_should_return_an_undeclared_plane_message_when_plane_does_not_exist(self):
        # Given
        position = Position(latitude=40.714, longitude=-74.006)
        flight_repository = FlightRepository()
        flight_repository.get_one_flight = Mock(return_value=None)
        identifier = Identifier('DYFGU')

        # When
        result = add_new_position_for_a_flight(flight_repository, position, identifier=identifier)

        # Then
        assert isinstance(result, UndeclaredFlight)
        flight_repository.get_one_flight.assert_called_once_with(identifier)

    def test_save_the_new_position(self):
        # Given
        position = Position(latitude=40.714, longitude=-74.006)
        flight_repository = FlightRepository()
        flight = Flight(
            status='ongoing',
            duration=1456,
            start_time=datetime(2020, 4, 5, 15, 25, 16),
            identifier=Identifier('0937'),
            position=None
        )
        flight_repository.get_one_flight = Mock(
            return_value=flight
        )
        flight_repository.save_new_position = Mock()

        # When
        add_new_position_for_a_flight(flight_repository, position, identifier=Identifier('DYFGU'))

        # Then
        flight_repository.save_new_position.assert_called_once_with(flight, position)


    def test_does_not_return_undeclared_flight_when_new_position_is_saved(self):
        # Given
        position = Position(latitude=40.714, longitude=-74.006)
        flight_repository = FlightRepository()
        flight = Flight(
            status='ongoing',
            duration=1456,
            start_time=datetime(2020, 4, 5, 15, 25, 16),
            identifier=Identifier('0937'),
            position=None
        )
        flight_repository.get_one_flight = Mock(
            return_value=flight
        )
        flight_repository.save_new_position = Mock(return_value=None)

        # When
        result = add_new_position_for_a_flight(flight_repository, position, identifier=Identifier('DYFGU'))

        # Then
        assert result is None
