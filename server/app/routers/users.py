from fastapi import APIRouter, Depends

from ..core import database
from ..schemas import Scuser
from sqlalchemy.orm import Session
from ..repository import Repousers

router = APIRouter(
    tags=['Register']
)

get_db = database.get_db

@router.post('/register',response_model=Scuser.ShowUser)
async def create_user(request: Scuser.User, db: Session = Depends(get_db)):
    return Repousers.create_user(request, db)
