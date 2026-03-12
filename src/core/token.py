from abc import ABC, abstractmethod
from jose import jwt, JWTError

from src.config import SECRET_KEY
from src.exceptions.exception_handlers import ItemNotFound, TokenTypeError


class TokenProcessor(ABC):
    @abstractmethod
    def encode(self, payload: dict) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> dict:
        pass


class JWTProcessor(TokenProcessor):
    def encode(self, payload: dict) -> str:
        try:
            return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        except JWTError:
            raise

    def decode(self, token: str) -> dict:
        try:
            return jwt.decode(token, SECRET_KEY, algorithm="HS256")
        except JWTError:
            raise

    def get_field(self, payload: dict, target: str):
        field = payload.get(target)
        if field is None:
            raise ItemNotFound
        return field

    def check_token_type(self, payload: dict, target: str) -> None:
        token_type = payload.get("type")
        if token_type != target:
            raise TokenTypeError
