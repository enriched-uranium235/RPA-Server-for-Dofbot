from binah.config import Config
import toml
import os
from geburah.start_dofbot import start_dofbot

class ConfigManager:
    """
    ConfigManager is responsible for loading and managing the configuration settings.
    It uses the Pydantic model to validate the configuration data.
    """

    def __init__(self, config: Config):
        self.config = config

    def get_config(self) -> Config:
        return self.config
    
    def set_config(self, config: Config) -> 'ConfigManager':
        """
        Set a new configuration.
        :param config: New configuration to set.
        :return: The ConfigManager instance for method chaining.
        """
        self.config = config
        return self

def create_config():
    config_path = os.path.join(os.path.dirname(__file__), '../daath/config.toml')
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    with open(config_path) as f:
        toml_data = toml.load(f)
        config_data = {}
        if "dofbot" in toml_data:
            for key, value in toml_data["dofbot"].items():
                if isinstance(value, list) and len(value) == 2:
                    config_data[key] = tuple(value)
                else:
                    config_data[key] = value
    return Config(**config_data)