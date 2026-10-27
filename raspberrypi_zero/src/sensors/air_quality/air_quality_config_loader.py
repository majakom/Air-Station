from air_quality_data.air_quality_data import AirQualityData

from pathlib import Path
import yaml

class AirQualityConfigLoader:
    def __init__(self, pathname: Path):
        self._pathname = pathname
        self._setup()

    def _setup(self):
        self.config_path = self._make_root() / self._pathname
        self._loader_config()

    def _loader_config(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        try:
            with self.config_path.open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.air_quality_data = AirQualityData(id_device=config["device"]["id_device"], pin=config["device"]["pin"])
                self.pin = self.air_quality_data.pin
                self.id_device = self.air_quality_data.id_config
        except Exception as e:
            self._logger.error(f"Failed loading config file for Air Quality: {self.config_path} - {e}")