import pytest
from unittest.mock import MagicMock

from src.schemas.user import UserCreateDB
from src.exceptions.exception_handlers import (
    ItemAlreadyExist,
    ItemNotFound,
    AccountDeactivated,
)


async def test_create_user_service_success(user_service):
    user_service._query.get_by_login.return_value = None
    user_service._command.create.return_value = MagicMock(id=1, login="dima")
    result = await user_service.create_user(
        UserCreateDB(login="dima", firstname="a", lastname="b")
    )

    assert result.id == 1
    assert result.login == "dima"
    user_service._command.create.assert_called_once()


async def test_create_user_service_duplicate_error(user_service):
    user_service._query.get_by_login.return_value = MagicMock(id=1, login="alena")

    with pytest.raises(ItemAlreadyExist):
        await user_service.create_user(
            UserCreateDB(login="alena", firstname="Alena", lastname="Gaichuk")
        )

    user_service._command.create.assert_not_called()


async def test_get_user_by_id_success(user_service):
    user_service._query.get_by_id.return_value = MagicMock(
        id=1, login="dima", is_active=True
    )
    result = await user_service.get_user_by_id(1)

    assert result.id == 1
    assert result.login == "dima"
    assert result.is_active is True


async def test_get_user_by_id_not_found(user_service):
    user_service._query.get_by_id.return_value = None
    with pytest.raises(ItemNotFound):
        await user_service.get_user_by_id(1)


async def test_get_user_by_id_inactive(user_service):
    user_service._query.get_by_id.return_value = MagicMock(
        id=1, login="alena", is_active=False
    )
    with pytest.raises(AccountDeactivated):
        await user_service.get_user_by_id(1)
