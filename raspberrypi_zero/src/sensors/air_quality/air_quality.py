from sensors.air_quality.air_quality_data.air_quality_data import *
from sensors.air_quality.air_quality_config_loader import AirQualityConfigLoader
from sensors.sensor.sensor import Sensor

import logging
from pathlib import Path

class AirQuality(Sensor):
    def __init__(self, config_pathname: Path):
        super().__init__(config_pathname=config_pathname)
        self._setup()

    def _setup(self):
        self._loader()
        self._setup_device()

    def _loader(self):
        """
        Load config file for Air Quality sensor from given pathname
        """
        try:
            self.config = AirQualityConfigLoader(config_pathname=self.config_pathname)
        except Exception as e:
            self.logger.error(f"Could not open the config file for Air Quality: {e}")
            self.stop()

    def _setup_device(self):
        pass

    def publish(self):
        pass

    def run(self):
        pass
   
    def stop(self):
        pass