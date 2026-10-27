
import threading
from abc import ABC, abstractmethod
import logging
from pathlib import Path

class SensorConfigLoader(ABC, threading.Thread):
    def __init__(self):
        super().__init__()
        self._setup_logging()
        
    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def _loader_config(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        raise NotImplemented

    @staticmethod
    def _make_root():
        """
        Find path for sensor config
        """
        root = Path(__file__).resolve().parent
        return root / Path("res") / Path("sensors")
        