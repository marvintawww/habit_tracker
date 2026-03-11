import pytest

from src.repo.jwt import JWTQueryRepository, JWTCommandRepository
from src.schemas.jwt import BlacklistedTokenDB


async def test_create_blacklist_item_success(db_session):
    command = JWTCommandRepository(session=db_session)
    token_data = BlacklistedTokenDB(jti="jti")
    token = await command.create(token_data)

    assert token.id == 1
    assert token.jti == "jti"


async def test_create_blacklist_item_duplicate_error(db_session, blacklisted_token):
    command = JWTCommandRepository(session=db_session)
    token_data = BlacklistedTokenDB(jti="jti")
    with pytest.raises(Exception):
        await command.create(token_data)


async def test_get_blacklisted_token_by_jti_success(db_session, blacklisted_token):
    query = JWTQueryRepository(session=db_session)
    token = await query.get_by_jti(jti="jti")

    assert token.id == 1
    assert token.jti == "jti"


async def test_get_blacklisted_token_by_jti_not_found(db_session):
    query = JWTQueryRepository(session=db_session)
    result = await query.get_by_jti(jti="jopa")

    assert result is None
