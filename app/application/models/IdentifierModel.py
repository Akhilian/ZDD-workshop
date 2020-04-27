from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from application.connection import Base


class IdentifierModel(Base):
    __tablename__ = 'identifier'
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)

    plane = relationship("PlaneModel", uselist=False, back_populates="identifier")
