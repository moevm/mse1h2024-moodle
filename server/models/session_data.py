from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import date, time
from typing import List
from enum import Enum

class ElementType(str, Enum):
    button = "button"


class ActionType(str, Enum):
    conversation = "conversation"


class EventType(str, Enum):
    mousedown = "mousedown"


class Payload(BaseModel):
    date: date
    time: time
    page: HttpUrl
    element_type: ElementType
    element_name: str
    action_type: ActionType
    event: ElementType


class SessionData(BaseModel):
    student: str
    group: int
    email: EmailStr
    course: str
    session: str
    actions: List[Payload]