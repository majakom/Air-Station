from pydantic import BaseModel
from datetime import datetime, timezone

class SensorData(BaseModel):
    id_device: str = ""

class SensorRecord(BaseModel):
    id_measurement: int = 0
    timestamp: datetime = datetime.now(timezone.utc)