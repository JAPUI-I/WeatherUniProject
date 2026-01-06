from __future__ import annotations

from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str

class TokenPair(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str
    refresh_token_expires_in: int