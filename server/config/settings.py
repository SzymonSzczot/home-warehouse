from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    api_domain: str
    db_user: str
    db_password: str

    model_config = SettingsConfigDict(env_file="config/.env")


@lru_cache
def get_settings():
    return Settings()
