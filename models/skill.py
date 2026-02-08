from sqlalchemy import Column, Text, Integer
from database.base import BASE

class Skill(BASE):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)