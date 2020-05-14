from business.entities.Flight import Flight
from business.entities.PlaneIdentifier import PlaneIdentifier
from business.entities.UnregisteredPlane import UnregisteredPlane
from business.repositories.FlightRepository import FlightRepository
from business.repositories.PlaneRepository import PlaneRepository


def declare_new_flight(
        plane_identifier: PlaneIdentifier,
        plane_repository: PlaneRepository,
        flight: Flight,
        flight_repository: FlightRepository,
) -> UnregisteredPlane:
    plane = plane_repository.get_one_plane(plane_identifier)

    if not plane:
        return UnregisteredPlane()

    flight_repository.save_new_flight(flight=flight, plane=plane)
