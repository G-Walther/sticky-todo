from fastapi import APIRouter, Body, Depends, status
from api.dependencies.database import get_repository
from db.repositories.posts import PostsRepository

from models.domains.posts import Post
from models.domains.users import User
from models.schemas.posts import (
    ListOfPostsInResponse,
    PostInCreate,
    PostInUpdate,
    PostInDelete,
    PostInResponse)


router = APIRouter()

@router.get(
    "",
    response_model=PostInResponse,
    name="post:list-posts")
def list_posts_for_user(
    user: User,
    posts_repo: PostsRepository = Depends(get_repository(PostsRepository))
) -> ListOfPostsInResponse:
    return

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PostInResponse,
    name="post:create-post")
def create_post(
    post_create: PostInCreate = Body(..., embed=True, alias="posts"),
    posts_repo: PostsRepository = Depends(get_repository(PostsRepository))
) -> None:
    return

@router.put(
    "",
    response_model=PostInResponse,
    name="post:update-post")
def update_post(
    post: Post,
    post_update: PostInUpdate = Body(..., embed=True, alias="posts"),
    posts_repo: PostsRepository = Depends(get_repository(PostsRepository))
) -> None:
    return

@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    name="posts:delete-post")
def delete_post(
    post_delete: PostInDelete = Body(..., embed=True, alias="posts"),
    posts_repo: PostsRepository = Depends(get_repository(PostsRepository))
) -> None:
    return
