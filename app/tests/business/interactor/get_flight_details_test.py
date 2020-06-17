from unittest.mock import Mock

from business.entities.Identifier import Identifier
from business.entities.Position import Position
from business.entities.UndeclaredFlight import UndeclaredFlight
from business.interactors.get_flight_details import get_flight_details
from business.repositories.FlightRepository import FlightRepository


class GetFlightDetailsTest():
    def test_should_return_an_undeclared_flight_message_when_flight_does_not_exist(self):
        # Given
        flight_repository = FlightRepository()
        flight_repository.get_one_flight = Mock(return_value=None)
        identifier = Identifier('DYFGU')

        # When
        result = get_flight_details(repository=flight_repository, identifier=identifier)

        # Then
        flight_repository.get_one_flight.assert_called_once_with(identifier=identifier)
        assert isinstance(result, UndeclaredFlight)
