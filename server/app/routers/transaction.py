from typing import List, Optional
from fastapi import APIRouter, Depends, status,  Query, Body
from ..utils import OAuth2
from ..schemas import Scuser
from ..repository import Repotransaction
from ..core.models import Transaction, UpdateTransaction

router = APIRouter(
    prefix="/transaction",
    tags=['Transaction']
)


@router.get('/',response_model=List[Transaction])
async def Search(id: Optional[str] = Query(None), tag: Optional[str] = Query(None),transaction_type: Optional[str] = Query(None), current_user: Scuser.User = Depends(OAuth2.get_current_user)):
    return await Repotransaction.Search(id, tag, transaction_type)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(transaction: Transaction = Body(...), current_user: Scuser.User = Depends(OAuth2.get_current_user)):
    return await Repotransaction.create(transaction)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id:str, current_user: Scuser.User = Depends(OAuth2.get_current_user)):
    return await Repotransaction.destroy(id)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(id:str, transaction: UpdateTransaction = Body(...), current_user: Scuser.User = Depends(OAuth2.get_current_user)):
    return await Repotransaction.update(id, transaction)


