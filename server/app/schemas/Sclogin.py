from typing import Optional
from pydantic import BaseModel

class Login(BaseModel):
    Email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None