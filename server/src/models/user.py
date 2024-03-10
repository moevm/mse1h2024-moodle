from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    regular = "regular"


class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str = Field(...)
    surname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    position: Role = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Иван",
                "surname": "Иванов",
                "lastname": "Иванович",
                "email": "iiivanov@edu.ru",
                "position": Role.regular,
                "password": "sdfsdfwgesdgcx"
            }
        }


class UpdateUser(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    lastname: Optional[str]
    email: Optional[EmailStr]
    position: Optional[Role]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Иван",
                "surname": "Иванов",
                "lastname": "Иванович",
                "email": "iiivanov@edu.ru",
                "position": Role.regular,
                "password": "sdfsdfwgesdgcx"
            }
        }