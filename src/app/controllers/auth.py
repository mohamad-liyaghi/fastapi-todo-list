from fastapi import HTTPException, status
from core.controller import BaseController
from core.security import PasswordHandler
from app.repositories import UserRepository
from app.models import User


class AuthController(BaseController):
    def __init__(self, user_repository: UserRepository):
        self.model_class = User
        self.repository = user_repository

    async def register(self, username: str, password: str) -> User:

        user = await self.repository.get_by_username(username)

        if user:
            raise HTTPException(
                detail='User with this username already exists.',
                status_code=status.HTTP_400_BAD_REQUEST
            )        
        hashed_password = PasswordHandler.hash(password)
        return await self.repository.create(
            username=username,
            password=hashed_password
        )
