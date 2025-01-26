from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    DB_NAME = 'mad'
    DB_USER = 'mad12345'
    DB_PORT = 5432
    DB_HOST = 'db'
    DB_PASSWORD = 'password'
    DB_DRIVER = 'postgresql+asyncpg'
    JWT_SECRET_KEY = 'secret_key'
    JWT_ENCODE_ALGORITHM = 'HS256'

    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
