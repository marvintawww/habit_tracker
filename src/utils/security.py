from passlib.context import CryptContext


class PasswordHasher:
    def __init__(self):
        self._pwd_hasher = CryptContext(schemes=["argon2"], deprecated="auto")

    def hash_pw(self, plain_password: str) -> str:
        return self._pwd_hasher.hash(plain_password)

    def verify_pw(self, plain_password: str, hashed_paswword: str) -> bool:
        return self._pwd_hasher.verify(plain_password, hashed_paswword)
