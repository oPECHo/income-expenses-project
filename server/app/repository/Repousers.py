from ..utils.hashing import Hash
from fastapi.encoders import jsonable_encoder
from ..core.database import db
from ..core.models import User
from fastapi import Body, status
from fastapi.responses import JSONResponse

async def create(user: User = Body(...)):
    user.password = Hash.bcrypt(user.password)
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)