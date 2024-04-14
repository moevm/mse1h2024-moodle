from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SessionFilter(BaseModel):
    timestamp__gte: Optional[datetime] = Field(default=None)
    timestamp__lte: Optional[datetime] = Field(default=None)

    def __init__(self, start, stop):
        super().__init__()
        self.timestamp__gte = start
        self.timestamp__lte = stop
