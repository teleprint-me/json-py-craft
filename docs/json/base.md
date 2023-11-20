# JSONPyCraft JSONBaseTemplate Usage Guide

## Introduction

The JSONPyCraft project includes the `JSONBaseTemplate` class, which serves as a fundamental component for working with JSON files. This guide provides an overview of how to use the `JSONBaseTemplate` class effectively for JSON file management in your Python projects.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Initialization](#initialization)
- [Loading JSON Data](#loading-json-data)
- [Saving JSON Data](#saving-json-data)
- [Backing Up JSON Files](#backing-up-json-files)
- [Creating the Directory](#creating-the-directory)

## Prerequisites

Before using the `JSONBaseTemplate` class, ensure that you have the following prerequisites in place:

- Python installed on your system.
- Familiarity with Python programming concepts.

## Initialization

To begin working with the `JSONBaseTemplate` class, you should first initialize an instance. Here's how you can do it:

```python
from jsonpycraft.json.base import JSONBaseTemplate

# Define the path to your JSON file
file_path = "path/to/your/json/file.json"

# Create an instance of JSONBaseTemplate
json_template = JSONBaseTemplate(file_path)
```

### Optional Logger

You can provide an optional logger for error handling during initialization. If not provided, a default logger will be used.

```python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Initialize JSONBaseTemplate with the custom logger
json_template = JSONBaseTemplate(file_path, logger=logger)
```

## Loading JSON Data

To load JSON data from a file into the `_data` attribute, use the `load_json()` method:

```python
if json_template.load_json():
    print("JSON data loaded successfully!")
else:
    print("Error loading JSON data.")
```

## Saving JSON Data

To save JSON data to a file, use the `save_json()` method. You can provide the data to be saved as an argument, and it will also update the `_data` attribute if data is provided:

```python
data_to_save = {"key": "value"}

if json_template.save_json(data_to_save):
    print("JSON data saved successfully!")
else:
    print("Error saving JSON data.")
```

## Backing Up JSON Files

You can create a backup of the JSON file using the `backup_json()` method. This method creates a backup file with the extension `.backup.json`:

```python
if json_template.backup_json():
    print("JSON file successfully backed up!")
else:
    print("Error creating a backup of the JSON file.")
```

## Creating the Directory

If the directory for the JSON file does not exist, you can create it using the `make_directory()` method:

```python
if json_template.make_directory():
    print("Directory created successfully!")
else:
    print("Error creating the directory.")
```

## Conclusion

The `JSONBaseTemplate` class simplifies JSON file management in your Python projects. By following the guidelines in this usage guide, you can effectively load, save, back up, and create directories for your JSON files.

For more advanced usage and detailed information, refer to the module's source code and additional project documentation.
