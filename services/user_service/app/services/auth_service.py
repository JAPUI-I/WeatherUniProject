from __future__ import annotations

class AuthService:
    async def login(self, *, email: str, password: str) -> tuple[str, str]:
        # TODO: implement later
        raise NotImplementedError

    async def refresh(self, *, refresh_token: str) -> tuple[str, str]:
        # TODO: implement later
        raise NotImplementedError

    async def logout(self, *, refresh_token: str) -> None:
        # TODO: implement later
        raise NotImplementedError
