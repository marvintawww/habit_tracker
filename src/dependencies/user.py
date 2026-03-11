from src.services.user import UserService
from src.repo.user import UserQueryRepository, UserCommandRepository
from src.database.db import db

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_service(
    session: AsyncSession = Depends(db.get_session),
) -> UserService:
    return UserService(
        query=UserQueryRepository(session), command=UserCommandRepository(session)
    )
