import pytest
from src.repo.user import UserQueryRepository, UserCommandRepository
from src.schemas.user import UserCreateDB


async def test_create_user_success(db_session):
    command = UserCommandRepository(session=db_session)
    user_data = UserCreateDB(login="alena", firstname="Alena", lastname="Gaichuk")
    user = await command.create(user_data)

    assert user.id == 1
    assert user.login == "alena"
    assert user.firstname == "Alena"
    assert user.lastname == "Gaichuk"


async def test_create_user_duplicate_error(db_session, created_user):
    command = UserCommandRepository(session=db_session)
    user_data = UserCreateDB(login="alena", firstname="Dima", lastname="Uvikov")
    with pytest.raises(Exception):
        await command.create(user_data)


async def test_get_user_by_id_success(db_session, created_user):
    query = UserQueryRepository(session=db_session)
    user = await query.get_by_id(1)

    assert user.id == 1
    assert user.login == "alena"
    assert user.firstname == "Alena"
    assert user.lastname == "Gaichuk"


async def test_get_user_by_id_user_not_found(db_session):
    query = UserQueryRepository(session=db_session)
    result = await query.get_by_id(id=999)

    assert result is None


async def test_get_user_by_login_success(db_session, created_user):
    query = UserQueryRepository(session=db_session)
    result = await query.get_by_login(login="alena")

    assert result.id == 1
    assert result.login == "alena"
    assert result.firstname == "Alena"
    assert result.lastname == "Gaichuk"


async def test_get_user_by_login_not_found(db_session, created_user):
    query = UserQueryRepository(session=db_session)
    result = await query.get_by_login(login="dima")

    assert result is None
