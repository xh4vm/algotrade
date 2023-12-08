from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from datetime import datetime
from typing import Annotated

from src.containers.candle import ServiceContainer
from src.services.trades.candle import CandleService
from src.models.candle import CandleTS


router = APIRouter(prefix='/trades', tags=['Trade functions'])


@router.get(path='/ts/candle', name='Candle timeseries', response_model=list[CandleTS])
@inject
async def get_all_tickers(
    secid: str,
    ts: str,
    till_ts: str | None = None,
    interval: Annotated[str, Query(pattern='\d+\s+(?:hour|minute|day)')] = '1 minute',
    candle_service: CandleService = Depends(Provide[ServiceContainer.candle_service])
) -> list[CandleTS]:
    
    candles_gen = candle_service.get_time_series(
        secid=secid,
        fields=[
            'secid',
            'median(open) as open',
            'median(close) as close',
            'median(high) as high',
            'median(low) as low',
            'median(volume) as volume',
            'median(value) as value',
            f'toStartOfInterval(begin, INTERVAL {interval}) as begin'
        ],
        ts=datetime.fromisoformat(ts) if ts is not None else None,
        till_ts=datetime.fromisoformat(till_ts) if till_ts is not None else None,
        group_by=['secid', 'begin'],
        order_by={'desc': ['begin']}
    )

    return [candle async for candle in candles_gen]
