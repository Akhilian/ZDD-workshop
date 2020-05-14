from datetime import datetime

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from presentation.transport.FlightSerializer import FlightSerializer


class FlightSerializerTest:
    class ToJsonTest:
        def test_should_return_the_json_version_of_a_flight(self):
            # Given
            flight = Flight(
                status='ongoing',
                duration=267,
                start_time=datetime(2020, 4, 5, 15, 25, 16),
                identifier=Identifier('0937')
            )

            # When
            json = FlightSerializer.to_json(flight)

            # Then
            assert json == {
                'status': 'ongoing',
                'duration': 267,
                'start_time': '2020-04-05T15:25:16',
                'identifier': '0937'
            }

        def test_should_serialize_even_an_array(self):
            # Given
            flights = [Flight(
                status='ongoing',
                duration=267,
                start_time=datetime(2020, 4, 5, 15, 25, 16),
                identifier=Identifier('0937')
            )]

            # When
            json = FlightSerializer.to_json(flights)

            # Then
            assert json == [{
                'status': 'ongoing',
                'duration': 267,
                'start_time': '2020-04-05T15:25:16',
                'identifier': '0937'
            }]
