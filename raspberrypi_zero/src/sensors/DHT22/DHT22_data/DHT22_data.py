from sensors.sensor.sensor_data.sensor_data import *

import board
from pydantic import BaseModel

class DHT22Data(SensorData):
    pin: int = board.D4

class DHT22Record(SensorRecord):
    temperature: float = 0.0
    humidity: float = 0.0

