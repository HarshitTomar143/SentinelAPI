# Thes are used for extra safety , single source of truth and Validation on startup
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings): 
    APP_NAME: str
    APP_ENV: str

    DATABASE_URL:str
    REDIS_URL:str

    rate_limit_request_count: int = 150
    rate_limit_timeout: float = 10.0
    rate_limit_max_workers: int = 150

    model_config= ConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()    