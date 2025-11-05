import databases
import sqlalchemy as sa
from src.config import settings

DATABASE_URL = "sqlite:///./blog.db"

database = databases.Database(settings.database_url)
metadata = sa.MetaData()

if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})