from pydantic import EmailStr
from pymongo import MongoClient

from db.errors import EntityDoesNotExist
from db.repositories.base import BaseRepository
from models.domains.users import UserInDB


class UsersRepository(BaseRepository):
    def __init__(self, client: MongoClient) -> None:
        super().__init__(client)
        self._collection = self.client["sticky-todo"]["users"]

    async def get_user_by_email(self, *, email: EmailStr) -> UserInDB:
        user_row = self._collection.find_one({"email": email})
        if user_row:
            return UserInDB(**user_row)
        
        raise EntityDoesNotExist("user with email {0} does not exist".format(email))
    
    async def create_user(self, *, username: str, email: EmailStr) -> UserInDB:
        user = UserInDB(name=username, email=email, posts=[])
        self._collection.insert_one(user)

        return user.copy()