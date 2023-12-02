"""
jsonpycraft/json/io.py
"""

import json
from pathlib import Path
from typing import Union

from jsonpycraft.core.errors import (
    JSONDecodeErrorHandler,
    JSONEncodeErrorHandler,
    JSONFileErrorHandler,
)
from jsonpycraft.core.types import DecodeError, EncodeError, FileError, JSONData


def read_json(filepath: Union[str, Path]) -> JSONData:
    """
    Reads JSON data from a file.

    Args:
        filepath (Union[str, Path]): The path to the JSON file to read.

    Returns:
        JSONData: The JSON data read from the file.

    Raises:
        JSONFileErrorHandler: If a file-related error occurs.
        JSONDecodeErrorHandler: If a JSON decoding error occurs.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileError as e:
        raise JSONFileErrorHandler(f"File error accessing {filepath}: {e}")
    except DecodeError as e:
        raise JSONDecodeErrorHandler(f"Error decoding JSON data at {filepath}: {e}")


def dump_json(filepath: Union[str, Path], indent: int = 2) -> str:
    """
    Reads JSON data from a file, dumps it as a formatted JSON string, and returns it.

    Args:
        filepath (Union[str, Path]): The path to the JSON file to read.
        indent (int): The indentation level for the formatted JSON string (default is 2).

    Returns:
        str: The formatted JSON data as a string.

    Raises:
        JSONFileErrorHandler: If a file-related error occurs.
        JSONEncodeErrorHandler: If a JSON encoding error occurs.
    """
    try:
        with open(filepath, "r") as file:
            return json.dumps(json.load(file), indent=indent)
    except FileError as e:
        raise JSONFileErrorHandler(f"File error accessing {filepath}: {e}")
    except EncodeError as e:
        raise JSONEncodeErrorHandler(f"Error encoding JSON data at {filepath}: {e}")


def write_json(filepath: Union[str, Path], content: JSONData, indent: int = 2) -> None:
    """
    Writes JSON data to a file.

    Args:
        filepath (Union[str, Path]): The path to the JSON file to write.
        content (JSONData): The JSON data to write to the file.
        indent (int): The indentation level for the formatted JSON (default is 2).

    Raises:
        JSONFileErrorHandler: If a file-related error occurs.
        JSONEncodeErrorHandler: If a JSON encoding error occurs.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(content, f, indent=indent)
    except FileError as e:
        raise JSONFileErrorHandler(f"File error accessing {filepath}: {e}")
    except EncodeError as e:
        raise JSONEncodeErrorHandler(
            f"Error encoding and writing JSON data to {filepath}: {e}"
        )


def force_read_json(
    filepath: Union[str, Path], content: JSONData, indent: int = 2
) -> JSONData:
    """
    Reads JSON data from a file or writes default content if decoding fails.

    Args:
        filepath (Union[str, Path]): The path to the JSON file to read or write.
        content (JSONData): The default JSON data to write if reading fails.
        indent (int): The indentation level for the formatted JSON (default is 2).

    Returns:
        JSONData: The JSON data read from the file or default content if reading fails.

    Raises:
        JSONFileErrorHandler: If a file-related error occurs.
        JSONEncodeErrorHandler: If a JSON encoding error occurs.
    """
    try:
        return read_json(filepath)
    except JSONDecodeErrorHandler:
        # If a JSONDecodeErrorHandler occurs (e.g., JSON decoding error),
        # write the default content and return it.
        write_json(filepath, content, indent=indent)
        return content
