from sensors.air_quality.air_quality_data.air_quality_data import *
from sensors.sensor.sensor_config_loader import SensorConfigLoader

from pathlib import Path
import yaml

class AirQualityConfigLoader(SensorConfigLoader):
    def __init__(self, config_pathname: Path):
        super().__init__(config_pathname=config_pathname)
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._config_setter()

    def _config_setter(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        try:
            self.air_quality_data = AirQualityData(id_device=self.config["id_device"], pin=self.config["pin"])
            self.id_device = self.air_quality_data.id_device
            self.pin = self.air_quality_data.pin
        except Exception as e:
            self.logger.error(f"Failed loading config file for air quality: {self.config_pathname} - {e}")