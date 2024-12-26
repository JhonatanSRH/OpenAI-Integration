"""settings module"""
# Python
import os
# Settings libraries
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings class"""
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///database.db")
    debug: bool = os.getenv("DEBUG", "0") == "1"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    class Config:
        """Config class"""
        env_file = "app/config/.env"
        env_file_encoding = "utf-8"

settings = Settings()
