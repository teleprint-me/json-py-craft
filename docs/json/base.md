# JSONBaseTemplate class

The `JSONBaseTemplate` class is a fundamental component of the JSONPyCraft project, designed for managing JSON files efficiently. This documentation provides insights into effectively utilizing the `JSONBaseTemplate` class in Python projects.

## Class Hierarchy

- Protocol (Inherits from)
  - JSONBaseTemplate

## Constructor

### JSONBaseTemplate(self, file_path: str, initial_data: Optional[JSONData] = None)

Initialize a new `JSONBaseTemplate` instance.

- `file_path` (str): The path to the JSON file.
- `initial_data` (Optional[JSONData]): The initial data. Defaults to None.

## Properties

### file_path

- Get the path to the JSON file (read-only).

### data

- Get the underlying JSON data structure (read-only).

## Methods

### load_json(self) -> None

Load JSON data from the file into the `_data` attribute.

Raises:
- `JSONFileErrorHandler`: If there is a file-related error accessing the JSON file.
- `JSONDecodeErrorHandler`: If there is an error loading JSON data from the file.

### save_json(self, data: Optional[JSONData] = None, indent: int = 2) -> None

Save JSON data to the file.

If data is provided, it updates the `_data` attribute as well.

Parameters:
- `data` (Optional[JSONData]): The data to be saved. Defaults to None.
- `indent` (int): The indentation level for the JSON output. Defaults to 2.

Raises:
- `JSONFileErrorHandler`: If there is a file-related error accessing the JSON file.
- `JSONEncodeErrorHandler`: If there is an error saving JSON data to the file.

### backup_json(self, indent: int = 2) -> None

Create a backup of the JSON file.

Parameters:
- `indent` (int): The indentation level for the JSON output. Defaults to 2.

Raises:
- `JSONFileErrorHandler`: If there is an error creating a backup of the JSON file.
- `JSONDecodeErrorHandler`: If there is an error loading JSON data from the file.
- `JSONEncodeErrorHandler`: If there is an error saving JSON data to the file.

### make_directory(self) -> None

Create the directory for the JSON file.

Raises:
- `JSONFileErrorHandler`: If there is an error creating the directory for the JSON file.

## Example Usage

Here's an example of how to use the `JSONBaseTemplate` class to load, modify, and save JSON data:

```python
from jsonpycraft.core.errors import JSONDecodeErrorHandler, JSONEncodeErrorHandler
from jsonpycraft.core.base import JSONBaseTemplate

# Path to your JSON file
file_path = "path/to/file.json"

# Create an instance of JSONBaseTemplate
json_template = JSONBaseTemplate(file_path)

# Load JSON data from the file
try:
    json_template.load_json()
    print("JSON data loaded successfully!")
except JSONDecodeErrorHandler as e:
    print(f"Error loading JSON data: {e}")

# Modify the loaded JSON data
if json_template.data:
    json_template.data["new_key"] = "new_value"

# Save JSON data back to the file
try:
    json_template.save_json()
    print("JSON data saved successfully!")
except JSONEncodeErrorHandler as e:
    print(f"Error saving JSON data: {e}")
```

This example demonstrates loading JSON data from a file, making modifications, and saving it back to the same file while handling potential errors. You can adapt this code snippet to your specific use case.

## Conclusion

The `JSONBaseTemplate` class streamlines JSON file management in Python. By leveraging this class, you can effectively load, save, back up, and manage directories for JSON files with robust error handling.

For advanced usage and more detailed information, refer to the module's source code and additional documentation.

### References

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python Exceptions Documentation](https://docs.python.org/3/library/exceptions.html)
