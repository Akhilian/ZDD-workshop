from datetime import datetime

from freezegun import freeze_time

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Position import Position
from presentation.transport.FlightSerializer import FlightSerializer


class FlightSerializerTest:
    class ToJsonTest:
        def test_should_return_the_json_version_of_a_flight(self):
            # Given
            flight = Flight(
                status='ongoing',
                duration=267,
                start_time=datetime(2020, 4, 5, 15, 25, 16),
                identifier=Identifier('0937'),
                position=None
            )

            # When
            json = FlightSerializer.to_json(flight)

            # Then
            assert json == {
                'status': 'ongoing',
                'duration': 267,
                'start_time': '2020-04-05T15:25:16',
                'identifier': '0937',
                'position': None
            }

        def test_should_serialize_even_an_array(self):
            # Given
            flights = [Flight(
                status='ongoing',
                duration=267,
                start_time=datetime(2020, 4, 5, 15, 25, 16),
                identifier=Identifier('0937'),
                position=Position(latitude=15.4156, longitude=54.2567)
            )]

            # When
            json = FlightSerializer.to_json(flights)

            # Then
            assert json == [{
                'status': 'ongoing',
                'duration': 267,
                'start_time': '2020-04-05T15:25:16',
                'identifier': '0937',
                'position': {
                    'latitude': 15.4156,
                    'longitude': 54.2567
                }
            }]

    class FromJsonTest:
        @freeze_time("2020-04-13")
        def test_should_turn_payload_to_Flight(self):
            # Given
            payload = {
                "status": 'ongoing',
                "duration": 2456,
                "start_time": datetime.now(),
                "identifier": 'FAA-331'
            }

            # When
            flight = FlightSerializer.from_json(payload)

            # Then
            assert isinstance(flight, Flight)
            assert isinstance(flight.identifier, Identifier)
            assert flight.status == 'ongoing'
            assert flight.duration == 2456
            assert flight.start_time == datetime.now()
            assert flight.identifier.value == 'FAA-331'
