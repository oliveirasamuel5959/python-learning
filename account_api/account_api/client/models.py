from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from account_api.configs.database import Base

class ClientModel(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    sexo: Mapped[str] = mapped_column(String(20), nullable=False)
    transactions: Mapped[List["TransactionModel"]] = relationship("TransactionModel", back_populates="client")
    account: Mapped["AccountModel"] = relationship("AccountModel", back_populates="client")
