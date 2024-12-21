
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models.user import *

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    # Связь с моделью User
    user = relationship("User", back_populates="tasks")

# Примеры вывода SQL-запросов для создания таблиц
from sqlalchemy.schema import CreateTable
print("SQL для Task:")
print(CreateTable(Task.__table__))

print("\nSQL для User:")
print(CreateTable(User.__table__))