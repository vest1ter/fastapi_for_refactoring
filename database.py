from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:yourpassword@localhost:5432/todoapp"

# Создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
