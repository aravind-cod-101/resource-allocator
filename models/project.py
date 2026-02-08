from sqlalchemy import Column, Text, Integer
from database.base import BASE


class Project(BASE):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
