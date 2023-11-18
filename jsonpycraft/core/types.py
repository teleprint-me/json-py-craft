"""
jsonpycraft/core/types.py

This module defines custom types and error handling related to JSON data.

- JSONMap: A dictionary with string keys and values of any type.
- JSONList: A list of dictionaries, where each dictionary has string keys and values of any type.
- JSONData: A union type representing JSONMap or JSONList for flexibility in JSON data representation.

- EncodeError: Error types for JSON encoding, including TypeError (raised by json.dump(s)) and file-related errors.
- DecodeError: Error types for JSON decoding, including json.JSONDecodeError and file-related errors.
- JSONError: A unified set of error types for handling JSON-related errors.

Usage:
- Import this module to use the custom types and error handling in your code.
"""

import json
from typing import Any, Dict, List, Union

# Custom Types Definitions
JSONMap = Dict[str, Any]
JSONList = List[JSONMap]
JSONData = Union[JSONMap, JSONList]

# Error Definitions
EncodeError = (
    TypeError,  # Raised by json.dump(s)
    FileNotFoundError,
    NotADirectoryError,
    PermissionError,
)

DecodeError = (
    json.JSONDecodeError,  # Raised by json.load(s)
    FileNotFoundError,
    NotADirectoryError,
    PermissionError,
)

JSONError = EncodeError + DecodeError
