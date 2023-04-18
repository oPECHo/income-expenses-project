from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BaseModel):

    id : PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username : str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)
    def hash_password(self):
        self.password = pwd_context.hash(self.password)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "string",
                "email": "user@gmail.com",
                "password": "string"
            }
        }    

class Transaction(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    date: str = Field(...)
    body: str = Field(...)
    amount: float = Field(...)
    tag: str = Field(...)
    transaction_type: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "date": "2023-04-18",
                "body": "string",
                "amount": "0.0",
                "tag": "string",
                "transaction_type": "string"
            }
        }    
        
class UpdateTransaction(BaseModel):
    date: Optional[str]
    body: Optional[str]
    amount: Optional[float]
    tag: Optional[str]
    transaction_type: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "date": "2023-04-18",
                "body": "string",
                "amount": "0.0",
                "tag": "string",
                "transaction_type": "string"
            }
        }
