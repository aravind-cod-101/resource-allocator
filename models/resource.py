from sqlalchemy import Column, Text, Integer
from database.base import BASE


class Resource(BASE):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
