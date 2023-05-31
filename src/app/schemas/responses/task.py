from pydantic import BaseModel, constr
from uuid import UUID
from datetime import datetime


class BaseTaskResponse(BaseModel):
    title: constr(min_length=5, max_length=60)
    description: constr(max_length=255)
    created_at: datetime
    uuid: UUID


class TaskCreateResponse(BaseTaskResponse):

    class Config:
        orm_mode = True


class TaskUpdateResponse(BaseTaskResponse):
    is_completed: bool

    class Config:
        orm_mode = True


class TaskRetrieveResponse(BaseTaskResponse):
    is_completed: bool
    owner_id: int

    class Config:
        orm_mode = True
