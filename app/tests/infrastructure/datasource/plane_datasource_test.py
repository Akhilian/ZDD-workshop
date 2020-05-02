from business.entities.Plane import Plane
from business.entities.PlaneIdentifier import PlaneIdentifier
from infrastructure.datasource.PlaneDatasource import PlaneDatasource
from infrastructure.models.IdentifierModel import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel


class PlaneDatasourceTest():
    class GetAllPlanesTest():
        def test_should_return_an_empty_array_when_no_plane_registered(self, database_session):
            # Given
            plane_datasource = PlaneDatasource(database_session)

            # When
            planes = plane_datasource.get_all_planes()

            # Then
            assert len(planes) == 0

        def test_should_return_every_registered_planed(self, database_session):
            # Given
            identifier_model = IdentifierModel()
            identifier_model.code = 'FDY-198'
            database_session.add(identifier_model)

            plane_model = PlaneModel()
            plane_model.places = 145
            plane_model.identifier = identifier_model
            database_session.add(plane_model)

            plane_datasource = PlaneDatasource(session=database_session)

            # When
            planes = plane_datasource.get_all_planes()

            # Then
            assert len(planes) == 1
            assert isinstance(planes[0], Plane)

            plane = planes[0]
            assert plane.number_of_places == 145
            assert plane.identifier.code == 'FDY-198'

    class AddNewPlaneTest():
        def test_should_save_the_plane_in_the_database(self, database_session):
            # Given
            plane = Plane(identifier=PlaneIdentifier('GAF-531'), number_of_places=145)

            plane_datasource = PlaneDatasource(database_session)

            # When
            plane_datasource.add_new_plane(plane=plane)

            # Then
            assert database_session.query(PlaneModel).count() == 1
            assert database_session.query(IdentifierModel).count() == 1
