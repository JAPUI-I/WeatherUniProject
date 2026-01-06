from __future__ import annotations

from typing import Annotated
from uuid import UUID, uuid4

from fastapi import Depends

from ..services.user_service import UserService
from ..services.auth_service import AuthService

async def get_current_user_id() -> UUID:
    """
    Mock dependency.
    Replace with JWT decoding later.
    """
    return uuid4()

CurrentUserIdDep = Annotated[UUID, Depends(get_current_user_id)]

def user_service() -> UserService:
    # NOTE: Later you will inject repositories here
    return UserService()

def auth_service() -> AuthService:
    # NOTE: Later you will inject repos + redis here
    return AuthService()
