
import threading
from abc import ABC, abstractmethod
import logging
import yaml
from pathlib import Path

class SensorConfigLoader(ABC, threading.Thread):
    def __init__(self, config_pathname: Path):
        super().__init__()
        self._setup_logging()
        self.config_pathname = self._make_root() / config_pathname
        self._loader_config()
        
    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def _config_setter(self):
        raise NotImplementedError

    def _loader_config(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        try:
            with self.config_pathname.open("r", encoding="utf-8") as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.error(f"Config file {self.config_pathname} not found")
        except Exception as e:
            self.logger.error(f"An exception occured during loading of config file: {self.config_pathname}: {e}")

    @staticmethod
    def _make_root():
        """
        Find path for sensor config
        """
        root = Path(__file__).resolve().parent
        return root / Path("res") / Path("sensors")
        