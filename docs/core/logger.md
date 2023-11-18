# JSONPyCraft Core Module: `jsonpycraft/core/logger.py`

This module provides a utility function for configuring and obtaining a default logger instance.

## Module Overview

The `jsonpycraft/core/logger.py` module offers a simple and configurable logging utility for the JSONPyCraft project. It includes the following key features:

- `get_default_logger` function: Retrieves or creates a default logger instance with customizable settings, such as the logger's name, log level, log output stream, and log message format.

## Usage

To use the logging utility provided by this module, follow these steps:

1. **Import the Module**:

   ```python
   from jsonpycraft.core import logger
   ```

2. **Obtain a Configured Logger**:

   Use the `get_default_logger` function to obtain a configured logger instance. Customize the logger's name, log level, log output stream, and log message format as needed.

   Example:

   ```python
   import logging
   from jsonpycraft.core import logger

   # Get a default logger with custom settings
   my_logger = logger.get_default_logger(
       name="MyLogger",
       level=logging.INFO,
       stream=sys.stdout,
       fmt="%(asctime)s - %(levelname)s - %(message)s"
   )
   my_logger.info("This is an info message.")
   ```

## Function Parameters

- `name` (str, optional): The name of the logger (default is None, which uses the root logger).
- `level` (int, optional): The log level for the logger (default is logging.DEBUG).
- `stream` (Optional[IO], optional): The stream where log messages should be written (default is sys.stdout).
- `fmt` (str, optional): The log message format (default is LOGGER_FORMAT).

## Notes

- If a logger with the specified `name` already exists, the `get_default_logger` function returns the existing logger to ensure consistent logging across the application.
- By default, log messages are written to the standard output (stdout) with a log format that includes a timestamp, log level, and the log message itself.

For detailed information and examples on how to use the `jsonpycraft/core/logger.py` module, refer to the module's source code.

These logging utilities aim to provide a straightforward yet flexible way to manage logging in the JSONPyCraft project.