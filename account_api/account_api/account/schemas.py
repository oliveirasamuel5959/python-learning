from pydantic import BaseModel

class AccountIn(BaseModel):
    account_type: str

class AccountOut(AccountIn):
    pass