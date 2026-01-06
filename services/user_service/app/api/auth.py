from __future__ import annotations

from fastapi import APIRouter, Depends, status

from ..api.deps import auth_service
from ..schemas.auth import LoginRequest, RefreshRequest, TokenPair
from ..services.auth_service import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/login", response_model=TokenPair)
async def login(payload: LoginRequest, svc: AuthService = Depends(auth_service)) -> TokenPair:
    access, refresh = await svc.login(email=payload.email, password=payload.password)
    return TokenPair(access_token=access, refresh_token=refresh)

@router.post("/refresh", response_model=TokenPair)
async def refresh(payload: RefreshRequest, svc: AuthService = Depends(auth_service)) -> TokenPair:
    access, refresh = await svc.refresh(refresh_token=payload.refresh_token)
    return TokenPair(access_token=access, refresh_token=refresh)

@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(payload: RefreshRequest, svc: AuthService = Depends(auth_service)) -> dict:
    await svc.logout(refresh_token=payload.refresh_token)
    return {"detail": "logged out"}

