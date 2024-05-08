import uuid
from pydantic import BaseModel, EmailStr, HttpUrl, Field
from datetime import datetime
from typing import List

class Payload(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now().isoformat())
    page: HttpUrl = Field(...)
    element_type: str = Field(...)
    element_name: str = Field(...)
    action_type: str = Field(...)
    event_type: str = Field(...)
    element_html: str = Field(..., description="The HTML content of the element")

    class Config:
        populate_by_field_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "examples": [
                {
                    "timestamp": datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "button",
                    "element_name": "отправить",
                    "action_type": "conversation",
                    "event_type": "mousedown",
                    "element_html": "<input/>"
                },
                {
                    "timestamp": datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "page",
                    "element_name": "сохранить",
                    "action_type": "hidden",
                    "event_type": "visibilitychange",
                    "element_html": "<input/>"
                },
                {
                    "timestamp": datetime.now().isoformat(),
                    "page": "https://example.com",
                    "element_type": "page",
                    "element_name": "сохранить",
                    "action_type": "visible",
                    "event_type": "visibilitychange", 
                    "element_html": "<input/>"
                }
            ]
        }


class SessionData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    student_id: int = Field(...)
    student: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
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
                "actions": [{
                    "timestamp": datetime.now().isoformat(),
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown", 
                    "element_html": "<input/>"
                }]
            },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "actions": [{
                        "timestamp": datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "button",
                        "element_name": "сохранить",
                        "action_type": "hidden",
                        "event_type": "visibilitychange", 
                        "element_html": "<input/>"
                    }]
                },
                {
                    "id": str(uuid.uuid4()),
                    "student": "Иванов Иван",
                    "student_id": 1,
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "actions": [{
                        "timestamp": datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "visible",
                        "event_type": "visibilitychange", 
                        "element_html": "<input/>"
                    }]
                    
                }]
        }


class CreateSessionData(BaseModel):
    student_id: int = Field(...)
    student: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
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
                "actions": [{
                    "timestamp": datetime.now().isoformat(),
                    "page": "http://e.moevm.info/some_course",
                    "element_type": "button",
                    "element_name": "сохранить",
                    "action_type": "conversation",
                    "event_type": "mousedown", 
                    "element_html": "<input/>"
                }]
            },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "actions": [{
                        "timestamp": datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "hidden",
                        "event_type": "visibilitychange", 
                        "element_html": "<input/>"
                    }]
                },
                {
                    "id": str(uuid.uuid4()),
                    "student_id": 1,
                    "student": "Иванов Иван",
                    "email": "iiivanov@edu.ru",
                    "course": "Курс молодого бойца",
                    "actions": [{
                        "timestamp": datetime.now().isoformat(),
                        "page": "http://e.moevm.info/some_course",
                        "element_type": "page",
                        "element_name": "сохранить",
                        "action_type": "visible",
                        "event_type": "visibilitychange", 
                        "element_html": "<input/>"
                    }]
                }]
        }
