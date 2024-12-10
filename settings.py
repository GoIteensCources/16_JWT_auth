from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra="allow")
    DEBUG: bool = True

    ALGORITHM: str = ""
    SECRET_KEY: str = "secret_key-123"
    ACCESS_TOKEN_EXPIRE_MIN = 1


settings = Settings()
