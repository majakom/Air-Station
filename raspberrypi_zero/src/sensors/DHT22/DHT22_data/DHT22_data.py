from sensor.sensor_data.sensor_data import *

from dataclasses import dataclass
import board
from pydantic import BaseModel

@dataclass
class DHT22Data(SensorData):
    pin: int = board.D4

@dataclass
class DHT22Record(SensorRecord):
    temperature: float = 0.0
    humidity: float = 0.0

