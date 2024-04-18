import uuid
from pydantic import BaseModel, EmailStr, HttpUrl, Field
import datetime
from typing import List
from enum import Enum


class ElementTypeEnum(str, Enum):
    button = "button"
    page = "page"

    def __str__(self):
        return self.value


class ActionTypeEnum(str, Enum):
    conversation = "conversation"
    visible = "visible"
    hidden = "hidden"

    def __str__(self):
        return self.value


class EventTypeEnum(str, Enum):
    mousedown = "mousedown"
    visibilitychange = "visibilitychange"

    def __str__(self):
        return self.value


class Payload(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.datetime.now().isoformat())
    page: HttpUrl = Field(...)
    element_type: ElementTypeEnum = Field(...)
    element_name: str = Field(...)
    action_type: ActionTypeEnum = Field(...)
    event_type: EventTypeEnum = Field(...)

    class Config:
        populate_by_field_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "examples": [
                {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "button",
                    "element_name": "отправить",
                    "action_type": "conversation",
                    "event_type": "mousedown"
                },
                {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "page",
                    "element_name": "сохранить",
                    "action_type": "hidden",
                    "event_type": "visibilitychange"},
                {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "page",
                    "element_name": "сохранить",
                    "action_type": "visible",
                    "event_type": "visibilitychange"
                }
            ]
        }


class SessionData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    student_id: int = Field(...)
    student: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    session: str = Field(...)
    actions: List[Payload] = Field(default_factory=list)

    class Config:
        populate_by_field_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "examples": [{
                "id": str(uuid.uuid4()),
                "student_id": 1,
                "student": "Иванов Иван",
                "email": "iiivanov@edu.ru",
                "course": "Курс молодого бойца",
                "session": "sessionId",
                "actions": [{
                    "timestamp": datetime.datetime.now().isoformat(),
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown"
                }]
            },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "session": "sessionId",
                    "actions": [{
                        "timestamp": datetime.datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "button",
                        "element_name": "сохранить",
                        "action_type": "hidden",
                        "event_type": "visibilitychange"
                    }]
                },
                {
                    "id": str(uuid.uuid4()),
                    "student": "Иванов Иван",
                    "student_id": 1,
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "session": "sessionId",
                    "actions": [{
                        "timestamp": datetime.datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "visible",
                        "event_type": "visibilitychange"
                    }]
                }]
        }


class CreateSessionData(BaseModel):
    student_id: int = Field(...)
    student: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    session: str = Field(...)
    actions: List[Payload] = Field(default_factory=list)

    class Config:
        populate_by_field_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "examples": [{
                "id": str(uuid.uuid4()),
                "student_id": 1,
                "student": "Иванов Иван",
                "email": "iiivanov@edu.ru",
                "course": "Курс молодого бойца",
                "session": "sessionId",
                "actions": [{
                    "timestamp": datetime.datetime.now().isoformat(),
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown"
                }]
            },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "session": "sessionId",
                    "actions": [{
                        "timestamp": datetime.datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "hidden",
                        "event_type": "visibilitychange"
                    }]
                },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "session": "sessionId",
                    "actions": [{
                        "timestamp": datetime.datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "visible",
                        "event_type": "visibilitychange"
                    }]
                }]
        }
