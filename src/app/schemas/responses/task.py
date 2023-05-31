from pydantic import BaseModel, constr
from uuid import UUID
from datetime import datetime


class BaseTaskResponse(BaseModel):
    title: constr(min_length=5, max_length=60)
    description: constr(max_length=255)
    created_at: datetime


class TaskCreateResponse(BaseTaskResponse):
    uuid: UUID

    class Config:
        orm_mode = True


class TaskUpdateResponse(BaseTaskResponse):
    uuid: UUID
    
    class Config:
        orm_mode = True
