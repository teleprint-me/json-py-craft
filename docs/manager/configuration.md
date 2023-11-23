# ConfigurationManager Class

The `ConfigurationManager` class is a key component of the JSON-Py-Craft library. It provides a high-level interface for managing configuration data in a JSON-based format. This class is designed to simplify the process of handling configuration settings, including loading, saving, backing up, and accessing values within the configuration data.

## Class Hierarchy

- `Singleton` (Inherits from)
  - `ConfigurationManager`

## Constructor

### `ConfigurationManager(file_path: str, initial_data: Optional[JSONMap] = None, logger: Optional[Logger] = None)`

- Initializes a new `ConfigurationManager` instance.
- Parameters:
  - `file_path` (str): The path to the configuration JSON file.
  - `initial_data` (Optional[JSONMap]): Optional initial configuration data.
  - `logger` (Optional[Logger]): Optional logger for error-handling.

## Methods

### `load() -> bool`

- Loads configuration data from the file.
- Returns:
  - `True` if the data was loaded successfully, `False` otherwise.

### `save() -> bool`

- Saves configuration data to the file.
- Returns:
  - `True` if the data was saved successfully, `False` otherwise.

### `backup() -> bool`

- Creates a backup of the configuration file.
- Returns:
  - `True` if the backup was created successfully, `False` otherwise.

### `get_value(key: str, default: Optional[Any] = None) -> Any`

- Gets a configuration value based on the provided key.
- Parameters:
  - `key` (str): The key to retrieve the value for.
  - `default` (Optional[Any]): The default value to return if the key is not found.
- Returns:
  - The configuration value corresponding to the key, or the default value if not found.

### `set_value(key: str, value: Any) -> bool`

- Sets a configuration value for the provided key.
- Parameters:
  - `key` (str): The key to set the value for.
  - `value` (Any): The value to set.
- Returns:
  - `True` if the value was set successfully, `False` otherwise.

### `evaluate_path(key: str, default: Optional[Any] = None) -> Optional[str]`

- Evaluates a configuration path based on the provided key.
- Parameters:
  - `key` (str): The key to retrieve the path for.
  - `default` (Optional[Any]): The default value to return if the path is not found.
- Returns:
  - The evaluated path, or the default value if not found.

### `get_environment(variable: str, key: Optional[str] = None) -> str`

- Gets the value of an environment variable.
- Parameters:
  - `variable` (str): The name of the environment variable.
  - `key` (Optional[str]): The key in the configuration data where the environment variable is stored.
- Returns:
  - The value of the environment variable.

### `get_logger(key: str, logger_name: str, level: str = "DEBUG") -> Logger`

- Gets a logger instance with specified configuration.
- Parameters:
  - `key` (str): A unique key identifying the logger configuration.
  - `logger_name` (str): The name of the logger.
  - `level` (str, optional): The log level for the logger (default is "DEBUG").
- Returns:
  - A configured logger instance.

# Usage Example

Here's a simple example of how to use the `ConfigurationManager` class to manage configuration data in your Python application:

```python
from jsonpycraft.manager.configuration import ConfigurationManager

# Initialize the ConfigurationManager with a file path
config_file_path = "config.json"
config_manager = ConfigurationManager(config_file_path)

# Load configuration data from the file
if not config_manager.load():
    # Handle the case where loading failed
    print("Failed to load configuration data.")
else:
    # Get a configuration value
    app_name = config_manager.get_value("app.name", "MyApp")
    print(f"Application Name: {app_name}")

    # Set a new configuration value
    config_manager.set_value("app.version", "1.0")

    # Save the updated configuration data
    if config_manager.save():
        print("Configuration data saved successfully.")

    # Create a backup of the configuration file
    if config_manager.backup():
        print("Backup created successfully.")
```

In this example, we first initialize the `ConfigurationManager` with the path to the configuration file (`config.json`). We then load the configuration data, retrieve and print a configuration value, set a new configuration value, save the updated data, and create a backup of the configuration file.

This demonstrates the basic usage of the `ConfigurationManager` class for managing configuration settings in your Python application.
