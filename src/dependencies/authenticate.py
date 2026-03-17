from fastapi impport Depends
from fastapi.security import OAuth2PasswordBearer
from src.core.token import JWTProcessor

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/")
jwt_processor = JWTProcessor()


async def get_current_user(token: str = Depends(oauth_scheme)) -> int:
    payload = jwt_processor.decode(token)
    user_id = jwt_processor.get_field(payload, "sub")
    return int(user_id)
