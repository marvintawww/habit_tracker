import pytest_asyncio

from src.models.user import User
from src.repo.user import UserCommandRepository
from src.schemas.user import UserCreateDB


@pytest_asyncio.fixture
async def created_user(db_session):
    command = UserCommandRepository(session=db_session)
    user_data = UserCreateDB(login="alena", firstname="Alena", lastname="Gaichuk")
    return await command.create(user_data)
