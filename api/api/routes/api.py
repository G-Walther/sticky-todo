from fastapi import APIRouter

from api.routes import authentication, users, posts


router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/auth")
router.include_router(users.router, tags=["users"], prefix="/users")
router.include_router(posts.router, tags=["posts"], prefix="/posts")
