# Thes are used for extra safety , single source of truth and Validation on startup
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings): 
    APP_NAME: str
    APP_ENV: str

    DATABASE_URL:str
    REDIS_URL:str

    model_config= ConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()    