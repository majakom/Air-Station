from sensors.sensor.sensor_data.sensor_data import *

from dataclasses import dataclass
from pydantic import BaseModel, field_validator
import board

class AirQualityData(SensorData):
    pin: object = board.D4

    @field_validator("pin", mode="before")
    @classmethod
    def resolve_pin(cls, value):
        if isinstance(value, str) and value.startswith("board."):
            pin_name = value.split(".", 1)[1]
            return getattr(board, pin_name)
        return value

@dataclass
class AirQualityRecord(SensorRecord):
    #TODO: research this sensor TMP:
    co2: int = 0
