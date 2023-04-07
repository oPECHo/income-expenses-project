from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Query
from ..core import models
from ..schemas import ScTrans
from ..core.database import get_db

def Search(
    id:Optional[int] = Query(None),
    db: Session = Depends(get_db),
    tag: Optional[str] = Query(None),
    transaction_type: Optional[str] = Query(None)
):
    if not id and not tag and not transaction_type:
        return db.query(models.Transaction).all()
    
    if id:
        transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
        if not transaction:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the ID [{id}] is not available')
        return [transaction]

    if tag:
        transactions = db.query(models.Transaction).filter(models.Transaction.tag == tag).all()
        if not transactions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the Tag [{tag}] is not available')
        return transactions

    if transaction_type:
        transactions = db.query(models.Transaction).filter(models.Transaction.transaction_type == transaction_type).all()
        if not transactions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the Type [{transaction_type}] is not available')
        return transactions

def create(request,db: Session):
    new_transaction = models.Transaction(date=request.date, body=request.body, amount=request.amount,tag=request.tag, transaction_type=request.transaction_type)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def destroy(id:int, db: Session):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transaction with id [{id}] not found')
    transaction.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:ScTrans, db: Session):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transaction with id [{id}] not found')
    transaction.date = request.date
    transaction.body = request.body
    transaction.amount = request.amount
    transaction.tag = request.tag
    transaction.transaction_type = request.transaction_type
    db.commit()
    return 'updated'
