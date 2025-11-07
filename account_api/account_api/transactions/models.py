from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from account_api.configs.database import Base, engine
from account_api.account.models import AccountModel

Base.metadata.create_all(bind=engine)

class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    account: Mapped['AccountModel'] = relationship(back_populates="account", lazy='selectin')
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
