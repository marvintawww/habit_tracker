class ItemAlreadyExist(Exception):
    """Объект уже существует"""

    pass


class ItemNotFound(Exception):
    """Объект не найден"""

    pass


class AccountDeactivated(Exception):
    """Аккаунт удален"""

    pass
