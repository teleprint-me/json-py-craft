"""
jsonpycraft/json/utils.py
"""
import json
from pathlib import Path
from typing import Union

from jsonpycraft.core.types import DecodeError, EncodeError, JSONData


def read_json(filepath: Union[str, Path]) -> JSONData:
    """
    Read JSON data from a file.

    Args:
        filepath (Union[str, Path]): The path to the JSON file.

    Returns:
        JSONData: The deserialized JSON data.

    Raises:
        DecodeError: If there is an error reading or decoding the JSON data.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except DecodeError as e:
        raise DecodeError(f"Error decoding JSON data at {filepath}: {e}")


def dump_json(filepath: Union[str, Path], indent: int = 2) -> str:
    """
    Serialize JSON data to a formatted string.

    Args:
        filepath (Union[str, Path]): The path to the JSON file.
        indent (int): The number of spaces to use for indentation in the output. Defaults to 2.

    Returns:
        str: The serialized JSON data in a formatted string.

    Raises:
        EncodeError: If there is an error encoding and writing the JSON data.
    """
    try:
        with open(filepath, "r") as file:
            return json.dumps(json.load(file), indent=indent)
    except EncodeError as e:
        raise EncodeError(f"Error encoding JSON data at {filepath}: {e}")


def write_json(filepath: Union[str, Path], content: JSONData, indent: int = 2) -> None:
    """
    Write JSON data to a file.

    Args:
        filepath (Union[str, Path]): The path to the JSON file.
        content (JSONData): The data to be serialized and written as JSON.
        indent (int, optional): The number of spaces to use for indentation. Defaults to 2.

    Raises:
        EncodeError: If there is an error encoding and writing the JSON data.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(content, f, indent=indent)
    except EncodeError as e:
        raise EncodeError(f"Error encoding and writing JSON data to {filepath}: {e}")


def force_read_json(
    filepath: Union[str, Path], content: JSONData, indent: int = 2
) -> JSONData:
    """
    Read JSON data from a file, or create the file with default content if it doesn't exist.

    If the specified file does not exist, it will be created with the provided content.
    This is useful for ensuring that a file exists before reading from it.

    Args:
        filepath (Union[str, Path]): The path to the JSON file.
        content (JSONData): The default content to be written as JSON if the file doesn't exist.
        indent (int, optional): The number of spaces to use for indentation. Defaults to 2.

    Returns:
        JSONData: The deserialized JSON data.

    Raises:
        DecodeError: If there is an error decoding the JSON data.
        EncodeError: If there is an error encoding and writing the JSON data.
    """
    try:
        return read_json(filepath)
    except DecodeError:
        # If the file does not exist or cannot be decoded, write the default content.
        write_json(filepath, content, indent=indent)
        return content
