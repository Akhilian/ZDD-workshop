from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from presentation.connection import Base


class FlightModel(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)

    identifier = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    status = Column(String, nullable=False)
    position = Column(String, nullable=True)

    planeId = Column(Integer, ForeignKey('planes.id'), nullable=False)
    plane = relationship("PlaneModel", back_populates="flight")
