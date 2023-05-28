from core.repository import BaseRepository
from app.models import User


class UserRepository(BaseRepository):
    """
    Provide all db operations for User model
    """

    async def get_by_username(
        self, username: str
    ) -> User | None:
        """
        Get user by username.

        :param username: Username.
        :param join_: Join relations.
        :return: User.
        """
        return await self.get_one(username=username)
