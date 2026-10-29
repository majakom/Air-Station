from connection.connection_handler import ConnectionHandler

import logging
from pathlib import Path
import threading
import importlib.util

class Service(threading.Thread):
    def __init__(self, connection_config_pathname: Path):
        super().__init__()
        self._connection_config_pathname = connection_config_pathname
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._find_all_sensors()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def _make_root_sensors() -> Path:
        """
        Find root for given folder_name
        """
        return Path(__file__).parent / Path('sensors')

    @staticmethod
    def _make_root_config() -> Path:
        """
        Find root for res/sensors/ with {sensor_name}_config.yaml files inside
        """
        return Path(__file__).parent.parent / 'res' / 'sensors'

    def _find_all_sensors(self):
        """
        In order to add new sensor:
        Structure: src/sensors/{name}/{name}.py
        where {name} is a name of a sensor
        In {name}.py put class names {Name} starting with a capital letter
        """
        _sensor_root = self._make_root_sensors()

        self.sensors = {}
        for folder in _sensor_root.iterdir():
            folder_name = folder.name
            if folder.is_dir() and folder_name != 'sensor' and not folder_name.startswith('__'):
                self.sensors[folder_name] = _sensor_root / Path(folder_name) / Path(f"{folder_name}.py")

        config_pathname_root = self._make_root_config()
        for name, file_path in self.sensors.items():
            spec = importlib.util.spec_from_file_location(name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            class_name = name if name.isupper() else name.title()
            class_name = class_name.replace("_", "")
            sensor_class = getattr(module, class_name)

            config_pathname = config_pathname_root / Path(f"{name}_config.yaml")
            self.sensors[name] = sensor_class(config_pathname=config_pathname)

    def run(self):
        """
        Run all sensors and MQTT communication
        """
        try:
            self.newMQTTService = ConnectionHandler(config_pathname=self._connection_config_pathname)
            self.newMQTTService.start()
        except Exception as e:
            self._logger.error(f"Could not start MQTT connection thread - {e}")

        for name, sensor_class in self.sensors.items():
            try:
                self._logger.info(f"Running sensor {name}")
                self.sensors[name] = sensor_class.start()
            except Exception as e:
                self._logger.error(f"Could not start sensor class thread: {name} - {e}")

    def stop(self):
        """
        Stop all sensors and MQTT client
        """
        try:
            self.newMQTTService.join()
        except Exception as e:
            self._logger.error(f"Could not stop MQTT connection thread - {e}")

        for name, sensor_class in self.sensors.items():
            try:
                self._logger.info(f"Stopping sensor {name}")
                self.sensors[name] = sensor_class().join()
            except Exception as e:
                self._logger.error(f"Could not stop sensor class thread: {name} - {e}")
            
