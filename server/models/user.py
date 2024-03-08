from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    regular = "regular"


class User(BaseModel):
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
