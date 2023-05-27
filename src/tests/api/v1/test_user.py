import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
class TestUserRouter:

    @pytest.fixture(autouse=True)
    def setup_method(self, client: AsyncClient) -> None:
        self.data = {
            'username' : 'fake_user', 
            'password' : '1234FakePASS#012'
        }
        self.client = client
    
    async def test_register_user(self) -> None:
        """Test user creation."""        
        response = await self.client.post("v1/users/register", json=self.data)
        assert response.status_code == 201
        assert response.json()["username"] == self.data["username"]
        assert response.json()["uuid"] is not None

    async def test_duplicate_register_user(self) -> None:
        """Test user creation."""
        response = await self.client.post("v1/users/register", json=self.data)
        assert response.status_code == 201
        response = await self.client.post("v1/users/register", json=self.data)
        assert response.status_code == 400

    async def test_register_with_short_username(self) -> None:
        """Test user creation."""
        self.data['username'] = 'r'
        response = await self.client.post("v1/users/register", json=self.data)
        assert response.status_code == 422

    async def test_register_with_short_password(self) -> None:
        """Test user creation."""
        self.data['password'] = '1'
        response = await self.client.post("v1/users/register", json=self.data)
        assert response.status_code == 422
