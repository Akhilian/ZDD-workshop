from datetime import datetime

from freezegun import freeze_time

from business.entities.Flight import Flight
from business.entities.Identifier import Identifier
from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.entities.Position import Position
from infrastructure.datasource.FlightDatasource import FlightDatasource
from infrastructure.models.FlightModel import FlightModel
from infrastructure.models.IdentifierModel import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel


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
            flight_model.position = "40.714,-74.006"

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
            assert isinstance(flight.position, Position)
            assert flight.position.latitude == 40.714
            assert flight.position.longitude == -74.006
            assert isinstance(flight.identifier, Identifier)
            assert flight.identifier.value == '5835'

        @freeze_time("2019-02-05")
        def test_return_(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.identifier = '5835'
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257
            flight_model.position = None

            database_session.add(flight_model)
            flight_datasource = FlightDatasource(database_session)

            # When
            flights = flight_datasource.get_all_flights()

            # Then
            assert len(flights) == 1
            flight = flights[0]
            assert flight.position is None

    class GetOneFlightTest():
        @freeze_time("2019-02-05")
        def test_return_the_found_flight(self, database_session):
            # Given
            flight_model = FlightModel()
            flight_model.identifier = '3558'
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257
            flight_model.position = "40.714,-74.006"

            database_session.add(flight_model)
            flight_datasource = FlightDatasource(database_session)

            # When
            flight = flight_datasource.get_one_flight(Identifier('3558'))

            # Then
            assert flight
            assert isinstance(flight, Flight)
            assert flight.status == 'ongoing'
            assert flight.duration == 257
            assert isinstance(flight.position, Position)
            assert flight.position.latitude == 40.714
            assert flight.position.longitude == -74.006
            assert isinstance(flight.identifier, Identifier)
            assert flight.identifier.value == '3558'
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

    class SaveNewPositionTest():
        @freeze_time("2019-02-05")
        def test_attach_a_new_position_for_a_flight(self, database_session):
            # Given
            position = Position(latitude=40.714, longitude=-74.006)
            flight_model = FlightModel()
            flight_model.identifier = '2VG5'
            flight_model.status = 'ongoing'
            flight_model.start_time = datetime.now()
            flight_model.duration = 257
            database_session.add(flight_model)

            flight = Flight(
                identifier=Identifier('2VG5'),
                status='ongoing',
                start_time=datetime.now(),
                duration=937,
                position=None
            )

            flight_datasource = FlightDatasource(database_session)

            # When
            flight_datasource.save_new_position(flight, position)

            # Then
            flight = database_session.query(FlightModel) \
                .filter(FlightModel.identifier == '2VG5').first()
            assert flight is not None
            assert flight.position == "40.714,-74.006"

    class SaveNewFlightTest():
        def test_save_flight_when_plane_exists(self, database_session):
            # Given
            identifier_model = IdentifierModel()
            identifier_model.code = 'FDY-198'
            database_session.add(identifier_model)

            plane_model = PlaneModel()
            plane_model.places = 145
            plane_model.identifier = identifier_model
            database_session.add(plane_model)

            flight = Flight(
                identifier=Identifier('2VG5'),
                status='ongoing',
                start_time=datetime.now(),
                duration=937,
                position=None
            )
            plane = Plane(
                identifier=PlaneIdentifier('FDY-198'),
                number_of_places=23
            )

            flight_datasource = FlightDatasource(database_session)

            # When
            flight_datasource.save_new_flight(flight, plane)

            # Then
            assert database_session.query(FlightModel).count() == 1
            saved_flight = database_session.query(FlightModel).first()
            assert saved_flight.plane.identifier.code == 'FDY-198'
