from air_quality_config_loader import AirQualityConfigLoader
from sensor.sensor import Sensor

import logging
from pathlib import Path

class AirQuality(Sensor):
    def __init__(self):
        super().__init__()
        self._setup()
        self._pathname = Path("air_quality_config.yaml") #TODO: move this

    def _setup(self):
        self._loader()

    def _loader(self):
        """
        Load config .yaml file from the given pathname
        """
        self._config = AirQualityConfigLoader(pathname=self._pathname)
        self.id_device = self._config.id_device
        

    def run(self):
        pass
   
    def stop(self):
        pass