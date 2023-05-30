import pytest
from httpx import AsyncClient


async def create_user_and_login(client: AsyncClient) -> None:
    data = {'username': 'fake_user', 'password': '1234FakePASS#012'}

    await client.post("v1/users/register", json=data)

    response = await client.post("v1/users/login", data=data)
    access_token = response.json()["access_token"]

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    return None


@pytest.mark.asyncio
class TestTaskRouter:

    @pytest.fixture(autouse=True)
    def setup_method(self, client: AsyncClient) -> None:
        self.data = {
            'title': 'Test task',
            'description': 'Test description'
        }
        self.client = client

    async def test_create_task(self) -> None:
        await create_user_and_login(self.client)
        response = await self.client.post("/v1/tasks/create", json=self.data)
        assert response.status_code == 201

    async def test_create_task_unauthorized(self) -> None:
        response = await self.client.post("/v1/tasks/create", data={})
        assert response.status_code == 403
