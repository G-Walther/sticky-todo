from fastapi import Depends
from pymongo import MongoClient
from typing import Callable, Type

from db.repositories.base import BaseRepository


def _get_db_client() -> MongoClient:
    yield MongoClient()

def get_repository(
    repo_type: Type[BaseRepository]
) -> Callable[[MongoClient], BaseRepository]:
    def _get_repo(
        client: MongoClient = Depends(_get_db_client)
    ) -> BaseRepository:
        return repo_type(client)

    return  _get_repo
