import pytest
import uuid
from httpx import AsyncClient


async def create_user_and_login(
        client: AsyncClient,
        username: str = 'default_username',
        password: str = 'default_pass#',
) -> None:

    data = {'username': username, 'password': password}

    await client.post("v1/users/register", json=data)

    response = await client.post("v1/users/login", data=data)
    assert response.status_code == 200
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

    async def test_update_task_unauthorized(self) -> None:
        response = await self.client.put("v1/tasks/update/fasf/", data={})
        assert response.status_code == 403

    async def test_update_task(self) -> None:
        await create_user_and_login(self.client)
        task = await self.client.post("/v1/tasks/create", json=self.data)
        task_uuid = task.json()['uuid']
        response = await self.client.put(
            f'v1/tasks/update/{task_uuid}/',
            json={'title': 'updated', 'description': 'updated'}
        )
        assert response.status_code == 200

    async def test_update_task_invalid_uuid(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.put(
            f'v1/tasks/update/{uuid.uuid4()}/',
            json={'title': 'updated', 'description': 'updated'}
        )
        assert response.status_code == 404

    async def test_update_task_no_data(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.put(
            f'v1/tasks/update/{uuid.uuid4()}/'
        )
        assert response.status_code == 422

    async def test_update_others_task(self) -> None:
        await create_user_and_login(self.client)

        others_task = await self.client.post(
            "/v1/tasks/create", json=self.data
        )
        others_task_uuid = others_task.json()['uuid']

        await create_user_and_login(self.client, username='other_user')

        response = await self.client.put(
            f'v1/tasks/update/{others_task_uuid}/',
            json={'title': 'updated', 'description': 'updated'}
        )
        assert response.status_code == 403

    async def test_delete_task_unauthorized(self) -> None:

        response = await self.client.delete(
            f'v1/tasks/delete/{uuid.uuid4()}/',
        )
        assert response.status_code == 403

    async def test_delete_task(self) -> None:
        await create_user_and_login(self.client)
        task = await self.client.post("/v1/tasks/create", json=self.data)
        task_uuid = task.json()['uuid']

        response = await self.client.delete(
            f'v1/tasks/delete/{task_uuid}/',
        )
        assert response.status_code == 200
    
    async def test_delete_invalid_task(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.delete(
            f'v1/tasks/delete/{uuid.uuid4()}/',
        )
        assert response.status_code == 404

    async def test_delete_others_task(self) -> None:
        await create_user_and_login(self.client)

        others_task = await self.client.post(
            "/v1/tasks/create", json=self.data
        )
        others_task_uuid = others_task.json()['uuid']

        await create_user_and_login(self.client, username='other_user')

        response = await self.client.delete(
            f'v1/tasks/delete/{others_task_uuid}/',
        )
        assert response.status_code == 403
