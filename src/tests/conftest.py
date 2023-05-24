import os
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base
from core.config import config


TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

# Override the config to use the test database
config.DATABASE_URL = TEST_DATABASE_URL


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncSession:

    engine = create_async_engine(config.DATABASE_URL, echo=False)
    session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with session() as s:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield s

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        pass

    await engine.dispose()
