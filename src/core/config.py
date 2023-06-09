import os
from enum import Enum
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = False


class Config(BaseConfig):
    DEBUG: int = os.environ.get('DEBUG', 0)
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: EnvironmentType = os.environ.get(
        'ENVIRONMENT', EnvironmentType.DEVELOPMENT
    )
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'secret-key')
    DATABASE_URL: str = os.environ.get('DATABASE_URL', None)


config: Config = Config()
