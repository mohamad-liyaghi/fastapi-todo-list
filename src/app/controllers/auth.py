from fastapi import HTTPException, status
from core.controller import BaseController
from core.security import PasswordHandler, JWTHandler
from app.repositories import UserRepository
from app.models import User


class AuthController(BaseController):
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    async def register(self, username: str, password: str) -> User:
        user = await self.repository.get_by_username(username)

        if user:
            raise HTTPException(
                detail='User with this username already exists.',
                status_code=status.HTTP_400_BAD_REQUEST)
        hashed_password = PasswordHandler.hash(password)
        return await self.repository.create(
            username=username,
            password=hashed_password
        )

    async def create_access_token(self, username: str, password: str) -> User:
        user = await self.repository.get_by_username(username)

        if not user:
            raise HTTPException(
                detail='User does not found.',
                status_code=status.HTTP_404_NOT_FOUND
            )

        if not PasswordHandler.verify(
            hashed_password=user.password, plain_password=password
        ):
            raise HTTPException(
                detail='Password is not correct.',
                status_code=status.HTTP_403_FORBIDDEN
            )
        return await JWTHandler.create_access_token({'username': username})
