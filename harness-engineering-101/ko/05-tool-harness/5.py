"""Generated from book-content article."""

from pydantic import BaseModel, Field
from typing import Literal

# Bad — too many responsibilities
def manage_user(action: str, user_id: str, **kwargs):
    """Manage a user."""
    ...

# Good — single responsibility, explicit schema
class CreateUserInput(BaseModel):
    email: str = Field(..., description="A valid email address")
    name: str = Field(..., min_length=1, max_length=100)
    role: Literal["admin", "user", "guest"]

class CreateUserOutput(BaseModel):
    user_id: str
    created_at: str
    status: Literal["created", "already_exists"]

def create_user(input: CreateUserInput) -> CreateUserOutput:
    """Create a new user. Returns already_exists if the email already exists."""
    ...
