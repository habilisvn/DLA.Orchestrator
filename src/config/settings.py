from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgresql_prefix_async: str
    postgresql_prefix_sync: str
    postgresql_db_name: str
    postgresql_username: str
    postgresql_password: str
    postgresql_host: str
    postgresql_port: int
    mongo_url: str
    mongo_db_name: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int
    jwt_refresh_token_expire_days: int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()  # type: ignore
