from pydantic import BaseModel, validator, constr
import re


class UserRegisterRequest(BaseModel):
    username: constr(min_length=8, max_length=16)
    password: constr(min_length=8, max_length=32)

    @validator('password')
    def password_contain_special_char(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        return v
