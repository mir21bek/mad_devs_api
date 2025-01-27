from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str = 'mad_devs'
    DB_USER: str = 'postgres'
    DB_PORT: int = 5432
    DB_HOST: str = 'db'
    DB_PASSWORD: str = 'mad12345'
    DB_DRIVER: str = 'postgresql+asyncpg'
    JWT_SECRET_KEY: str = 'secret_key'
    JWT_ENCODE_ALGORITHM: str = 'HS256'

    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
