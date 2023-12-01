# JSONPyCraft JSONBaseTemplate Usage Guide

## Introduction

The JSONPyCraft project includes the `JSONBaseTemplate` class, serving as a fundamental component for managing JSON files. This guide outlines the effective use of the `JSONBaseTemplate` class for JSON file management in Python projects.

## Prerequisites

Before using `JSONBaseTemplate`, ensure you have:

- Python installed on your system.
- Basic familiarity with Python programming.

## Initialization

Initialize an instance of `JSONBaseTemplate` as follows:

```python
from jsonpycraft.json.base import JSONBaseTemplate

# Path to your JSON file
file_path = "path/to/your/json/file.json"

# Create an instance
json_template = JSONBaseTemplate(file_path)
```

## Loading JSON Data

To load JSON data into the `_data` attribute, use the `load_json()` method. This method now raises exceptions on failure:

```python
try:
    json_template.load_json()
    print("JSON data loaded successfully!")
except DecodeError as e:
    print(f"Error loading JSON data: {e}")
```

## Saving JSON Data

Use `save_json()` to save JSON data. This method can also update the `_data` attribute if data is provided and raises exceptions on failure:

```python
data_to_save = {"key": "value"}

try:
    json_template.save_json(data_to_save)
    print("JSON data saved successfully!")
except EncodeError as e:
    print(f"Error saving JSON data: {e}")
```

## Backing Up JSON Files

Create a backup of the JSON file with `backup_json()`, which raises exceptions on failure:

```python
try:
    json_template.backup_json()
    print("JSON file successfully backed up!")
except JSONError as e:
    print(f"Error creating a backup of the JSON file: {e}")
```

## Creating the Directory

Create the directory for the JSON file with `make_directory()`, which now raises exceptions on failure:

```python
try:
    json_template.make_directory()
    print("Directory created successfully!")
except FileError as e:
    print(f"Error creating the directory: {e}")
```

## Conclusion

The `JSONBaseTemplate` class streamlines JSON file management in Python. By leveraging this class, you can effectively load, save, back up, and manage directories for JSON files with robust error handling.

For advanced usage and more detailed information, refer to the module's source code and additional documentation.
