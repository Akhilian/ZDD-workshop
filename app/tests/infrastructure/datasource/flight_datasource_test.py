from datetime import datetime

from freezegun import freeze_time

from business.entities.Flight import Flight
from infrastructure.datasource.FlightDatasource import FlightDatasource
from infrastructure.models.FlightModel import FlightModel


class FlightDatasourceTest():
    class GetAllFlightsTest():
        def test_should_return_an_empty_list_when_no_flight_registered(self, database_session):
            # Given
            flight_datasource = FlightDatasource(database_session)

            # When
            flights = flight_datasource.get_all_flights()

            # Then
            assert len(flights) == 0

        @freeze_time("2019-02-05")
        def test_should_return_all_found_flights(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257

            database_session.add(flight_model)
            flight_datasource = FlightDatasource(database_session)

            # When
            flights = flight_datasource.get_all_flights()

            # Then
            assert len(flights) == 1
            flight = flights[0]
            assert isinstance(flight, Flight)
            assert flight.status == 'ongoing'
            assert flight.duration == 257
            assert flight.start_time == datetime.now()
