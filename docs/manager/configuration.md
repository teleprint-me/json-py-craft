# ConfigurationManager Class

The `ConfigurationManager` class is a key component of the **JSONPyCraft** library. It provides a high-level interface for managing configuration data in a JSON-based format. This class is designed to simplify the process of handling configuration settings, including loading, saving, backing up, and accessing values within the configuration data.

## Class Hierarchy

- `Singleton` (Inherits from)
  - `ConfigurationManager`

### `ConfigurationManager(file_path: str, initial_data: Optional[JSONMap] = None, indent: int = 2)`

- **Purpose**: The constructor initializes a new `ConfigurationManager` instance, setting up the essential links to a JSON configuration file. It is designed to manage configuration settings, whether creating a new file or handling an existing one.

- **Parameters**:
  - `file_path` (str): The path to the JSON configuration file. This parameter is crucial as it determines which file the manager will interact with for all operations. The path can be relative or absolute.
  - `initial_data` (Optional[JSONMap]): Optional initial data to populate a new configuration file. This parameter is particularly useful for establishing default settings in a configuration. It is important to note that if the specified JSON file already exists, this initial data does not merge with the existing data; instead, it's used only if the file does not exist or when explicitly saving this data.
  - `indent` (int, optional): Sets the JSON indentation level for the output format, affecting the readability of the saved configuration file. The default is 2, which is a standard practice for JSON formatting.

- **Functionality**:
  - Upon instantiation, `ConfigurationManager` prepares to manage the specified JSON file. The `initial_data` is held in readiness to be used if needed (e.g., creating a new file or explicitly saving this initial data). No automatic merging of `initial_data` with existing data occurs.
  - The `indent` parameter influences the aesthetics of the JSON file, making it more readable when opened in a text editor.

- **Error Handling**: 
  - The constructor itself does not handle errors related to file operations or data handling. These are managed within their respective methods (`load`, `save`, and `backup`). This design choice keeps the constructor simple and delegates error handling to the specific operations where errors are more likely to occur.

- **Example Usage**:
  - Showcasing the initialization of the `ConfigurationManager` with and without the `initial_data` parameter.

```python
# Initializing ConfigurationManager for an existing configuration file
config_manager = ConfigurationManager("existing_config.json")

# Initializing ConfigurationManager with initial data for a new configuration file
initial_config = {"app_name": "MyApp", "version": "1.0"}
config_manager = ConfigurationManager("new_config.json", initial_data=initial_config)
```

## Methods

### `load() -> None`

- Loads configuration data from the file.
- Raises:
  - `JSONFileErrorHandler`: If there is a file-related error accessing the JSON file.
  - `JSONDecodeErrorHandler`: If there is an error loading JSON data from the file.

### `save() -> None`

- Saves configuration data to the file.
- Raises:
  - `JSONFileErrorHandler`: If there is a file-related error accessing the JSON file.
  - `JSONEncodeErrorHandler`: If there is an error saving JSON data to the file.

### `backup() -> None`

- Creates a backup of the configuration file.
- Raises:
  - `JSONFileErrorHandler`: If there is an error creating a backup of the JSON file.
  - `JSONDecodeErrorHandler`: If there is an error loading JSON data from the file during backup.
  - `JSONEncodeErrorHandler`: If there is an error saving JSON data to the file during backup.

### `get_value(key: str, default: Optional[Any] = None) -> Any`

- Retrieves a configuration value based on the provided key. Supports accessing nested values in the configuration data.
- Parameters:
  - `key` (str): The key for the desired value. Supports dot notation for nested keys (e.g., "section.subsection.key").
  - `default` (Optional[Any]): The default value to return if the key is not found. Ensures type consistency with the expected return value.
- Returns:
  - The value corresponding to the key or the default value if the key is not found. If a non-existent key is provided and no default is specified, returns `None`.

Examples:

```python
# Retrieving a simple configuration value with a default
app_name = config_manager.get_value("app.name", "MyApp")
print(f"Application Name: {app_name}")

# Accessing a nested configuration value
db_port = config_manager.get_value("database.settings.port", 3306)
print(f"Database Port: {db_port}")

# Handling non-existent keys
unknown_key_value = config_manager.get_value("nonexistent.key")
if unknown_key_value is None:
    print("The key 'nonexistent.key' was not found in the configuration.")
```

### `set_value(key: str, value: Any) -> bool`

- **Purpose**: Assigns a new value to a specified configuration key. This method is versatile and can handle both top-level and nested keys within the configuration structure.

- **Parameters**:
  - `key` (str): The key under which the value will be set. Supports dot notation for nested keys (e.g., "section.subsection.key"), allowing for deep updates within the configuration structure.
  - `value` (Any): The new value to be assigned. This can be of any data type supported by JSON (e.g., string, number, object).

- **Returns**:
  - `bool`: Always returns `True` if the update is successful.

- **Behavior and Error Handling**:
  - The method internally uses `JSONMapTemplate.update_nested` to handle nested keys. In this process, keys are expanded and coerced into strings, facilitating the handling of deeply nested structures.
  - Exceptions are raised in rare edge cases, such as when an invalid key structure is passed. The method will raise a `ValueError` for invalid keys or a `TypeError` for incompatible value types.
  - It's important to note that while `set_value` is designed to be robust and handle most typical use cases smoothly, the underlying complexity of `update_nested` should be considered when dealing with highly nested or complex configurations.

- **Examples**:
  - Demonstrating both simple and nested key updates, as well as error handling:

```python
# Setting a simple configuration value
try:
    config_manager.set_value("app.version", "1.0")
    print("Configuration value 'app.version' set to '1.0'")
except (ValueError, TypeError) as e:
    print(f"Error setting 'app.version': {str(e)}")

# Updating a nested configuration value
try:
    config_manager.set_value("database.settings.hostname", "db.example.com")
    print("Database hostname updated successfully.")
except (ValueError, TypeError) as e:
    print(f"Error updating database hostname: {str(e)}")
```

### `evaluate_path(key: str, default_path: Optional[Any] = None, default_type: str = "dir") -> Optional[str]`

- **Purpose**: This method is designed to retrieve and validate paths from the configuration data. It is particularly useful for dynamically determining file or directory paths based on the configuration settings.

- **Parameters**:
  - `key` (str): The key corresponding to the path in the configuration data. This key can be a simple string or a dot-notated string for nested keys.
  - `default_path` (Optional[str], optional): A fallback path to return when the specified key is not found in the configuration. This parameter allows for a default behavior when a configuration entry is missing.
  - `default_type` (str, optional): Specifies the expected type of the path – either "file" or "dir". This is used to determine the nature of the path validation and creation process. Defaults to "dir", implying that in the absence of explicit specification, the path is treated as a directory.

- **Returns**:
  - `Optional[str]`: The method returns the evaluated path as a string. If the key is not found, and a `default_path` is provided, that path is returned. If no `default_path` is specified, it returns `None`.

- **Functionality and Behavior**:
  - The method first attempts to retrieve the path specified by the `key`. If the path is not found in the configuration, and `default_path` is provided, the method returns this default path.
  - If the path does not exist in the file system, the method will attempt to create it based on the `default_type` parameter. For example, if `default_type` is "dir", it will try to create the directory structure. If it is "file", it will create an empty file at that location.
  - This functionality is particularly useful for ensuring that required directories or files are available at runtime, especially in scenarios where the application dynamically generates or modifies paths.

- **Examples**:
  - Demonstrating how to retrieve and automatically create paths:

```python
# Retrieve a configuration path for logging
log_path = config_manager.evaluate_path("logging.directory", default_path="/var/logs/myapp", default_type="dir")
print(f"Log Path: {log_path}")

# Handle a configuration path for a data file
data_file_path = config_manager.evaluate_path("data.filepath", default_path="data/default_data.json", default_type="file")
print(f"Data File Path: {data_file_path}")
```

### `get_environment(variable: str, key: Optional[str] = None) -> str`

- **Purpose**: Retrieves the value of an environment variable, optionally mapping it to a configuration key. This method is designed to bridge the gap between the application's runtime environment and its configuration settings.

- **Parameters**:
  - `variable` (str): Specifies the name of the environment variable to retrieve. This should match the variable's name as it is set in the system's environment.
  - `key` (Optional[str]): If provided, this parameter points to a key within the configuration data where the environment variable value is expected to be mirrored or overridden. This allows for dynamic configuration changes based on environmental conditions.

- **Returns**:
  - `str`: The value of the specified environment variable. If the variable is not found in the system's environment and a `key` is provided, the method will attempt to retrieve the value from the configuration data associated with that key.

- **Behavior and Use Cases**:
  - The method first checks the system's environment for the specified `variable`. If found, its value is returned.
  - If the environment variable is not set, and a `key` is provided, the method looks up this key in the configuration data. This feature is useful for scenarios where certain settings might be overridden or specified within the application configuration instead of the environment.
  - This dual approach (environment variable first, then configuration data) provides flexibility and a fallback mechanism, allowing applications to adapt to different deployment environments and configurations seamlessly.

- **Examples**:
  - Demonstrating how to retrieve an environment variable and fallback to configuration data:

```python
# Retrieving a database URL from an environment variable or configuration file
db_url = config_manager.get_environment("DATABASE_URL", key="database.url")
print(f"Database URL: {db_url}")

# Getting an API key with fallback to configuration if not set in the environment
api_key = config_manager.get_environment("API_KEY", key="api.credentials.key")
print(f"API Key: {api_key}")
```

### `get_logger(key: str, logger_name: str, level: str = "DEBUG", logger_format: Optional[str] = None) -> Logger`

- **Purpose**: Retrieves a logger instance that is configured based on provided settings. This method offers customization for the logger's name, log level, and format, allowing for tailored logging setups according to different parts of an application.

- **Parameters**:
  - `key` (str): A unique key identifying the logger's configuration. This key is used to retrieve log settings such as file path and level from the configuration data.
  - `logger_name` (str): The name of the logger, which can be used to retrieve the same logger instance across different parts of the application.
  - `level` (str, optional): Specifies the log level (e.g., "DEBUG", "INFO", "ERROR"). The default level is "DEBUG".
  - `logger_format` (str, optional): Defines the format of the log messages. If not specified, a default format or the format specified in the configuration is used.

- **Returns**:
  - `Logger`: A configured logger instance tailored for logging messages as per the specified settings.

- **Behavior and Error Handling**:
  - The method uses the `key` to fetch specific configuration settings related to logging, such as file paths and log levels.
  - If a logger with the given `logger_name` already exists, it returns that instance to ensure consistent logging throughout the application.
  - Log messages are written to a file as specified in the configuration, and if `logger_format` is provided, it customizes the appearance of log messages.
  - A `ValueError` is raised if the logger configuration for the specified `key` is not found.

- **Examples**:
  - Illustrating the creation of a custom logger:

```python
# Creating a logger with a specific level and format
logger = config_manager.get_logger("logger_config", "my_logger", "INFO", "%(asctime)s - %(levelname)s - %(message)s")
logger.info("This is an info message.")
```

- **Notes**:
  - The method's flexibility in specifying logger configuration makes it ideal for applications that require different logging behaviors in various components or modules.
  - The addition of `logger_format` provides greater control over log message formatting, enhancing readability and debugging.

# Usage Example

Here's a comprehensive example of how to use the `ConfigurationManager` class to manage configuration data within a Python application:

```python
from jsonpycraft.core.errors import JSONEncodeErrorHandler, JSONDecodeErrorHandler
from jsonpycraft.manager.configuration import ConfigurationManager

# Initialize the ConfigurationManager with a file path
config_file_path = "config.json"
config_manager = ConfigurationManager(config_file_path)

# Load configuration data from the file
try:
    config_manager.load()
    print("Configuration data loaded successfully.")
except JSONDecodeErrorHandler:
    raise JSONDecodeErrorHandler("Failed to load configuration data.")

# Get a configuration value
app_name = config_manager.get_value("app.name", "MyApp")
print(f"Application Name: {app_name}")

# Set a new configuration value
config_manager.set_value("app.version", "1.0")
print("Configuration value 'app.version' set to '1.0'")

# Evaluate a path for log files
log_path = config_manager.evaluate_path("logging.directory", default_path="/var/logs/myapp", default_type="dir")
print(f"Log Path: {log_path}")

# Get an environment variable or fallback to a default
db_url = config_manager.get_environment("DATABASE_URL", key="database.url")
print(f"Database URL: {db_url}")

# Create and configure a logger
logger = config_manager.get_logger("logger_config", "my_logger", "INFO")
logger.info("Configuration manager initialized successfully.")

# Save the updated configuration data
try:
    config_manager.save()
    print("Configuration data saved successfully.")
except JSONEncodeErrorHandler:
    raise JSONEncodeErrorHandler("Failed to save configuration data.")

# Create a backup of the configuration file
try:
    config_manager.backup()
    print("Backup created successfully.")
except JSONEncodeErrorHandler:
    raise JSONEncodeErrorHandler("Failed to backup configuration data.")
```

This example demonstrates several key operations:
- Loading configuration data from a file.
- Retrieving and setting configuration values.
- Evaluating paths for specific configurations, such as log directories.
- Integrating environment variables into the configuration.
- Setting up and using a custom logger.
- Saving updates to the configuration and creating backups.

This example provides a practical illustration of how `ConfigurationManager` can be utilized in real-world scenarios, covering a wide range of its capabilities. This holistic approach helps with understanding how different methods and features can work together effectively.
