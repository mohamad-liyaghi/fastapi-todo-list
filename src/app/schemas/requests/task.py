from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    title: str
    description: str
