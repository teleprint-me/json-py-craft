"""
jsonpycraft/manager/configuration.py
"""
import logging
import os
from logging import Logger
from typing import Any, Optional

import dotenv

from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import JSONMap
from jsonpycraft.json.map import JSONMapTemplate


class ConfigurationManager(Singleton):
    """
    Singleton class for managing configuration data.
    """

    def __init__(
        self,
        file_path: str,
        initial_data: Optional[JSONMap] = None,
    ):
        """
        Initialize the ConfigurationManager instance.

        Args:
            file_path (str): The path to the configuration file.
            initial_data (Optional[JSONMap], optional): Initial configuration data. Defaults to None.
            logger (Optional[Logger]): Optional logger for error-handling.
        """
        super(ConfigurationManager, self).__init__()

        # Initialize the Configuration map
        self._map_template = JSONMapTemplate(file_path, initial_data=initial_data)
        # NOTE: Removed automated loading to avoid a bug where `initial_data` was unintentionally overridden as a result.

    def load(self) -> bool:
        """
        Load configuration data from the file.

        Returns:
            bool: True if the data was loaded successfully, False otherwise.
        """
        return self._map_template.load_json()

    def save(self) -> bool:
        """
        Save configuration data to the file.

        Returns:
            bool: True if the data was saved successfully, False otherwise.
        """
        return self._map_template.save_json(self._map_template.data)

    def backup(self) -> bool:
        """
        Create a backup of the configuration file.

        Returns:
            bool: True if the backup was created successfully, False otherwise.
        """
        return self._map_template.backup_json()

    def get_value(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get a configuration value based on the provided key.

        Args:
            key (str): The key to retrieve the value for.
            default (Optional[Any], optional): The default value to return if the key is not found. Defaults to None.

        Returns:
            Any: The configuration value corresponding to the key, or the default value if not found.
        """
        keys = key.split(".")
        return self._map_template.read_nested(*keys) or default

    def set_value(self, key: str, value: Any) -> bool:
        """
        Set a configuration value for the provided key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.

        Returns:
            bool: True if the value was set successfully, False otherwise.
        """
        keys = key.split(".")
        return self._map_template.update_nested(value, *keys)

    def evaluate_path(self, key: str, default: Optional[Any] = None) -> Optional[str]:
        """
        Evaluate a configuration path based on the provided key.

        Args:
            key (str): The key to retrieve the path for.
            default (Optional[Any], optional): The default value to return if the path is not found. Defaults to None.

        Returns:
            Optional[str]: The evaluated path, or the default value if not found.
        """
        path_info = self.get_value(key, default)

        if path_info is None:
            return None

        path_type = path_info.get("type", "dir")  # default to 'dir' if not specified
        path = path_info.get("path")

        if path_type not in ["file", "dir"]:
            raise ValueError(f"Invalid path type: {path_type}")

        if not isinstance(path, str):
            raise TypeError(f"Expected a string for path but got {type(path).__name__}")

        evaluated_path = os.path.expanduser(os.path.expandvars(path))

        # Create the path if it doesn't exist
        if not os.path.exists(evaluated_path):
            if path_type == "dir":
                os.makedirs(evaluated_path)
            else:
                os.makedirs(os.path.dirname(evaluated_path), exist_ok=True)
                open(evaluated_path, "a").close()

        return evaluated_path

    def get_environment(self, variable: str, key: Optional[str] = None) -> str:
        """
        Get the value of an environment variable.

        Args:
            variable (str): The name of the environment variable.
            key (str, optional): The key in the configuration data where the environment variable is stored. Defaults to None.

        Returns:
            str: The value of the environment variable.

        NOTE:
            - The evaluated path assumes a `.env` is within the local path if key is `None`.
        """
        env_path = self.evaluate_path(key, ".env")

        if not dotenv.load_dotenv(env_path):
            raise ValueError("EnvironmentError: Failed to load `.env`")

        value = os.getenv(variable) or ""

        if not value:
            raise ValueError(f"EnvironmentError: Failed to find `{variable}`")

        return value

    def get_logger(
        self,
        key: str,
        logger_name: str,
        level: str = "DEBUG",
        logger_format: Optional[str] = None,
    ) -> Logger:
        """
        Get a logger instance with specified configuration.

        Args:
            key (str): A unique key identifying the logger configuration.
            logger_name (str): The name of the logger.
            level (str, optional): The log level for the logger (default is "DEBUG").

        Returns:
            Logger: A configured logger instance.

        NOTE:
            - The `key` parameter is used to determine the log file path and log level based on configuration settings.
            - If the logger with the specified `logger_name` already exists, it returns the existing logger to ensure consistent logging across the application.
            - Log messages are written to a log file, and the log format includes timestamp, log level, and the log message itself.
        """
        if logger_format is None:
            logger_format = (
                "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
            )

        log_info = self.get_value(key, None)

        if log_info is None:
            raise ValueError(f"Logger configuration for {key} not found.")

        default_log_dir = "/var/log/jsonpycraft/"  # Default log directory
        log_file_path = self.evaluate_path(key, default_log_dir)

        log_level = log_info.get("level", level)
        logger = logging.getLogger(logger_name)

        if not logger.handlers:
            handler = logging.FileHandler(log_file_path, "a")
            formatter = logging.Formatter(logger_format)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(log_level)

        return logger
