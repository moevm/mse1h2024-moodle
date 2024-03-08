from pydantic import BaseModel, EmailStr
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    regular = "regular"


class User(BaseModel):
   name: str
   surname: str
   lastname: str
   email: EmailStr
   position: Role
   password: str
