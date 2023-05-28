from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class UserRegisterResponse(BaseModel):
    username: str
    uuid: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class UserAccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
