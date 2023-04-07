from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exceotion = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not validate credentials",
        headers={"WWW-Authentical": "Bearer"}
    )

    return token.verify_token(data, credentials_exceotion)
