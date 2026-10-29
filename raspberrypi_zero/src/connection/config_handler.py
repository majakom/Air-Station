from connection.connection_data.mqtt_data import MQTTData
from connection.connection_data.credentials_data import CredentialsData

from pathlib import Path
import logging
import yaml
from dotenv import load_dotenv
import os

class ConfigHandler:
    def __init__(self, config_pathname: Path):
        self.config_pathname = config_pathname
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._config_pathname = self._make_root() / Path(self.config_pathname)
        self._load_config()
        self._load_env()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def _load_config(self):
        """
        Open config file from "res/connection/*.yaml"
        """
        try:
            with self._config_pathname.open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.mqtt_data = MQTTData(host=config["mqtt_data"]["host"], port=config["mqtt_data"]["port"])
                self.host = self.mqtt_data.host
                self.port = self.mqtt_data.port
        except Exception as e:
            self._logger.error(f"Error during reading config file: {self.config_path} - {e}")

    def _load_env(self):
        """
        Load .env data
        """
        try:
            load_dotenv()
            self.credentials_data = CredentialsData(username=os.getenv("USERNAME_STATION", default="test"),
                                                    password=os.getenv("PASSWORD_STATION", default="test"))
            self.username = self.credentials_data.username
            self.password = self.credentials_data.password
        except Exception as e:
            self._logger.error(f"Error during reading .env file - {e}")

    def _make_root(self) -> Path:
        root = Path(__file__).resolve().parent.parent.parent
        return root / Path("res") / Path("connection")
