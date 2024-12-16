from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models.task import *


class User(Base):
    __tablename__ = "users" # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True) # Уникальный идентификатор
    username = Column(String)# Имя пользователя
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))