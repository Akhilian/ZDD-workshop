from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from presentation.connection import Base


class PlaneModel(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True)
    places = Column(Integer, nullable=True)

    planeIdentifierId = Column(Integer, ForeignKey('identifier.id'), nullable=False)
    identifier = relationship("IdentifierModel", back_populates="plane")
