from sqlalchemy import Column, Integer, String, DateTime
from uuid import UUID, uuid4
from datetime import datetime


class User:
    """Base user model."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
