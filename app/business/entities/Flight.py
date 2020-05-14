from business.entities.Identifier import Identifier


class Flight():
    def __init__(self, status, duration, start_time, identifier: Identifier):
        self.status = status
        self.duration = duration
        self.start_time = start_time
        self.identifier = identifier
