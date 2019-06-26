from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from database.base import Base
from models.user import User


class UserTableModel(Base, User):
    __tablename__='user_table'
    name_max_length = 500
    title_max_length = 1000
    position_max_length = 10000
    summary_max_length = 10000
    skills_max_length = 10000
    experience_max_length = 30000
    education_max_length = 10000

    id = Column(Integer, primary_key=True)
    name = Column(String(name_max_length), default="")
    title = Column(String(title_max_length), default="")
    position = Column(String(position_max_length), default="")
    summary = Column(String(summary_max_length), default="")
    skills = Column(String(skills_max_length), default="")
    experience = Column(String(experience_max_length), default="")
    education = Column(String(education_max_length), default="")
