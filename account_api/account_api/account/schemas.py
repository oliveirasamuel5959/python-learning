from pydantic import BaseModel

class AccountIn(BaseModel):
    bank_name: str
    agencia: int
    account_type: str

class AccountOut(AccountIn):
    pass