"""
jsonpycraft/core/json_base.py

WARNING:
    Be cautious when parsing JSON data from untrusted sources. A malicious JSON string may cause the decoder to consume considerable CPU and memory resources. Limiting the size of data to be parsed is recommended.

REFERENCE:
    https://docs.python.org/3/library/json.html
    https://docs.python.org/3/library/exceptions.html
"""
import json
from pathlib import Path
from typing import Optional, Protocol

from jsonpycraft.core.errors import (
    JSONDecodeErrorHandler,
    JSONEncodeErrorHandler,
    JSONFileErrorHandler,
)
from jsonpycraft.core.types import DecodeError, EncodeError, FileError, JSONData


class JSONBaseTemplate(Protocol):
    """
    A base template class for working with JSON files.

    Properties:
        _file_path (Path): A path-like object pointing to the JSON source file.
        _data (Optional[JSONData]): The internal JSON data structure. May be None if not loaded.
    """

    def __init__(
        self,
        file_path: str,
        initial_data: Optional[JSONData] = None,
    ):
        """
        Initialize a JSONBaseTemplate instance.

        Parameters:
            file_path (str): The path to the JSON file.
            initial_data (Optional[JSONData]): The initial data. Defaults to None.
        """
        self._file_path = Path(file_path)
        self._data: Optional[JSONData] = initial_data

    @property
    def file_path(self) -> Path:
        """
        Get the path to the JSON file.

        Returns:
            Path: The file path.
        """
        return self._file_path

    @property
    def data(self) -> Optional[JSONData]:
        """
        Get the underlying JSON data structure.

        Returns:
            JSONData (Union[JSONMap, JSONList]): The underlying data structure.
        """
        return self._data

    def load_json(self) -> None:
        """
        Load JSON data from the file into the _data attribute.

        Raises:
            JSONFileErrorHandler: If there is a file-related error accessing the JSON file.
            JSONDecodeErrorHandler: If there is an error loading JSON data from the file.
        """
        try:
            with self._file_path.open("r") as file:
                self._data = json.load(file)
        except FileError as e:
            raise JSONFileErrorHandler(f"File error accessing {self._file_path}: {e}")
        except DecodeError as e:
            raise JSONDecodeErrorHandler(
                f"Error loading JSON from {self._file_path}: {e}"
            )

    def save_json(self, data: Optional[JSONData] = None, indent: int = 2) -> None:
        """
        Save JSON data to the file.

        If data is provided, it updates the _data attribute as well.

        Parameters:
            data (Optional[JSONData]): The data to be saved. Defaults to None.
            indent (int): The indentation level for the JSON output. Defaults to 2.

        Raises:
            JSONFileErrorHandler: If there is a file-related error accessing the JSON file.
            JSONEncodeErrorHandler: If there is an error saving JSON data to the file.
        """
        try:
            with self._file_path.open("w") as file:
                if data is not None:
                    json.dump(data, file, indent=indent)
                    self._data = data  # Update the _data attribute if data is provided
                else:
                    json.dump(self._data, file, indent=indent)
        except FileError as e:
            raise JSONFileErrorHandler(f"File error accessing {self._file_path}: {e}")
        except EncodeError as e:
            raise JSONEncodeErrorHandler(f"Error saving JSON to {self._file_path}: {e}")

    def backup_json(self, indent: int = 2) -> None:
        """
        Create a backup of the JSON file.

        Parameters:
            indent (int): The indentation level for the JSON output. Defaults to 2.

        Raises:
            JSONFileErrorHandler: If there is an error creating a backup of the JSON file.
            JSONDecodeErrorHandler: If there is an error loading JSON data from the file.
            JSONEncodeErrorHandler: If there is an error saving JSON data to the file.
        """
        try:
            backup_path = self._file_path.with_suffix(".backup.json")
            with self._file_path.open("r") as original_file, backup_path.open(
                "w"
            ) as backup_file:
                json.dump(json.load(original_file), backup_file, indent=indent)
        except FileError as e:
            raise JSONFileErrorHandler(f"File error accessing {self._file_path}: {e}")
        except DecodeError as e:
            raise JSONDecodeErrorHandler(
                f"Error loading JSON from {self._file_path}: {e}"
            )
        except EncodeError as e:
            raise JSONEncodeErrorHandler(f"Error saving JSON to {self._file_path}: {e}")

    def make_directory(self) -> None:
        """
        Create the directory for the JSON file.

        Raises:
            JSONFileErrorHandler: If there is an error creating the directory for the JSON file.
        """
        try:
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
        except FileError as e:
            raise JSONFileErrorHandler(
                f"Error creating path for {self._file_path}: {e}"
            )
