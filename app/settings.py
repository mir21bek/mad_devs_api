from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    DB_NAME: str = 'mad'
    DB_USER: str = 'mad12345'
    DB_PORT: int = 5432
    DB_HOST: str = 'db'
    DB_PASSWORD: str = 'password'
    DB_DRIVER: str = 'postgresql+psycopg2'

    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
