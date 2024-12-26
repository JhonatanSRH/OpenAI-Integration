"""settings module"""
# Python
import os
# Settings libraries
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv("config/.env")

class Settings(BaseSettings):
    """Settings class"""
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///database.db")
    debug: bool = os.getenv("DEBUG", "0") == "1"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
