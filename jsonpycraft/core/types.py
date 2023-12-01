"""
jsonpycraft/core/types.py

This module defines custom types and error handling related to JSON data.

Custom Types:
- JSONMap: A dictionary with string keys and values of any type.
- JSONList: A list of dictionaries, where each dictionary has string keys and values of any type.
- JSONData: A union type representing JSONMap or JSONList for flexibility in JSON data representation.

File Handling Error Types:
- FileError: A tuple of file-related error types, including FileNotFoundError, NotADirectoryError, PermissionError, IsADirectoryError, and IOError.

Custom Error Types for JSON Encoding and Decoding:
- EncodeError: A tuple of error types for JSON encoding, including TypeError (raised by json.dump(s)).

- DecodeError: A tuple of error types for JSON decoding, including json.JSONDecodeError (raised by json.loads).

- JSONError: A unified set of error types for handling JSON-related errors, including both EncodeError and DecodeError.

Usage:
- Import this module to use the custom types and error handling in your code.
"""

from json import JSONDecodeError
from typing import Any, Dict, List, Union

# Custom Types Definitions
JSONMap = Dict[str, Any]
JSONList = List[JSONMap]
JSONData = Union[JSONMap, JSONList]

# File Handling Error Definitions
FileError = (
    FileNotFoundError,
    NotADirectoryError,
    PermissionError,
    IsADirectoryError,  # For handling directories where a file is expected
    IOError,  # For general I/O errors
)

# TypeError is raised by json.dumps for invalid JSON types
EncodeError = (TypeError,)

# JSONDecodeError is raised by json.loads for invalid JSON formatting
DecodeError = (JSONDecodeError,)

# Custom Error Definitions for JSON Encoding and Decoding
JSONError = EncodeError + DecodeError
