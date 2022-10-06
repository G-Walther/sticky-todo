from pydantic import HttpUrl
from typing import List, Optional

from models.domains.rwmodel import RWModel


class Todo(RWModel):
    content: str
    checked: bool
    image: Optional[HttpUrl] = None

class Post(RWModel):
    _id: Optional[str]
    todos: List[Todo]

class PostInDB(Post):
    pass
