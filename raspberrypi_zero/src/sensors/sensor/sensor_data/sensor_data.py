from pydantic import BaseModel
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class SensorData(BaseModel):
    id_device: int = 0

@dataclass
class SensorRecord(BaseModel):
    id_measurement: int = 0
    timestamp: datetime = datetime(timezone.utc)