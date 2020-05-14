from sqlalchemy import Integer, \
    Column, \
    ForeignKey, \
    String, \
    DateTime, \
    Float
from sqlalchemy.orm import relationship
from presentation.connection import Base


class PositionModel(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    flightId = Column(Integer, ForeignKey('flights.id'), nullable=True)
    flight = relationship("FlightModel", back_populates="positions")
