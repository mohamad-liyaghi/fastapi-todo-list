from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from core.database import Base
from app.models.task import Task


class User(Base):
    """Base user model."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(
        UUID(as_uuid=True), default=uuid4, unique=True, nullable=False
    )
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship('Task', back_populates='owner')
