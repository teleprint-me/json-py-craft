"""
jsonpycraft/core/logger.py

This module provides a utility function for configuring and obtaining a
default logger instance.

The `get_default_logger` function retrieves or creates a default logger
instance with specified configuration. It allows customization of the
logger's name and log level.

Usage:
- Import this module to use the `get_default_logger` function.
- Use the `get_default_logger` function to obtain a configured logger
  instance for logging in your Python code.

Example:

    import logging
    from jsonpycraft.core import logger

    # Get a default logger with a custom name and log level
    my_logger = logger.get_default_logger("MyLogger", logging.INFO)
    my_logger.info("This is an info message.")

Note:
- If a logger with the specified `name` already exists, the function returns
  the existing logger to ensure consistent logging across the application.
- By default, log messages are written to the standard output (stdout) with a
  log format that includes a timestamp, filename, line number, log level, and
  the log message itself.
"""

import logging
import sys
from typing import IO, Optional

LOGGER_FORMAT = "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"


def get_default_logger(
    name: Optional[str] = None,
    level: Optional[int] = logging.DEBUG,
    stream: Optional[IO] = sys.stdout,
    fmt: Optional[str] = LOGGER_FORMAT,
):
    """
    Get a default logger instance with specified configuration.

    Args:
        name (str, optional): The name of the logger (default is None, which uses the root logger).
        level (int, optional): The log level for the logger (default is logging.DEBUG).
        stream (Optional[IO], optional): The stream where log messages should be written (default is sys.stdout).
        fmt (str, optional): The log message format (default is LOGGER_FORMAT).

    Returns:
        Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler(stream=stream)
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger
