from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    ENV_VAR_1: str


def get_env() -> Env:
    return Env()  # type: ignore
