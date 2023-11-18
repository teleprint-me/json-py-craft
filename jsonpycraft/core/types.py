"""
jsonpycraft/core/types.py
"""
import json
from typing import Any, Dict, List, Union

# NOTE:
# List[Dict[str, Any]] uses a data type value of Any,
# enforcing generic types, to allow for portability.
JSONMap = Dict[str, Any]
JSONList = List[JSONMap]
JSONData = Union[JSONMap, JSONList]

EncodeError = (
    TypeError,  # raised by json.dump(s)
    FileNotFoundError,
    NotADirectoryError,
    PermissionError,
)

DecodeError = (
    json.JSONDecodeError,  # raised by json.load(s)
    FileNotFoundError,
    NotADirectoryError,
    PermissionError,
)

JSONError = EncodeError + DecodeError
