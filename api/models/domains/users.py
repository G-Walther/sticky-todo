from typing import List, Optional

from models.domains.rwmodel import RWModel


class User(RWModel):
    _id: Optional[str]
    name: str
    email: str
    posts: List[str]

class UserInDB(User):
    pass
