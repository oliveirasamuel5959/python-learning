from sqlalchemy import Column, Integer, String
from account_api.configs.database import BaseModel

class AccountModel(BaseModel):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    account_type = Column(String)
