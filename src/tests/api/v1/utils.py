from httpx import AsyncClient


async def create_user_and_login(
    client: AsyncClient,
    username: str = 'default_username',
    password: str = 'default_pass#',
) -> None:
    """
    Create a new user and set its access token to Authorization header
    """
    data = {'username': username, 'password': password}

    await client.post("v1/users/register", json=data)

    response = await client.post("v1/users/login", data=data)
    assert response.status_code == 200
    access_token = response.json()["access_token"]

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    return None


async def create_task(
    client: AsyncClient,
    data: dict = {
        'title': 'default title',
        'description': 'default description'
    }
) -> dict:
    """
    Create a new task and return it
    """
    task_response = await client.post("/v1/tasks/", json=data)
    return task_response
