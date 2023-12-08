from abc import ABC, abstractmethod
from typing import Iterator


class BaseClient(ABC):
    @property
    @abstractmethod
    def conn(self):
        '''Клиент БД'''


class BaseLoader(ABC):
    @abstractmethod
    def load(self, data: Iterator[type]):
        raise NotImplementedError
