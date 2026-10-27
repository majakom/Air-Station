from sensor.sensor_data.sensor_data import *

from dataclasses import dataclass
@dataclass
class AirQualityData(SensorData):
    pin: int = 0 

@dataclass
class AirQualityRecord(SensorRecord):
    raise NotImplemented
