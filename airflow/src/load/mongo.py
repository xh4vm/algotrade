import backoff
from motor.motor_asyncio import AsyncIOMotorClient
from load.base import BaseLoader, BaseClient
from loguru import logger
from core.config import DBSettings, BACKOFF_CONFIG
from typing import Iterator, Any


class AsyncMongoClient(BaseClient):
    def __init__(self, settings: DBSettings):
        self._settings: DBSettings = settings
        self._conn = None

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def _reconnection(self) -> AsyncIOMotorClient:
        if self._conn is not None:
            self._conn.close()

        return AsyncIOMotorClient(
            f'{self._settings.DRIVER}://{self._settings.HOST}:{self._settings.PORT}',
            uuidRepresentation='standard'
        )

    @property
    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def conn(self) -> AsyncIOMotorClient:
        if self._conn is None:
            return self._reconnection()

        return self._conn

    @conn.setter
    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def conn(self, value: AsyncIOMotorClient) -> None:
        self.conn = value


class AsyncMongoLoader(BaseLoader):
    def __init__(self, client: BaseClient):
        self.client: BaseClient = client

    async def load(
        self,
        db_name: str,
        collection_name: str,
        data: Iterator[type]
    ) -> list[Any]:
        cursor = self.client.conn[db_name][collection_name]
        result = await cursor.insert_many(data)
        return result.inserted_ids
