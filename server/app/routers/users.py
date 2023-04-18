from fastapi import APIRouter, Body
from ..repository import Repousers
from ..core.models import User

router = APIRouter(
    tags=['Register']
)

@router.post('/register',response_model=User)
async def create_user(user: User = Body(...)):
    return await Repousers.create(user)
