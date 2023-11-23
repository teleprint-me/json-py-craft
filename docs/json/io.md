# JSON I/O Module

The `jsonpycraft/json/io.py` module is responsible for handling input and output operations related to JSON data within the JSON-Py-Craft library. It provides utility functions for reading, writing, and manipulating JSON data from files.

## Functions

### `read_json(filepath: Union[str, Path]) -> JSONData`

Read JSON data from a file.

- Parameters:
  - `filepath` (Union[str, Path]): The path to the JSON file.

- Returns:
  - `JSONData`: The deserialized JSON data.

- Raises:
  - `DecodeError`: If there is an error reading or decoding the JSON data.

### `dump_json(filepath: Union[str, Path], indent: int = 2) -> str`

Serialize JSON data to a formatted string.

- Parameters:
  - `filepath` (Union[str, Path]): The path to the JSON file.
  - `indent` (int, optional): The number of spaces to use for indentation in the formatted JSON string (default is 2).

- Returns:
  - `str`: The serialized JSON data in a formatted string.

- Raises:
  - `EncodeError`: If there is an error encoding the JSON data.

### `write_json(filepath: Union[str, Path], content: JSONData, indent: int = 2) -> None`

Write JSON data to a file.

- Parameters:
  - `filepath` (Union[str, Path]): The path to the JSON file.
  - `content` (JSONData): The data to be serialized and written as JSON.
  - `indent` (int, optional): The number of spaces to use for indentation in the JSON file (default is 2).

### `force_read_json(filepath: Union[str, Path], content: JSONData) -> JSONData`

Read JSON data from a file or create the file with default content if it doesn't exist.

If the specified file does not exist, it will be created with the provided content. This function is useful for ensuring that a file exists before reading from it.

- Parameters:
  - `filepath` (Union[str, Path]): The path to the JSON file.
  - `content` (JSONData): The default content to be written as JSON if the file doesn't exist.

- Returns:
  - `JSONData`: The deserialized JSON data.

- Raises:
  - `DecodeError`: If there is an error reading or decoding the JSON data.

## Example Usage

```python
from jsonpycraft.json.io import read_json, write_json

# Reading JSON data from a file
data = read_json("data.json")

# Modifying the data
data["new_key"] = "new_value"

# Writing the modified data back to the file
write_json("data.json", data)
```

## Notes

- The functions provided by this module make it easy to work with JSON data stored in files, whether you need to read, write, or manipulate the data.
- Error handling is built into these functions to provide informative error messages in case of issues related to JSON encoding or decoding.
