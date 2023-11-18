# JSONPyCraft Core Module: `jsonpycraft/core/types.py`

This module defines custom types and error handling related to JSON data.

## Custom Types

### `JSONMap`
A dictionary with string keys and values of any type.

### `JSONList`
A list of dictionaries, where each dictionary has string keys and values of any type.

### `JSONData`
A union type representing either `JSONMap` or `JSONList` for flexibility in JSON data representation.

## Error Handling

### `EncodeError`
Error types for JSON encoding:
- `TypeError`: Raised by `json.dump(s)` for encoding errors.
- `FileNotFoundError`: Raised for file-related errors during encoding.
- `NotADirectoryError`: Raised for directory-related errors during encoding.
- `PermissionError`: Raised for permission-related errors during encoding.

### `DecodeError`
Error types for JSON decoding:
- `json.JSONDecodeError`: Raised by `json.load(s)` for decoding errors.
- `FileNotFoundError`: Raised for file-related errors during decoding.
- `NotADirectoryError`: Raised for directory-related errors during decoding.
- `PermissionError`: Raised for permission-related errors during decoding.

### `JSONError`
A unified set of error types for handling JSON-related errors, including both encoding and decoding errors.

## Usage
- Import this module to use the custom types and error handling in your Python code.

For detailed information and examples on how to use these custom types and error handling, refer to the module's source code.

These updates enhance the documentation and readability of the `jsonpycraft/core/types.py` source file for better code comprehension.
