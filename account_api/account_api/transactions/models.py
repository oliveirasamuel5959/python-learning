from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, text
from pydantic import UUID4
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from account_api.configs.database import Base, engine
# from account_api.client.models import ClientModel

# Base.metadata.create_all(bind=engine)

class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id", name="fk_client"))
    client = relationship("ClientModel", back_populates='transactions')

