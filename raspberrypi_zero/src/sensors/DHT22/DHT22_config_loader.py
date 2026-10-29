from sensors.DHT22.DHT22_data.DHT22_data import DHT22Data
from sensors.sensor.sensor_config_loader import SensorConfigLoader

import logging
from pathlib import Path
import yaml

class DHT22ConfigLoader(SensorConfigLoader):
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
            print(self.config)
            self.dht22_data = DHT22Data(id_device=self.config["device"]["id_device"], pin=self.config["device"]["pin"])
            self.id_device = self.dht22_data.id_device
            self.pin = self.dht22_data.pin
        except Exception as e:
            self.logger.error(f"Failed loading config file for DHT22: {self.config_pathname} - {e}")


    