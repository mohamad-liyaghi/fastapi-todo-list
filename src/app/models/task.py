from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True, default='Empty description.')
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='tasks')
