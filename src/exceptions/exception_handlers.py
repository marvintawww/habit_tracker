class ItemAlreadyExist(Exception):
    """Объект уже существует"""

    pass


class ItemNotFound(Exception):
    """Объект не найден"""

    pass


class AccountDeactivated(Exception):
    """Аккаунт удален"""

    pass


class AuthenticationError(Exception):
    """Ошибка аутентификации"""

    pass


class TokenIsBlacklisted(Exception):
    """Токен находится в черном списке"""

    pass


class TokenTypeError(Exception):
    """Неверный тип токена"""

    pass
