from sensors.sensor.sensor_data.sensor_data import *

import board
from pydantic import BaseModel, field_validator

class DHT22Data(SensorData):
    pin: object = board.D4

    @field_validator("pin", mode="before")
    @classmethod
    def resolve_pin(cls, value):
        if isinstance(value, str) and value.startswith("board."):
            pin_name = value.split(".", 1)[1]
            return getattr(board, pin_name)
        return value

class DHT22Record(SensorRecord):
    temperature: float = 0.0
    humidity: float = 0.0

