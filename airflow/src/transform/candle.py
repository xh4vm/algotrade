from typing import Any, Iterator

from src.transform.base import BaseTransformer
from src.models.candle import CandleModel


class CandleTransformer(BaseTransformer):
    def transform(self, data: Iterator[Any], ticker: str, to_dict: bool = False) -> Iterator[Any]:

        for elem in data:
            elem = CandleModel(
                secid=ticker,
                open=elem.open,
                close=elem.close,
                high=elem.high,
                low=elem.low,
                value=elem.value,
                volume=elem.volume,
                begin=elem.begin,
                end=elem.end
            )
            yield elem.model_dump()
