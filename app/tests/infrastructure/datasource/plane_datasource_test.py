import pytest

from application.PlaneModel import PlaneModel
from infrastructure.datasource import PlaneDatasource


class PlaneDatasourceTest():
    class GetAllPlanesTest():
        def test_should_return_an_empty_array_when_no_plane_registered(self, database_session):
            # Given
            plane_datasource = PlaneDatasource(database_session)

            # When
            planes = plane_datasource.get_all_planes()

            # Then
            assert len(planes) == 0

        def test_should_every_registered_planed(self, database_session):
            # Given
            plane_model = PlaneModel()
            plane_model.places = 145
            database_session.add(plane_model)
            plane_datasource = PlaneDatasource(session=database_session)

            # When
            planes = plane_datasource.get_all_planes()

            # Then
            assert len(planes) == 1
