from typing import Optional, Iterator, Any

import backoff
import pandas as pd
from loguru import logger
from clickhouse_driver import Client as Clickhouse

from src.core.config import BACKOFF_CONFIG
from src.load.base import BaseLoader


def ch_conn_is_alive(ch_conn: Clickhouse) -> bool:
    """Функция для проверки работоспособности Clickhouse"""
    try:
        return ch_conn.execute("SHOW DATABASES")
    except Exception:
        return False


class ClickhouseLoader(BaseLoader):
    def __init__(
        self,
        host: str,
        port: int,
        user: str = "default",
        password: str = "",
        alt_hosts: Optional[list[str]] = None,
        conn: Optional[Clickhouse] = None,
        settings: Optional[dict[str, Any]] = None,
    ) -> None:
        self._conn: Clickhouse = conn
        self._host: str = host
        self._alt_hosts: Optional[list[str]] = alt_hosts
        self._port: int = port
        self._user: str = user
        self._password: str = password
        self._settings: Optional[dict[str, Any]] = settings

    @property
    def conn(self) -> Clickhouse:
        if self._conn is None or not ch_conn_is_alive(self._conn):
            self._conn = self._reconnection()

        return self._conn

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def _reconnection(self) -> Clickhouse:
        logger.info('Reconnection clickhouse node "%s:%d" ...', self._host, self._port)

        if self._conn is not None:
            logger.info("Closing already exists clickhouse connector...")
            self._conn.disconnect()

        return Clickhouse(
            host=self._host,
            port=self._port,
            user=self._user,
            alt_hosts=",".join(self._alt_hosts),
            password=self._password,
            settings=self._settings,
        )

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def load(self, data: Iterator[type], table: str) -> int | None:

        return self.conn.execute(
            f"INSERT INTO {table} VALUES ", (_.model_dump() for _ in data)
        )
