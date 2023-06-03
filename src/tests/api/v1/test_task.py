import pytest
import uuid
from httpx import AsyncClient
from tests.api.v1.utils import create_user_and_login, create_task


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
        response = await create_task(self.client, self.data)
        assert response.status_code == 201

    async def test_create_task_unauthorized(self) -> None:
        response = await create_task(self.client, self.data)
        assert response.status_code == 403

    async def test_update_task_unauthorized(self) -> None:
        response = await create_task(self.client, self.data)
        assert response.status_code == 403

    async def test_update_task(self) -> None:
        await create_user_and_login(self.client)
        task = await create_task(self.client, self.data)
        task_uuid = task.json()['uuid']
        response = await self.client.put(
            f'v1/tasks/{task_uuid}/',
            json={
                'title': 'updated',
                'description': 'updated',
                'is_completed': 'false'
            }
        )
        assert response.status_code == 200

    async def test_update_task_invalid_uuid(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.put(
            f'v1/tasks/{uuid.uuid4()}/',
            json={
                'title': 'updated',
                'description': 'updated',
                'is_completed': 'false'
            }
        )
        assert response.status_code == 404

    async def test_update_task_no_data(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.put(
            f'v1/tasks/{uuid.uuid4()}/'
        )
        assert response.status_code == 422

    async def test_update_others_task(self) -> None:
        await create_user_and_login(self.client)

        others_task = await create_task(self.client, self.data)
        others_task_uuid = others_task.json()['uuid']

        await create_user_and_login(self.client, username='other_user')

        response = await self.client.put(
            f'v1/tasks/{others_task_uuid}/',
            json={
                'title': 'updated',
                'description': 'updated',
                'is_completed': 'false'
            }
        )
        assert response.status_code == 403

    async def test_delete_task_unauthorized(self) -> None:

        response = await self.client.delete(
            f'v1/tasks/{uuid.uuid4()}/',
        )
        assert response.status_code == 403

    async def test_delete_task(self) -> None:
        await create_user_and_login(self.client)
        task = await create_task(self.client, self.data)
        task_uuid = task.json()['uuid']

        response = await self.client.delete(
            f'v1/tasks/{task_uuid}/',
        )
        assert response.status_code == 200

    async def test_delete_invalid_task(self) -> None:
        await create_user_and_login(self.client)

        response = await self.client.delete(
            f'v1/tasks/{uuid.uuid4()}/',
        )
        assert response.status_code == 404

    async def test_delete_others_task(self) -> None:
        await create_user_and_login(self.client)

        others_task = await create_task(self.client, self.data)
        others_task_uuid = others_task.json()['uuid']

        await create_user_and_login(self.client, username='other_user')

        response = await self.client.delete(
            f'v1/tasks/{others_task_uuid}/',
        )
        assert response.status_code == 403

    async def test_task_detail_unauthorized(self):
        response = await self.client.get(f'v1/tasks/{uuid.uuid4()}/',)
        assert response.status_code == 403

    async def test_task_detail(self):
        await create_user_and_login(self.client)
        task = await create_task(self.client, self.data)
        task_uuid = task.json()['uuid']
        response = await self.client.get(f'v1/tasks/{task_uuid}/')
        assert response.status_code == 200

    async def test_others_task_detail(self):
        await create_user_and_login(self.client)
        others_task = await create_task(self.client, self.data)
        others_task_uuid = others_task.json()['uuid']

        await create_user_and_login(self.client, username='other_user')
        response = await self.client.get(f'v1/tasks/{others_task_uuid}/')
        assert response.status_code == 403

    async def test_invalid_task_detail(self):
        await create_user_and_login(self.client)
        response = await self.client.get(f'v1/tasks/{uuid.uuid4()}/')
        assert response.status_code == 404

    async def test_task_list_unauthorized(self):
        response = await self.client.get('v1/tasks/')
        assert response.status_code == 403

    async def test_empty_task_list(self):
        await create_user_and_login(self.client)
        response = await self.client.get('v1/tasks/')
        assert response.status_code == 200
        assert response.json() == []

    async def test_task_list(self):
        await create_user_and_login(self.client)
        await create_task(self.client, self.data)
        response = await self.client.get('v1/tasks/')
        assert response.status_code == 200
        assert response.json() != []
