from sqlalchemy import Column, Text, Integer, ForeignKey
from database.base import BASE


class ResourceSkill(BASE):
    __tablename__ = "resource_skill"

    resource_id = Column(Integer, ForeignKey("resources.id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)
