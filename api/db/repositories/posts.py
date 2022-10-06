from pymongo import MongoClient
from typing import List, Optional

from db.errors import EntityDoesNotExist
from db.repositories.base import BaseRepository
from models.domains.posts import Post, PostInDB, Todo
from models.domains.users import User


class PostsRepository(BaseRepository):
    def __init__(self, client: MongoClient) -> None:
        super().__init__(client)
        self._collection = self.client["sticky-todo"]["posts"]

    async def get_posts_for_user(self, *, user: User) -> List[Post]:
        posts = await self._collection.find({"_id":{"$id": user.posts}})
        if posts:
            return [Post(**post) for post in posts]
        
        raise EntityDoesNotExist("user with email {0} does not have any post".format(user.email))
    
    async def create_post(self, *, user: User) -> Post:
        post = PostInDB(todos=[])
        result = await self._collection.insert_one(post)
        post._id = result.inserted_id
        
        self._client["sticky-todo"]["users"].update_one({"_id": user._id}, {"$push": {"posts": result.inserted_id}})

        return post.copy()
    
    async def update_post(
        self,
        *,
        _id: str,
        todos: Optional[List[Todo]]
    ) -> None:
        result = await self._collection.update_one({"_id": _id}, {"todos": todos})
        return

    async def delete_post(self, *, post: Post) -> None:
        result = await self._collection.delete_one({"_id": post._id})
        return
