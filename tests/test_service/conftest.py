import pytest
from unittest.mock import AsyncMock
from src.services.user import UserService


@pytest.fixture
def user_service():
    query = AsyncMock()
    command = AsyncMock()
    return UserService(query=query, command=command)
