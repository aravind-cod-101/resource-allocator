from sqlalchemy import Column, Text, Integer, ForeignKey, Date
from database.base import BASE

class ResourceAvailability(BASE):
    __tablename__ = "resource_availability"
    
    id = Column(Integer, primary_key=True)
    resource_id = Column(Integer, ForeignKey('resources.id'), nullable=False)
    available_from = Column(Date, nullable=False)
    available_to = Column(Date, nullable=False) 