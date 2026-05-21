# 3_response.py
from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    created_at: str   # ISO 8601 string
