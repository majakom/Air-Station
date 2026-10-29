from sensors.DHT22.DHT22_config_loader import DHT22ConfigLoader
from sensors.DHT22.DHT22_data.DHT22_data import DHT22Record
from sensors.sensor.sensor import Sensor

import adafruit_dht
from pathlib import Path
from datetime import datetime, timezone

class DHT22(Sensor):
    def __init__(self, config_pathname: Path):
        super().__init__(config_pathname=config_pathname)
        self._setup()

    def _setup(self):
        self._loader()
        self._setup_device()

    def _loader(self):
        """
        Load config file for DHT22 sensor from given pathname
        """
        try:
            self.config = DHT22ConfigLoader(config_pathname=self.config_pathname)
        except Exception as e:
            self.logger.error(f"Could not open the config file for DHT22: {e}")
            self.stop()

    def _setup_device(self):
        self.device = adafruit_dht.DHT22(self.config.pin, use_pulseio=False)

    def read_temperature(self) -> float:
        return self.device.temperature

    def read_humidity(self) -> float:
        return self.device.humidity

    def publish(self) -> DHT22Record | None:
        """
        Send record of data for DHT22
        """
        try:
            return DHT22Record( id_measurement=0, 
                                timestamp=datetime(timezone.utc),
                                temperature=self.read_temperature(),
                                humidity=self.read_humidity())            
        except Exception as e:
            self.logger.error(f"Failed sending record message for DHT22: {e}")
            return None

    def run(self):
        pass

    def stop(self):
        pass
