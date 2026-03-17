from src.dependencies.user import get_user_service
from src.dependencies.authenticate import get_current_user
from src.schemas.user import UserCreateData, UserResponse
from src.services.user import UserService

from fastapi import APIRouter, status, Depends

router = APIRouter()


@router.get(
    "/profile",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Профиль пользователя"
)
async def profile(
    user_service: UserService = Depends(get_user_service), 
    user_id: int = Depends(get_current_user)
) -> UserResponse:
    return await user_service.get_user_by_id(user_id)
