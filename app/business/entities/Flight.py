from typing import Union

from business.entities.Identifier import Identifier
from business.entities.Position import Position


class Flight():
    def __init__(self, status, duration, start_time, identifier: Identifier, position: Union[Position, None]):
        self.status = status
        self.duration = duration
        self.start_time = start_time
        self.identifier = identifier
        self.position = position
