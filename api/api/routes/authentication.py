from fastapi import APIRouter, Body, Depends, status

from api.dependencies.database import get_repository
from db.repositories.users import UsersRepository
from models.schemas.users import (
    UserInCreate,
    UserInLogin,
    UserInResponse)


router = APIRouter()

@router.post(
    "/login",
    response_model=UserInResponse,
    name="auth:login")
async def login(
    user_login: UserInLogin = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserInResponse:
    return

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserInResponse,
    name="auth:register")
async def register(
    user_create: UserInCreate = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserInResponse:
    return 
