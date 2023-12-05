from datetime import datetime

from src.models.base import JSONModel, UUIDMixin, TimestampMixin


class TickerModel(JSONModel, UUIDMixin, TimestampMixin):
    secid: str
    boardid: str
    shortname: str
    prevprice: float | None
    lotsize: int | None
    facevalue: float | None
    status: str | None
    boardname: str | None
    decimials: int | None
    secname: str | None
    remarks: str | None
    marketcode: str | None
    instrid: str | None
    sectorid: str | None
    minstep: float | None
    prevwaprice: float | None
    faceunit: str | None
    prevdate: datetime | None
    issuesize: int | None
    isin: str | None
    latname: str | None
    regnumber: str | None
    prevlegalcloseprice: float | None
    currencyid: str | None
    sectype: str | None
    listlevel: int | None
    settledate: datetime | None
