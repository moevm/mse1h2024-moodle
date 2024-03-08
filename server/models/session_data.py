from pydantic import BaseModel, EmailStr, HttpUrl, Field
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
    date: date = Field(default_factory=date.today)
    time: time = Field(default_factory=time)
    page: HttpUrl = Field(...)
    element_type: ElementType = Field(...)
    element_name: str = Field(...)
    action_type: ActionType = Field(...)
    event: ElementType = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "date": date.today(),
                "time": time,
                "page": "https://example.com",
                "element_type": ElementType.button,
                "element_name": "отправить",
                "action_type": ActionType.conversation,
                "event": EventType.mousedown
            }
        }


class SessionData(BaseModel):
    student: str = Field(...)
    group: int = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    session: str = Field(...)
    actions: List[Payload] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "student": "Иванов Иван",
                "group": 1303,
                "email": "iiivanov@edu.ru",
                "course": "Курс молодого бойца",
                "session": "sessionId",
                "actions": []
            }
        }
