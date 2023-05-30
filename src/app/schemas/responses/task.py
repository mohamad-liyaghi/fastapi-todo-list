from pydantic import BaseModel, constr
from datetime import datetime


class TaskCreateResponse(BaseModel):
    title: constr(min_length=5, max_length=60)
    description: constr(max_length=255)
    created_at: datetime

    class Config:
        orm_mode = True
