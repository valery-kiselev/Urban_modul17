from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Создаём движок для подключения к базе данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)
# Создаём фабрику сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)
# Базовый класс для всех моделей SQLAlchemy

Base = declarative_base()