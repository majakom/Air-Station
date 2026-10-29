import threading
from abc import ABC, abstractmethod
import logging
from pathlib import Path

class Sensor(ABC, threading.Thread):
    def __init__(self, config_pathname: Path):
        super().__init__()
        self.config_pathname = config_pathname
        self._setup_logging()

    @abstractmethod
    def _setup(self):
        raise NotImplemented

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def _setup_device(self):
        raise NotImplemented

    @abstractmethod
    def publish(self):
        raise NotImplemented

    @abstractmethod
    def run(self):
        raise NotImplemented

    @abstractmethod
    def stop(self):
        raise NotImplemented