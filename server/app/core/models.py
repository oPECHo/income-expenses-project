from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    body = Column(String)
    amount = Column(Float)
    tag = Column(String)
    transaction_type = Column(String, ForeignKey('type_transactions.title'))

    type_tra = relationship("Type_transaction", back_populates="types")

class Type_transaction(Base):
    __tablename__ = 'type_transactions'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    types = relationship("Transaction", back_populates="type_tra")


    