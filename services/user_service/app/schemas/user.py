from __future__ import annotations

from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    display_name: str | None = None

class UserPublic(BaseModel):
    id: UUID
    email: EmailStr
    display_name: str | None = None
