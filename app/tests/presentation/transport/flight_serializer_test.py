from business.entities.Flight import Flight
from presentation.transport.FlightSerializer import FlightSerializer


class FlightSerializerTest:
    class ToJsonTest:
        def test_should_return_the_json_version_of_a_flight(self):
            # Given
            flight = Flight(status='ongoing')

            # When
            json = FlightSerializer.to_json(flight)

            # Then
            assert json == {
                'status': 'ongoing'
            }
