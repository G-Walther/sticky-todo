from pydantic import EmailStr
from typing import Optional

from models.schemas.rwschema import RWSchema
from models.domains.users import User


class UserInLogin(RWSchema):
    email: EmailStr

class UserInCreate(UserInLogin):
    username: str

class UserInUpdate(RWSchema):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserInDelete(RWSchema):
    email: EmailStr

class UserInResponse(RWSchema):
    user: User
