from fastapi import Depends, APIRouter, status

from src.dependencies.user import get_user_service
from src.dependencies.jwt import get_jwt_service
from src.services.user import UserService
from src.services.jwt import JWTService
from src.schemas.jwt import TokenPairResponse
from src.schemas.user import UserCreateData, UserLoginData

router = APIRouter()


@router.post(
    "/register",
    response_model=TokenPairResponse,
    status_code=status.HTTP_200_OK,
    summary="Создание пользователя",
)
async def register(
    data: UserCreateData,
    user_service: UserService = Depends(get_user_service),
    jwt_service: JWTService = Depends(get_jwt_service),
) -> TokenPairResponse:
    user = await user_service.create_user(data)
    return jwt_service.create_token_pair(user.id)


@router.post(
    "/login",
    response_model=TokenPairResponse,
    status_code=status.HTTP_200_OK,
    summary="Вход в аккаунт",
)
async def login(
    data: UserLoginData,
    user_service: UserService = Depends(get_user_service),
    jwt_service: JWTService = Depends(get_jwt_service),
) -> TokenPairResponse:
    user = await user_service.authenticate(data)
    return jwt_service.create_token_pair(user.id)
