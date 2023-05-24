from dotenv import load_dotenv
from core.config import config
import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

engine = create_async_engine(
    config.DATABASE_URL, echo=os.environ.get('DATABASE_ECHO', False)
)

async_session = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncSession:
    '''Return a database session'''
    async with async_session() as session:
        yield session


Base = declarative_base()
