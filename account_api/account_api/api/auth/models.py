from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import datetime
from account_api.core.database import Base

class TokenModel(Base):
    __tablename__ = "token"

    user_id: Mapped[int] = mapped_column(Integer)
    access_token: Mapped[str] = mapped_column(String(450), primary_key=True)
    refresh_token: Mapped[str] = mapped_column(String(450), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
