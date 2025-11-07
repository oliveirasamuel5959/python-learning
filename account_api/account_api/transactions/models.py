from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from account_api.configs.database import Base, engine
# from account_api.client.models import ClientModel

Base.metadata.create_all(bind=engine)

class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, server_default=text('CURRENT_TIMESTAMP'))
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    # client: Mapped['ClientModel'] = relationship("ClientModel", back_populates="transactions", lazy='selectin')
