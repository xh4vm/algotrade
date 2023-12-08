from datetime import datetime

from src.models.base import JSONModel, UUIDMixin, CreatedModelMixin


class PredictionModel(JSONModel, UUIDMixin, CreatedModelMixin):
    secid: str
    algorithm: str
    prediction: float
    timestamp: datetime
