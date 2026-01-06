from __future__ import annotations

from fastapi import FastAPI


from .api.users import router as users_router
from .api.auth import router as auth_router

app = FastAPI(title="User Service")

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}


def create_app() -> FastAPI:
    app = FastAPI(title="User Service")
    app.include_router(users_router)
    app.include_router(auth_router)
    return app

app = create_app()
