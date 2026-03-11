from src.exceptions.exception_handlers import ItemAlreadyExist
from src.schemas.user import UserCreateData, UserCreateDB
from src.models.user import User


class UserService:
    def __init__(self, query, command):
        self._query = query
        self._command = command

    async def _check_user_not_exist_by_login(self, login: str) -> None:
        user = await self._query.get_by_login(login)
        if user:
            raise ItemAlreadyExist

    async def create_user(self, data: UserCreateData) -> User:
        await self._check_user_not_exist_by_login(data.login)
        user_data = UserCreateDB(
            login=data.login, firstname=data.firstname, lastname=data.lastname
        )
        return await self._command.create(user_data)
