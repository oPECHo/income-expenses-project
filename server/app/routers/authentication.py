from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..core.database import db
from ..utils import token
from ..utils.hashing import Hash

router = APIRouter(
    tags=['Login']
)

@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"email": request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Credentials')

    if not Hash.verify(user["password"], request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')

    access_token = token.create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
