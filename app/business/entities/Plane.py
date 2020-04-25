from business.entities import PlaneIdentifier


class Plane():
    def __init__(self, identifier: PlaneIdentifier, number_of_places: int):
        self.identifier = identifier
        self.number_of_places = number_of_places
