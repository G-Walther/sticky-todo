from pydantic import HttpUrl
from typing import List, Optional

from models.domains.posts import Post, Todo
from models.schemas.rwschema import RWSchema


class PostInCreate(RWSchema):
    todos: List[Todo] = []

class PostInUpdate(RWSchema):
    content: Optional[str] = None
    checked: Optional[bool] = None
    image: Optional[HttpUrl] = None

class PostInDelete(RWSchema):
    _id: str

class PostInResponse(Post):
    pass

class ListOfPostsInResponse(RWSchema):
    posts: List[Post]
