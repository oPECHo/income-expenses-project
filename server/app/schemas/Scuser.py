from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
