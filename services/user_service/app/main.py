from fastapi import FastAPI
from app.api import users, auth

app = FastAPI(title="User Service", version="1.0.0")

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
