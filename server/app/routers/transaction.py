from typing import List, Optional
from fastapi import APIRouter, Depends, status,  Query

from ..core import database
from ..schemas import ScTrans
from sqlalchemy.orm import Session
from ..repository import Repotransaction

router = APIRouter(
    prefix="/transaction",
    tags=['Transaction']
)

get_db = database.get_db

@router.get('/',response_model=List[ScTrans.Transaction])
async def Search(id: Optional[int] = Query(None), db : Session = Depends(get_db), tag: Optional[str] = Query(None),transaction_type: Optional[str] = Query(None)):
    return Repotransaction.Search(id, db, tag, transaction_type)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: ScTrans.TransactionBase, db : Session = Depends(get_db)):
    return Repotransaction.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id:int, db: Session = Depends(get_db)):
    return Repotransaction.destroy(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(id:int, request: ScTrans.TransactionBase, db: Session = Depends(get_db)):
    return Repotransaction.update(id, request, db)
