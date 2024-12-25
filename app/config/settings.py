"""settings module"""
# Python
import os
# Settings libraries
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    """Settings class"""
    database_url: str = os.getenv("DATABASE_URL")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
