from pymongo import MongoClient


class BaseRepository:
    def __init__(self, client: MongoClient) -> None:
        self._client = client
    
    @property
    def client(self) -> MongoClient:
        return self._conn
