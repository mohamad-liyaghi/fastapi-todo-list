from typing import Any, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient

from core.database import get_session
import main


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a new FastAPI app
    """
    app = main.app

    yield app


@pytest_asyncio.fixture(scope="function")
async def client(app: FastAPI, db_session) -> AsyncClient:
    """
    Create a new FastAPI AsyncClient
    """

    async def _get_session():
        return db_session

    app.dependency_overrides[get_session] = _get_session

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
