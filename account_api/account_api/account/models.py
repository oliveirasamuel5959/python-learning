from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from account_api.configs.database import Base, engine

Base.metadata.create_all(bind=engine)

class AccountModel(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bank_name: Mapped[str] = mapped_column(String(50), nullable=False)
    agencia: Mapped[int] = mapped_column(Integer, nullable=False)
    account_type: Mapped[str] = mapped_column(String(20), nullable=False)
