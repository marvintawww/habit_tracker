from src.schemas.jwt import TokenPairResponse, BlacklistedTokenDB, RefreshTokenRequest
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from src.exceptions.exception_handlers import TokenIsBlacklisted

from uuid import uuid4
from datetime import datetime, timezone, timedelta


class JWTService:
    def __init__(self, query, command, jwt_processor):
        self._query = query
        self._command = command
        self._jwt_processor = jwt_processor

    def _create_access_token(self, user_id: int) -> str:
        payload = {
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
            "jti": str(uuid4()),
            "type": "access",
        }
        return self._jwt_processor.encode(payload)

    def _create_refresh_token(self, user_id: int) -> str:
        payload = {
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc)
            + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
            "jti": str(uuid4()),
            "type": "refresh",
        }
        return self._jwt_processor.encode(payload)

    async def _check_token_not_in_blacklist(self, jti: str):
        token = await self._query.get_by_jti(jti)
        if token:
            raise TokenIsBlacklisted

    async def _add_token_to_blacklist(self, token: str) -> None:
        payload = self._jwt_processor.decode(token)
        self._jwt_processor.check_token_type(payload, "refresh")
        jti = self._jwt_processor.get_field(payload, "jti")
        await self._check_token_not_in_blacklist(jti)
        await self._command.create(BlacklistedTokenDB(jti=jti))

    def create_token_pair(self, user_id: int) -> TokenPairResponse:
        return TokenPairResponse(
            access_token=self._create_access_token(user_id),
            refresh_token=self._create_refresh_token(user_id),
        )

    async def refresh_token_pair(self, data: RefreshTokenRequest) -> TokenPairResponse:
        payload = self._jwt_processor.decode(data.refresh_token)
        await self._add_token_to_blacklist(data.refresh_token)
        user_id = int(self._jwt_processor.get_field(payload, "sub"))
        return await self.create_token_pair(user_id)

    async def logout(self, data: RefreshTokenRequest) -> None:
        await self._add_token_to_blacklist(data.refresh_token)
