from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from account_api.core.database import Base

# Base.metadata.create_all(bind=engine)

class AccountModel(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bank_name: Mapped[str] = mapped_column(String(50), nullable=False)
    agencia: Mapped[int] = mapped_column(String(10), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    account_type: Mapped[str] = mapped_column(String(20), nullable=False)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"))
    client = relationship("ClientModel", back_populates='account')
