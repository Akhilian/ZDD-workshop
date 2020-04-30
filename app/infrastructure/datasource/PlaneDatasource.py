from typing import List

from infrastructure.models import IdentifierModel
from infrastructure.models.PlaneModel import PlaneModel
from business.entities import Plane, PlaneIdentifier
from business.repositories import PlaneRepository


class PlaneDatasource(PlaneRepository):
    def __init__(self, session):
        self.session = session

    def get_all_planes(self) -> List[Plane]:
        planes = self.session.query(PlaneModel).all()
        return [
            Plane(identifier=PlaneIdentifier(plane.identifier.code), number_of_places=plane.places)
            for plane in planes
        ]

    def add_new_plane(self, plane: Plane) -> None:
        plane_model = PlaneModel()
        plane_model.places = plane.number_of_places
        plane_model.identifier = IdentifierModel()
        plane_model.identifier.code = plane.identifier.code

        self.session.add(plane_model)
        self.session.commit()
