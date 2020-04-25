from typing import List

from application.PlaneModel import PlaneModel
from business.entities import Plane
from business.repositories import PlaneRepository


class PlaneDatasource(PlaneRepository):
    def __init__(self, session):
        self.session = session

    def get_all_planes(self) -> List[Plane]:
        return self.session.query(PlaneModel).all()
