from __future__ import annotations

from uuid import UUID

class UserService:
    async def signup(self, *, email: str, password: str, display_name: str | None) -> UUID:
        # TODO: 
        raise NotImplementedError

    async def get_me(self, *, user_id: UUID) -> dict:
        # TODO: 
        raise NotImplementedError
