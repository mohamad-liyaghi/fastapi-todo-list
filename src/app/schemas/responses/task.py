from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class BaseTaskResponse(BaseModel):
    title: str
    created_at: datetime
    uuid: UUID


class TaskCreateResponse(BaseTaskResponse):
    description: str

    class Config:
        orm_mode = True


class TaskUpdateResponse(BaseTaskResponse):
    description: str
    is_completed: bool

    class Config:
        orm_mode = True


class TaskRetrieveResponse(BaseTaskResponse):
    description: str
    is_completed: bool
    owner_id: int

    class Config:
        orm_mode = True


class TaskListResponse(BaseTaskResponse):
    class Config:
        orm_mode = True
