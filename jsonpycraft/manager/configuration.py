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

    def evaluate_path(
        self, key: str, default_path: Optional[str] = None, default_type: str = "dir"
    ) -> Optional[str]:
        """
        Evaluate a configuration path based on the provided key.

        This method retrieves a configuration value associated with the provided key,
        which is expected to represent a file or directory path. It evaluates the path
        by expanding environment variables and user home directory '~' if present.

        Args:
            key (str): The key to retrieve the path for.
            default_path (Optional[str], optional): The default path value to return if
                the key is not found in the configuration. Defaults to None.
            default_type (str, optional): The default type of the path, either "file" or "dir",
                if not explicitly specified in the configuration. Defaults to "dir".

        Returns:
            Optional[str]: The evaluated path, or the default path value if not found in
            the configuration. If the path does not exist, it will be created based on the
            specified path type.

        Raises:
            ValueError: If the path type specified in the configuration is invalid.
            TypeError: If the path retrieved from the configuration is not a string.

        Example Usage:

            config_manager = ConfigurationManager("path/to/config.json")
            config_manager.set_value("my_path", {"type": "dir", "path": "~/my_directory"})
            path = config_manager.evaluate_path("my_path")

        Note:
            The method will expand '~' to the user's home directory and evaluate environment
            variables in the path string before returning it. If the path does not exist, it
            will be created based on the specified path type.
        """
        path_info = self.get_value(key, default_path)

        if path_info is None:
            return default_path  # Key does not exist, return default

        if isinstance(path_info, str):
            return path_info  # Directly return the string value

        # Path type should default to 'dir' if not specified
        path_type = path_info.get("type", default_type)
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
        log_info = self.get_value(key, None)

        if log_info is None:
            raise ValueError(f"Logger configuration for {key} not found.")

        if logger_format is None:  # Only do this step if ValueError is not raised
            logger_format = (
                "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
            )

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
