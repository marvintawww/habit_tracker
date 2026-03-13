import pytest
from unittest.mock import AsyncMock, MagicMock
from src.services.user import UserService
from src.services.jwt import JWTService


@pytest.fixture
def user_service():
    query = AsyncMock()
    command = AsyncMock()
    pwd_hasher = MagicMock()
    pwd_hasher.hash_pw.return_value = "fake_hash"
    return UserService(query=query, command=command, pwd_hasher=pwd_hasher)


@pytest.fixture
def jwt_service():
    query = AsyncMock()
    command = AsyncMock()
    jwt_processor = MagicMock()
    return JWTService(query=query, command=command, jwt_processor=jwt_processor)
