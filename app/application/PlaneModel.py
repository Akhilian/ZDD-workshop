from sqlalchemy import Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlaneModel(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True)
    places = Column(Integer, nullable=True)
