from fastapi import APIRouter, Body, Depends

from api.dependencies.database import get_repository
from db.repositories.users import UsersRepository
from models.schemas.users import (
    UserInDelete,
    UserInResponse,
    UserInUpdate)


router = APIRouter()

@router.put(
    "",
    response_model=UserInResponse,
    name="users:update-user")
def update_user(
    user_update: UserInUpdate = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserInResponse:
    return

@router.delete(
    "",
    response_model=UserInResponse,
    name="users:delete-user")
def delete_user(
    user_delete: UserInDelete = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserInResponse:
    return