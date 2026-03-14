from src.exceptions.exception_handlers import (
    ItemAlreadyExist,
    ItemNotFound,
    AccountDeactivated,
    AuthenticationError,
)
from src.schemas.user import UserCreateData, UserCreateDB, UserLoginData
from src.models.user import User


class UserService:
    def __init__(self, query, command, pwd_hasher):
        self._query = query
        self._command = command
        self._pwd_hasher = pwd_hasher

    async def _check_user_not_exist_by_login(self, login: str) -> None:
        user = await self._query.get_by_login(login)
        if user:
            raise ItemAlreadyExist

    async def _get_user_by_login(self, login: str) -> User:
        user = await self._query.get_by_login(login)
        if not user:
            raise ItemNotFound
        if user.is_active is False:
            raise AccountDeactivated
        return user

    async def get_user_by_id(self, id: int) -> User:
        user = await self._query.get_by_id(id)
        if not user:
            raise ItemNotFound
        elif user.is_active is False:
            raise AccountDeactivated
        return user

    async def create_user(self, data: UserCreateData) -> User:
        await self._check_user_not_exist_by_login(data.login)
        hashed_password = self._pwd_hasher.hash_pw(data.password)
        user_data = UserCreateDB(
            login=data.login,
            firstname=data.firstname,
            lastname=data.lastname,
            hashed_password=hashed_password,
        )
        return await self._command.create(user_data)

    async def authenticate(self, data: UserLoginData) -> None:
        user = await self._get_user_by_login(data.login)
        if not self._pwd_hasher.verify_pw(data.password, user.hashed_password):
            raise AuthenticationError
