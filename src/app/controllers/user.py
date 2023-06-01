from core.controller import BaseController
from app.repositories import UserRepository
from app.models import User


class UserController(BaseController):
    def __init__(self, user_repository: UserRepository):
        self.model_class = User
        self.repository = user_repository

    async def get_by_id(self, _id: int):
        return await self.repository.get_one(id=_id)
