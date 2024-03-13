import uuid
from pydantic import BaseModel, EmailStr, HttpUrl, Field
import datetime
from typing import List, Optional
from enum import Enum


class ElementTypeEnum(str, Enum):
    button = "button"

    def __str__(self):
        return self.value


class ActionTypeEnum(str, Enum):
    conversation = "conversation"

    def __str__(self):
        return self.value


class EventTypeEnum(str, Enum):
    mousedown = "mousedown"

    def __str__(self):
        return self.value


class Payload(BaseModel):
    date: str = Field(default_factory=lambda: str(datetime.date.today()))
    time: str = Field(default_factory=lambda: str(datetime.datetime.now().time()))
    page: HttpUrl = Field(...)
    element_type: ElementTypeEnum = Field(...)
    element_name: str = Field(...)
    action_type: ActionTypeEnum = Field(...)
    event_type: EventTypeEnum = Field(...)

    class Config:
        populate_by_field_name = True
        json_schema_extra = {
            "example": {
                "date": str(datetime.date.today()),
                "time": str(datetime.datetime.now().time()),
                "page": "https://example.com",
                "element_type": "button",
                "element_name": "отправить",
                "action_type": "conversation",
                "event_type": "mousedown"
            }
        }


class SessionData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    student: str = Field(...)
    group: int = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    session: str = Field(...)
    actions: List[Payload] = Field(default_factory=list)

    class Config:
        populate_by_field_name = True
        json_schema_extra = {
            "example": {
                "id": str(uuid.uuid4()),
                "student": "Иванов Иван",
                "group": 1303,
                "email": "iiivanov@edu.ru",
                "course": "Курс молодого бойца",
                "session": "sessionId",
                "actions": [{
                    "date": "2024-02-02",
                    "time": "14:00:00",
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown"
                }]
            }
        }


class CreateSessionData(BaseModel):
    student: str = Field(...)
    group: int = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    session: str = Field(...)
    actions: List[Payload] = Field(default_factory=list)

    class Config:
        populate_by_field_name = True
        json_schema_extra = {
            "example": {
                "student": "Иванов Иван",
                "group": 1303,
                "email": "iiivanov@edu.ru",
                "course": "Курс молодого бойца",
                "session": "sessionId",
                "actions": [{
                    "date": "2024-02-02",
                    "time": "14:00:00",
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown"
                }]
            }
        }
