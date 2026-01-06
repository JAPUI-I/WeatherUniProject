from __future__ import annotations

from fastapi import APIRouter, Depends, status

from ..api.deps import CurrentUserIdDep, user_service
from ..schemas.user import UserCreate, UserPublic
from ..services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(payload: UserCreate, svc: UserService = Depends(user_service)) -> dict:
    user_id = await svc.signup(
        email=payload.email,
        password=payload.password,
        display_name=payload.display_name,
    )
    return {"user_id": str(user_id)}

@router.get("/me", response_model=UserPublic)
async def me(user_id: CurrentUserIdDep, svc: UserService = Depends(user_service)) -> UserPublic:
    data = await svc.get_me(user_id=user_id)
    return UserPublic.model_validate(data)
