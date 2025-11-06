# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# engine = create_engine("postgresql+asyncpg://account:account@localhost:5432/account")
# SessionLocal = sessionmaker(autocommit=False, bind=engine)
# session = Session()

# Base = declarative_base()

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from pydantic import Field
from pydantic_settings import BaseSettings

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://account:account@localhost:5432/account')

settings = Settings()

engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(
    engine, class_= AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
