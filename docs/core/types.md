# JSONPyCraft Core Module: `jsonpycraft/core/types.py`

This module defines custom types and error handling related to JSON data.

## Custom Types

### `JSONMap`
A dictionary with string keys and values of any type.

### `JSONList`
A list of dictionaries, where each dictionary has string keys and values of any type.

### `JSONData`
A union type representing either `JSONMap` or `JSONList` for flexibility in JSON data representation.

## File Handling Error Types

### `FileError`
A tuple of file-related error types, which includes:
- `FileNotFoundError`: For handling cases where a file is not found.
- `NotADirectoryError`: For errors related to directory issues.
- `PermissionError`: For errors arising due to insufficient permissions.
- `IsADirectoryError`: For handling directories where a file is expected.
- `IOError`: For general input/output errors.

## Custom Error Types for JSON Encoding and Decoding

### `EncodeError`
A tuple of error types for JSON encoding, including:
- `TypeError`: Raised by `json.dump(s)` for encoding errors.

### `DecodeError`
A tuple of error types for JSON decoding, including:
- `json.JSONDecodeError`: Raised by `json.loads` for decoding errors.

### `JSONError`
A unified set of error types for handling JSON-related errors. It includes both `EncodeError` and `DecodeError`.

## Usage
- Import this module to use the custom types and error handling in your Python code.

These updates expand error handling capabilities and enhance documentation for better comprehension and usability of the `jsonpycraft/core/types.py` module.
