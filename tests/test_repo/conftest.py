import pytest_asyncio

from src.models.user import User
from src.models.jwt import JWTBlacklist
from src.repo.user import UserCommandRepository
from src.repo.jwt import JWTCommandRepository
from src.schemas.user import UserCreateDB
from src.schemas.jwt import BlacklistedTokenDB


@pytest_asyncio.fixture
async def created_user(db_session):
    command = UserCommandRepository(session=db_session)
    user_data = UserCreateDB(login="alena", firstname="Alena", lastname="Gaichuk")
    return await command.create(user_data)


@pytest_asyncio.fixture
async def blacklisted_token(db_session):
    command = JWTCommandRepository(session=db_session)
    token_data = BlacklistedTokenDB(jti="jti")
    return await command.create(token_data)
