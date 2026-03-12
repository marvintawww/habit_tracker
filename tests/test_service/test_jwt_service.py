import pytest
from unittest.mock import MagicMock

from src.schemas.jwt import BlacklistedTokenDB
from src.exceptions.exception_handlers import TokenIsBlacklisted


async def test_create_token_pair_success(jwt_service):
    jwt_service._jwt_processor.encode.side_effect = ["access", "refresh"]
    result = jwt_service.create_token_pair(user_id=1)

    assert result.access_token == "access"
    assert result.refresh_token == "refresh"
    assert jwt_service._jwt_processor.encode.call_count == 2


async def test_check_token_not_in_blacklist_success(jwt_service):
    jwt_service._query.get_by_jti.return_value = None
    result = await jwt_service._check_token_not_in_blacklist(jti="jti")

    assert result is None
