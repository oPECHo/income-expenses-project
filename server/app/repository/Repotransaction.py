from typing import Optional
from bson import ObjectId
from fastapi import Body, HTTPException, status
from ..core.models import Transaction, UpdateTransaction
from fastapi.encoders import jsonable_encoder
from ..core.database import db
from fastapi.responses import JSONResponse

async def Search(
    id: Optional[str] = None,
    tag: Optional[str] = None,
    transaction_type: Optional[str] = None
):
    if not id and not tag and not transaction_type:
        return await db['transactions'].find().to_list(1000)
    
    if id:
        transaction = await db['transactions'].find({'_id': id}).to_list(1000)
        if not transaction:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the ID [{id}] is not available')
        return transaction

    if tag:
        transactions = await db['transactions'].find({'tag': tag}).to_list(1000)
        if not transactions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the Tag [{tag}] is not available')
        return transactions

    if transaction_type:
        transactions = await db['transactions'].find({'transaction_type': transaction_type}).to_list(1000)
        if not transactions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f'Transaction with the Type [{transaction_type}] is not available')
        return transactions

async def create(transaction: Transaction = Body(...)):
    transaction = jsonable_encoder(transaction)
    new_transaction = await db["transactions"].insert_one(transaction)
    created_transaction = await db["transactions"].find_one({"_id": new_transaction.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_transaction)

async def destroy(id:str):
    result = await db['transactions'].delete_one({"_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transaction with id [{id}] not found')
    return 'done'

async def update(id:str, transaction: UpdateTransaction = Body(...)):
    transaction = {k: v for k, v in transaction.dict().items() if v is not None}
    if len(transaction) >= 1:
        update_result = await db["transactions"].update_one({"_id": id}, {"$set": transaction})
        if update_result.modified_count == 1:
            if (updated_transaction := await db["students"].find_one({"_id": id})) is not None:
                return updated_transaction
    if (existing_transaction := await db["transactions"].find_one({"_id": id})) is not None:
        return existing_transaction
    raise HTTPException(status_code=404, detail=f"Student {id} not found")
