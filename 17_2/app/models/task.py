from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.backend.db import Base
from sqlalchemy.orm import relationship
from app.models.user import *


class Task(Base):
    __tablename__ = "tasks" # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True) # Уникальный идентификатор
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="tasks")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))