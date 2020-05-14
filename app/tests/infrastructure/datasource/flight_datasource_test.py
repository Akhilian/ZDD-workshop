from datetime import datetime

from freezegun import freeze_time

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from infrastructure.datasource.FlightDatasource import FlightDatasource
from infrastructure.models.FlightModel import FlightModel


class FlightDatasourceTest():
    class GetAllFlightsTest():
        def test_return_an_empty_list_when_no_flight_registered(self, database_session):
            # Given
            flight_datasource = FlightDatasource(database_session)

            # When
            flights = flight_datasource.get_all_flights()

            # Then
            assert len(flights) == 0

        @freeze_time("2019-02-05")
        def test_return_all_found_flights(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.identifier = '5835'
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

    class GetOneFlightTest():
        @freeze_time("2019-02-05")
        def test_return_the_found_flight(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.identifier = '3558'
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257

            database_session.add(flight_model)
            flight_datasource = FlightDatasource(database_session)

            # When
            flight = flight_datasource.get_one_flight(Identifier('3558'))

            # Then
            assert flight
            assert isinstance(flight, Flight)
            assert flight.status == 'ongoing'
            assert flight.duration == 257
            assert flight.identifier == '3558'
            assert flight.start_time == datetime.now()

        @freeze_time("2019-02-05")
        def test_return_none_when_the_flight_does_not_exist(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.identifier = 3558
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257

            database_session.add(flight_model)
            flight_datasource = FlightDatasource(database_session)

            # When
            flight = flight_datasource.get_one_flight(Identifier('2456'))

            # Then
            assert flight is None
