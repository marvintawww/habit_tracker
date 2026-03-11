from src.repo.base import BaseQueryRepository, BaseCommandRepository
from src.schemas.jwt import BlacklistedTokenDB
from src.models.jwt import JWTBlacklist

from sqlalchemy import select


class JWTQueryRepository(BaseQueryRepository[JWTBlacklist]):
    def __init__(self, session):
        super().__init__(session, JWTBlacklist)

    async def get_by_jti(self, jti: str) -> JWTBlacklist | None:
        stmt = select(JWTBlacklist).where(JWTBlacklist.jti == jti)
        token = await self._session.execute(stmt)
        return token.scalar_one_or_none()


class JWTCommandRepository(BaseCommandRepository[JWTBlacklist, BlacklistedTokenDB]):
    def __init__(self, session):
        super().__init__(session, JWTBlacklist)
