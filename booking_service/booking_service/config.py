from pydantic_settings import BaseSettings

class EnvBaseSettings(BaseSettings):
    class Config:
        env_file = ".env"


class DjangoSettings(EnvBaseSettings):
    DJANGO_SECRET: str
    DJANGO_DEBUG: bool

class PostgreSettings(EnvBaseSettings):
    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASS: str
    DB_NAME: str


class Settings(DjangoSettings, PostgreSettings):
    pass

settings = Settings()
