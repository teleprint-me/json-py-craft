# JSONPyCraft Core Types

The `jsonpycraft/core/types.py` module defines custom types and error handling related to JSON data.

## Custom Types

### JSONMap
A dictionary with string keys and values of any type.

### JSONList
A list of dictionaries, where each dictionary has string keys and values of any type.

### JSONData
A union type representing either `JSONMap` or `JSONList` for flexibility in JSON data representation.

## File Handling Error Types

### FileError
A tuple of file-related error types, which includes:
- `FileNotFoundError`: For handling cases where a file is not found.
- `NotADirectoryError`: For errors related to directory issues.
- `PermissionError`: For errors arising due to insufficient permissions.
- `IsADirectoryError`: For handling directories where a file is expected.
- `IOError`: For general input/output errors.

## Custom Error Types for JSON Encoding and Decoding

### EncodeError
A tuple of error types for JSON encoding, including:
- `TypeError`: Raised by `json.dump(s)` for encoding errors.

### DecodeError
A tuple of error types for JSON decoding, including:
- `json.JSONDecodeError`: Raised by `json.loads` for decoding errors.

### JSONError
A unified set of error types for handling JSON-related errors. It includes both `EncodeError` and `DecodeError`.

## Usage Example

Import this module to use the custom types and error handling in your Python code.

```python
from jsonpycraft.core.types import FileError, DecodeError, EncodeError
from jsonpycraft.core.errors import JSONFileErrorHandler, JSONDecodeErrorHandler, JSONEncodeErrorHandler

# Read from a JSON file
try:
    with open(filepath, "r") as file:
        return json.load(file)
except FileError as e:
    raise JSONFileErrorHandler(f"File error accessing {filepath}: {e}")
except DecodeError as e:
    raise JSONDecodeErrorHandler(f"Error decoding JSON data at {filepath}: {e}")

# Write to a JSON file
try:
    with open(filepath, "w") as f:
        json.dump(content, f, indent=indent)
except FileError as e:
    raise JSONFileErrorHandler(f"File error accessing {filepath}: {e}")
except EncodeError as e:
    raise JSONEncodeErrorHandler(
        f"Error encoding and writing JSON data to {filepath}: {e}"
    )
```
