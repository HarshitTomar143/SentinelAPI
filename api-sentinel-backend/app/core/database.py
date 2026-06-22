from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#Creating the engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

# Creating the session 
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit= False
)