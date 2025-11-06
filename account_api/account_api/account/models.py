from sqlalchemy import Column, Integer, String
from account_api.configs.database import Base

class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, index=True)
    agencia = Column(String)
    account_type = Column(String, index=True)
