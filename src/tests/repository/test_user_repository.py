import pytest
from app.repositories import UserRepository
from app.models import User

@pytest.mark.asyncio
class TestUserRepository:

    @pytest.fixture(autouse=True)
    def setup_method(self, db_session) -> None:
        self.username = 'fake_username'
        self.user_repository = UserRepository(model=User, session=db_session)
    
    async def test_get_user_by_username(self, setup_method) -> None:
        created_user = await self.user_repository.create(username=self.username, password='fake_pass')
        user = await self.user_repository.get_by_username(self.username)
        assert user.id == created_user.id

    async def test_get_user_by_invalid_username(self, setup_method) -> None:
        user = await self.user_repository.get_by_username('fakeusername')
        assert user is None