from DHT22_data.DHT22_data import DHT22Data
from sensor.sensor_config_loader import SensorConfigLoader

import logging
from pathlib import Path
import yaml

class DHT22ConfigLoader(SensorConfigLoader):
    def __init__(self, pathname: Path):
        self._pathname = pathname
        self._setup()

    def _setup(self):
        self._setup_logging()
        self.config_path = self._make_root() / self._pathname
        self._loader_config()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def _loader_config(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        try:
            with self.config_path.open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.dht22_data = DHT22Data(id_device=config["device"]["id_device"], pin=config["device"]["pin"])
                self.id_device = self.dht22_data.id_device
                self.pin = self.dht22_data.pin
        except Exception as e:
            self._logger.error(f"Failed loading config file for DHT22: {self._pathname} - {e}")

    @staticmethod
    def _make_root():
        root = Path(__file__).resolve().parent
        return root / Path("res") / Path("sensors")
    