import datetime
from pydantic import BaseModel

class TransactionBase(BaseModel):
    date: datetime.date
    body: str
    amount: float
    tag: str
    transaction_type: str

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True

class ShowDeatil(TransactionBase):
    class Config:
        orm_mode = True
