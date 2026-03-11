from src.dependencies.user import get_user_service
from src.schemas.user import UserCreateData, UserResponse

from fastapi import APIRouter, status, Depends
