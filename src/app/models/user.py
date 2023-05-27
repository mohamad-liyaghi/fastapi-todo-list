from sqlalchemy import Column, Integer, String, DateTime
from uuid import uuid4
from datetime import datetime
from core.database import Base


class User(Base):
    """Base user model."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String, default=str(uuid4()), unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
